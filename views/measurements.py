from multiprocessing import Process, Lock, Value
import subprocess
import cmath
from datetime import datetime
from time import sleep

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QAbstractTableModel, Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

import inclinometer
from settings import DB_SESSION
from tools import translate
from models import Station, Measurement
from transmitters import TransmittersTableModel
from vlfrx import STREAM_NAME
from ui.measurements import Ui_MeasurementsView


class ResultsTableModel(QAbstractTableModel):
    H_COL_HEADERS = [
        translate('ResultsTableModel', '% In-Phase'),
        translate('ResultsTableModel', '% Quadrature'),
        translate('ResultsTableModel', 'Tilt Angle')
    ]

    def __init__(self):
        super().__init__()
        self.station = None

    def rowCount(self, *args, **kwargs):
        if not self.station:
            return 0
        return len(self.station.measurements)

    def columnCount(self, *args, **kwargs):
        return len(self.H_COL_HEADERS)

    def headerData(self, section, orientation, role=None):
        if role == Qt.FontRole:
            font = QtGui.QFont()
            font.setPointSize(22)
            font.setBold(True)
            return font
        elif role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.H_COL_HEADERS[section]
            elif orientation == Qt.Vertical:
                return '%.2f kHz' % self.station.measurements[section].freq
        return None

    def itemData(self, index):
        return self.station.measurements[index.row()]

    def data(self, index, role=None):
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter | Qt.AlignVCenter
        elif role == Qt.FontRole:
            font = QtGui.QFont("Monospace")
            font.setStyleHint(QtGui.QFont.Monospace)
            font.setPointSize(24)
            return font
        elif role == Qt.DisplayRole:
            if index.column() == 0:
                return '%+.2f' % self.itemData(index).in_phase
            elif index.column() == 1:
                return '%+.2f' % self.itemData(index).quadrature
            elif index.column() == 2:
                return '-'

    def set_station(self, station):
        self.station = station
        self.layoutChanged.emit()


