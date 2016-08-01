from PyQt4 import QtGui, QtCore

import inclinometer
from tools import translate

from ui.inclinometer import Ui_InclinometerView


class InclinometerView(QtGui.QWidget, Ui_InclinometerView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Add frequencies to list
        current_ff = inclinometer.read_ff()
        for ms in sorted(map(int, list(inclinometer.FF_INDEX.keys()))):
            freq = inclinometer.FF_INDEX[str(ms)]
            self.select_filter_freq.addItem("%s Hz" % freq[0], freq[1])

            # Select Current Frequency
            if current_ff == freq[0]:
                self.select_filter_freq.setCurrentIndex(self.select_filter_freq.findData(freq[1]))

        # X & Y Signal
        inclinometer.XYThread.updated.connect(self.update_xy)

        # T Signal
        inclinometer.TThread.updated.connect(self.update_t)

        # Filter Change Signal
        self.select_filter_freq.currentIndexChanged.connect(self.filter_changed)

    def update_t(self, t):
        self.lcd_t.display('%.1f' % t)

    def update_xy(self, x, y):
        self.lcd_x.display('%.2f' % x)
        self.lcd_y.display('%.2f' % y)

    def filter_changed(self, index):
        inclinometer.set_filter_frequency(self.select_filter_freq.itemData(index))

    @staticmethod
    def _confirm_box(msg):
        confirm = QtGui.QMessageBox()
        confirm.setIcon(QtGui.QMessageBox.Warning)
        confirm.setWindowTitle(translate('InclinometerView', 'Confirmation'))
        confirm.setText(msg)
        confirm.setStandardButtons(QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)
        confirm.setDefaultButton(QtGui.QMessageBox.No)
        return confirm.exec()

    @QtCore.pyqtSlot()
    def on_button_zero_set_clicked(self):
        ret = self._confirm_box(
            translate('InclinometerView', 'Do you really want to set the current position to zero?'))
        if ret == QtGui.QMessageBox.Yes:
            inclinometer.set_zero()

    @QtCore.pyqtSlot()
    def on_button_zero_reset_clicked(self):
        ret = self._confirm_box(translate('InclinometerView', 'Do you really want to reset zero to factory settings?'))
        if ret == QtGui.QMessageBox.Yes:
            inclinometer.reset_zero()
