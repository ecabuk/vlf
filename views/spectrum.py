from time import sleep
from datetime import datetime
import subprocess

import os
from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import vlfrx
import inclinometer
from settings import SETTINGS, EXPORTS_DIR
from tools import translate, HZ_2_KHZ_FORMATTER, get_mic_vol
from ui.spectrum import Ui_SpectrumView
from views.spectrum_options import SpectrumOptionsView, option_lock
from transmitters import TRANSMITTERS

render_wait = QtCore.QWaitCondition()
mutex = QtCore.QMutex()
render_lock = QtCore.QMutex()


class TimeThread(QtCore.QThread):
    updated = QtCore.pyqtSignal(str)

    def run(self):
        while True:
            time = QtCore.QTime.currentTime()
            self.updated.emit("%s:%s%s%s" % (
                time.toString("hh"),
                time.toString("mm"),
                (' ' if (time.second() % 2) == 0 else ':'),
                time.toString("ss"),
            ))
            sleep(1)


class SpectrumReadThread(QtCore.QThread):
    updated = QtCore.pyqtSignal(list)

    def run(self):
        while True:
            self.updated.emit(vlfrx.wideband_spectrum(
                SETTINGS.value('spectrum/resolution', 10, int),
                SETTINGS.value('spectrum/frames', 100, int),
                SETTINGS.value('spectrum/channels', '1,2')
            ))

            # Wait for render
            render_wait.wait(mutex)


class AverageAmplitudesReadThread(QtCore.QThread):
    updated = QtCore.pyqtSignal(float, float)

    def run(self):
        while True:
            self.updated.emit(*vlfrx.average_amplitudes(1))


class SpectrumView(QtGui.QWidget, Ui_SpectrumView):
    canvas_initiated = False
    current_aa_v = 0
    current_aa_h = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Start Spectrum Read Thread
        self.sr_thread = SpectrumReadThread()
        self.sr_thread.start(QtCore.QThread.HighPriority)

        # Start Time Thread
        self.time_thread = TimeThread()
        self.time_thread.start(QtCore.QThread.LowPriority)

        # Connect signals
        self.sr_thread.updated.connect(self.plot)
        self.time_thread.updated.connect(self.update_time)
        inclinometer.XYThread.updated.connect(self.update_xy)

        # Average Amplitudes
        self.aa_thread = AverageAmplitudesReadThread()
        self.aa_thread.start(QtCore.QThread.NormalPriority)
        self.aa_thread.updated.connect(self.update_average_amplitudes)

    def update_xy(self, x, y):
        self.lcd_x.display('%.1f' % x)
        self.lcd_y.display('%.1f' % y)

    def update_time(self, val):
        self.lcd_time.display(val)

    def update_average_amplitudes(self, h, v):
        self.current_aa_h = h
        self.current_aa_v = v
        self.lcd_h_average.display(h)
        self.lcd_v_average.display(v)

    def init_canvas(self):
        self.label_wait.deleteLater()

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        self.layout_main.insertWidget(0, self.canvas)

        # create an axis
        self.axes = self.figure.add_subplot(111)

        # Set canvas as initiated
        self.canvas_initiated = True

    def plot(self, data):
        render_lock.lock()
        option_lock.lock()
        if not self.canvas_initiated:
            self.init_canvas()

        # Plot
        ch = SETTINGS.value('spectrum/channels', '1,2')
        c = 0
        for ch in ch.split(','):
            self.axes.plot(
                data[c * 2], data[c * 2 + 1],
                color='r' if ch == '1' else 'b',
                label='Horizontal' if ch == '1' else 'Vertical'
            )
            c += 1
            self.axes.hold(True)
        self.axes.hold(False)

        # Title
        self.figure.suptitle('%s R=%d F=%d AH=%.2f AV=%.2f V=%d' % (
            datetime.now().strftime('%c'),
            SETTINGS.value('spectrum/resolution', 10, int),
            SETTINGS.value('spectrum/frames', 10, int),
            self.current_aa_h,
            self.current_aa_v,
            get_mic_vol()
        ))

        # Grid
        self.axes.grid(True, which='both')

        self.axes.set_xlim([SETTINGS.value('spectrum/x_min', 15000, int), SETTINGS.value('spectrum/x_max', 30000, int)])
        y_max = SETTINGS.value('spectrum/y_max', 0.1, float)
        if y_max > 0:
            self.axes.set_ylim([0, y_max])
        # Labels
        self.axes.set_xlabel(translate('SpectrumView', 'Frequency [kHz]'))
        self.axes.set_ylabel(translate('SpectrumView', 'Amplitude'))

        option_lock.unlock()

        # Transmitter indicators
        selected = SpectrumOptionsView.get_selected_frequencies()

        if len(selected):
            frequencies = []
            for tx in TRANSMITTERS:
                freq = float(tx[0])
                if freq in selected:
                    frequencies.append([freq, tx[1]])

            # Color Map
            scalar_color_map = cmx.ScalarMappable(
                norm=colors.Normalize(vmin=1, vmax=len(frequencies)),
                cmap=plt.get_cmap('Dark2')
            )
            clr_idx = 0
            for freq in frequencies:
                clr_idx += 1
                self.axes.axvline(
                    freq[0] * 1000,
                    linewidth=2,
                    color=scalar_color_map.to_rgba(clr_idx),
                    alpha=0.9,
                    linestyle='-',
                    label="%.2f kHz [%s]" % (freq[0], freq[1])
                )

        self.axes.legend(prop={'family': 'monospace', 'size': 'small'})

        self.axes.xaxis.set_major_formatter(HZ_2_KHZ_FORMATTER)

        # Refresh canvas
        self.canvas.draw()

        render_lock.unlock()

        # Start the calculation again
        render_wait.wakeAll()

    @QtCore.pyqtSlot()
    def on_button_save_clicked(self):
        render_lock.lock()
        self.figure.savefig(
            os.path.join(EXPORTS_DIR, 'spectrum', '%s.pdf' % datetime.now().isoformat()),
            dpi=300,
            orientation='portrait',
            papertype='a4',
            format='pdf',
        )
        render_lock.unlock()

    @QtCore.pyqtSlot()
    def on_button_close_clicked(self):
        subprocess.call(["killall", 'vtcard'])

        super().close()

    @QtCore.pyqtSlot()
    def on_button_options_clicked(self):
        view = SpectrumOptionsView(parent=self)
        view.show()