class MeasurementsView(QtGui.QWidget, Ui_MeasurementsView):
    profile = None
    station = None
    canvas_initiated = False

    def __init__(self, profile, *args, **kwargs):

        self.worker_lock = Lock()
        self.worker_count = Value('i', 0)
        self.tilt_x = Value('f', .0)
        self.tilt_y = Value('f', .0)

        DB_SESSION.expire_all()
        self.profile = profile
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.label_profile_num_val.setText(str(self.profile.id))
        self.label_interval_val.setText("%d m" % self.profile.interval)

        # Transmitters Table
        self.tx_model = TransmittersTableModel()
        self.table_tx.setModel(self.tx_model)

        # Table model view
        self.model = ResultsTableModel()
        self.results_table.setModel(self.model)

        if self.profile.has_stations():
            station = self.profile.get_last_station()
        else:
            station = self.profile.new_station()
        self.set_station(station)

        # Selected Transmitters Updater
        self.table_tx.selectionModel().selectionChanged.connect(self.changed_tx)

        # Inclinometer Updater
        inclinometer.XYThread.updated.connect(self.update_xy)

        # Measure Button Click Signal
        self.button_measure.clicked.connect(self.measure)

        # Next Station Click Signal
        self.button_next_station.clicked.connect(self.show_next_station)

        # Prev Station Click Signal
        self.button_prev_station.clicked.connect(self.show_prev_station)

        # Tab Changed Signal
        self.tabWidget.currentChanged.connect(self.tab_changed)

        # Set Transmitters Table Row Height
        v_header = self.table_tx.verticalHeader()
        v_header.setResizeMode(QtGui.QHeaderView.Fixed)
        v_header.setDefaultSectionSize(42)

        # Set Results Table Row Height
        v_header = self.results_table.verticalHeader()
        v_header.setResizeMode(QtGui.QHeaderView.Fixed)
        v_header.setDefaultSectionSize(50)

    def get_prev_station(self):
        return DB_SESSION.query(Station) \
            .with_parent(self.profile) \
            .filter(Station.point < self.station.point) \
            .order_by(Station.point.desc()) \
            .first()

    def get_next_station(self):
        return DB_SESSION.query(Station) \
            .with_parent(self.profile) \
            .filter(Station.point > self.station.point) \
            .order_by(Station.point.asc()) \
            .first()

    def set_station(self, station):
        self.station = station

        # Set table model
        self.model.set_station(station)

        # Current Point
        self.label_current_point_val.setText(str(self.station.point))

        # Distance
        self.label_distance_val.setText("%d m" % (int(self.profile.interval) * (int(self.station.point) - 1)))

        # Frames
        self.label_frames_val.setText(str(self.station.frames))

        # Resolution
        self.label_resolution_val.setText(str(self.station.resolution))

        # Disable next button if next station not exist
        self.button_next_station.setEnabled(bool(self.station.has_measurements()))

        # Disable prev button if prev station not exist
        prev_station = self.get_prev_station()
        self.button_prev_station.setEnabled(bool(prev_station))

        # (Re)Measure Button Text
        self.button_measure.setText(
            translate("MeasurementsView", 'Remeasure') if self.station.has_measurements()
            else translate("MeasurementsView", 'Measure')
        )

        # Selected Transmitters
        for row_id in range(self.tx_model.rowCount()):
            idx = self.tx_model.index(row_id, 1)
            if self.tx_model.itemData(idx) in self.get_selected_frequencies():
                self.table_tx.selectionModel().select(
                    idx,
                    QtGui.QItemSelectionModel.Select | QtGui.QItemSelectionModel.Rows
                )

    def worker(self, frequency_khz, counter, lock, x, y):
        lock.acquire()
        counter.value += 1
        lock.release()

        second = 10
        frequency = round(frequency_khz * 1000)
        resolution = 10
        frames = 5

        t1 = None
        sum_h = complex(0, 0)  # Horizontal Average
        sum_v = complex(0, 0)  # Vertical Average

        p = subprocess.Popen([
            'vtnspec',  # A narrow band spectrum analyser
            '-f%d' % frequency,  # Center frequency
            '-r%d' % resolution,  # Frequency resolution - bin width in Hertz
            '-N%d' % frames,  # Average up to this many transform frames
            '-c',  # Coherent averaging of frames until end of input
            '-k',  # Repeat mode
            '@%s' % STREAM_NAME  # Input
        ], stdout=subprocess.PIPE)

        # Read each line
        for line in p.stdout:
            # Parse output
            parts = line.decode().split(' ')
            t = float(parts[0])  # time stamp
            hr = float(parts[2])  # horizontal real
            hi = float(parts[3])  # horizontal imaginary
            vr = float(parts[5])  # vertical real
            vi = float(parts[6])  # vertical imaginary

            # Starting a new averaging period?
            if t1 is None:
                t1 = t

            # Measured signals
            h = complex(hr, hi)  # Horizontal signal
            v = complex(vr, vi)  # Vertical signal

            # Make correction using tilt angles
            sum_h += cmath.cos(y.value) * h - cmath.sin(y.value) * v
            sum_v += cmath.sin(y.value) / cmath.cos(x.value) * h + \
                     cmath.cos(y.value) / cmath.cos(x.value) * v

            # End of averaging period?
            if t - t1 > second:
                break

        # Stop vtnspec
        p.terminate()

        ratio = sum_v / sum_h

        # In Phase Ratio
        ip = ratio.real
        # Out of Phase Ratio
        op = ratio.imag

        # Save Measurement
        out = Measurement(
            station=self.station,
            freq=frequency_khz,
            in_phase=ip,
            quadrature=op
        )
        DB_SESSION.add(out)
        DB_SESSION.commit()
        DB_SESSION.merge(out)

        lock.acquire()
        counter.value -= 1
        lock.release()

    def is_measuring(self):
        self.worker_lock.acquire()
        out = self.worker_count.value > 0
        self.worker_lock.release()
        return out

    def measure(self):
        # Do not run if there is working workers
        if self.is_measuring():
            return

        # Change measure button
        self.button_measure.setText(translate("MeasurementsView", 'Working'))
        self.button_measure.setEnabled(False)
        self.button_measure.setStyleSheet('color: red;')

        # Force Qt to change button
        QtCore.QCoreApplication.processEvents()

        # Delete old measurements
        for measurement in self.station.measurements:
            DB_SESSION.delete(measurement)
        DB_SESSION.commit()

        frequencies = self.get_selected_frequencies()
        for freq in frequencies:
            Process(target=self.worker,
                    args=(freq, self.worker_count, self.worker_lock, self.tilt_x, self.tilt_y)).start()

        # Wait for the worker initialization
        sleep(5)

        # TODO: Add a timeout to prevent dead lock
        while True:
            if not self.is_measuring():
                break
            sleep(1)

        self.station.time = datetime.now()
        DB_SESSION.commit()
        self.model.set_station(self.station)

        # Set measure button
        self.button_measure.setText(translate("MeasurementsView", 'Remeasure'))
        self.button_measure.setEnabled(True)
        self.button_measure.setStyleSheet('')

        # Enable next station button
        self.button_next_station.setEnabled(True)

    def update_xy(self, x, y):
        self.tilt_x.value = x
        self.tilt_y.value = y

        abs_x = abs(x)
        abs_y = abs(y)

        x_color = '#DDDDDD'
        y_color = '#DDDDDD'

        if abs_x > 5.0:
            x_color = 'yellow' if 5.0 < abs_x < 10.0 else 'red'

        if abs_y > 5.0:
            y_color = 'yellow' if 5.0 < abs_y < 10.0 else 'red'

        self.lcd_x.setStyleSheet("background-color:%s;" % x_color)
        self.lcd_y.setStyleSheet("background-color:%s;" % y_color)

        # Set text
        self.lcd_x.display("%.2f" % x)
        self.lcd_y.display("%.2f" % y)

    def changed_tx(self):
        selected = sorted(map(self.tx_model.itemData, self.table_tx.selectionModel().selectedRows()))
        self.profile.transmitters = ','.join(map(str, selected))
        DB_SESSION.commit()

    def show_next_station(self):
        if not self.station.has_measurements():
            return

        station = self.get_next_station()
        if not station:
            station = self.profile.new_station()
        self.set_station(station)

    def show_prev_station(self):
        station = self.get_prev_station()
        if station:
            self.set_station(station)

    def get_selected_frequencies(self):
        return list(map(float, str(self.profile.transmitters).split(',')))

    def tab_changed(self, index):
        if index == 1:
            self.plot_profile()

    def init_profile_canvas(self):
        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        self.profile_layout.insertWidget(0, self.canvas)

        # create an axis
        self.axes = self.figure.add_subplot(111)

        # Set canvas as initiated
        self.canvas_initiated = True

    def plot_profile(self):
        if not self.canvas_initiated:
            self.init_profile_canvas()

        data = {}

        for station in DB_SESSION.query(Station).with_parent(self.profile).order_by(Station.point.asc()):
            distance = int(self.profile.interval) * (int(station.point) - 1)
            for measurement in station.measurements:
                freq = '%.2f' % measurement.freq
                if freq not in data:
                    data[freq] = [[], [], []]
                data[freq][0].append(distance)
                data[freq][1].append(measurement.in_phase)
                data[freq][2].append(measurement.quadrature)

        for f in data:
            self.axes.plot(data[f][0], data[f][1], label="%.2f kHz IP" % float(f))
            self.axes.hold(True)
            self.axes.plot(data[f][0], data[f][2], label="%.2f kHz OP" % float(f))
            self.axes.hold(True)
        self.axes.hold(False)

        # Title
        self.figure.suptitle('Profile #%d' % (
            int(self.profile.id)
        ))

        self.axes.grid(True, which='both')

        self.axes.set_xlabel(translate('MeasurementsView', 'Distance'))
        self.axes.set_ylabel(translate('MeasurementsView', '% HS/HP'))

        self.axes.legend(loc='upper right', shadow=True)
