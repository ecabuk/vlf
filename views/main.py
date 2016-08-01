from PyQt4.QtCore import QAbstractTableModel, Qt

from PyQt4 import QtGui, QtCore
import inclinometer
import vlfrx
from settings import SETTINGS, DB_SESSION
from models import Profile, Station
from tools import translate
from ui.main import Ui_MainView
from views.spectrum import SpectrumView
from views.inclinometer import InclinometerView
from views.license import LicenseView
from views.measurements import MeasurementsView


class ProfilesTableModel(QAbstractTableModel):
    H_COL_HEADERS = [
        translate('ProfilesTableModel', 'Profile #'),
        translate('ProfilesTableModel', 'Interval'),
        translate('ProfilesTableModel', 'Points')
    ]

    def __init__(self):
        super().__init__()

    def rowCount(self, *args, **kwargs):
        return DB_SESSION.query(Profile).count()

    def columnCount(self, *args, **kwargs):
        return 3

    def data(self, index, role=None):
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter | Qt.AlignVCenter
        elif role == Qt.DisplayRole:
            data = DB_SESSION.query(Profile)[index.row()]
            if index.column() == 0:
                return data.id
            elif index.column() == 1:
                return data.interval
            elif index.column() == 2:
                return DB_SESSION.query(Station).with_parent(data).count()

    def itemData(self, index):
        return DB_SESSION.query(Profile)[index.row()]

    def headerData(self, section, orientation, role=None):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.H_COL_HEADERS[section]


class MainView(QtGui.QWidget, Ui_MainView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Table
        self.model = ProfilesTableModel()
        self.table_profiles.setModel(self.model)

        # Set Row Height
        v_header = self.table_profiles.verticalHeader()
        v_header.setResizeMode(QtGui.QHeaderView.Fixed)
        v_header.setDefaultSectionSize(42)

        self.button_close.clicked.connect(self.close_application)

    @QtCore.pyqtSlot()
    def on_button_delete_clicked(self):
        selected = self.table_profiles.selectedIndexes()
        if not selected:
            return

        index = selected[0]
        model = self.model.itemData(index)
        DB_SESSION.delete(model)
        DB_SESSION.commit()
        self.model.layoutChanged.emit()

    @QtCore.pyqtSlot()
    def on_button_continue_clicked(self):
        selected = self.table_profiles.selectedIndexes()
        if not selected:
            return

        index = selected[0]
        model = self.model.itemData(index)
        view = MeasurementsView(model, parent=self)
        view.show()

    @QtCore.pyqtSlot()
    def on_button_new_clicked(self):
        new_profile = Profile.create_new()
        self.model.layoutChanged.emit()
        view = MeasurementsView(new_profile, parent=self)
        view.show()

    @QtCore.pyqtSlot()
    def on_button_options_clicked(self):
        pass

    @QtCore.pyqtSlot()
    def on_button_spectrum_clicked(self):
        view = SpectrumView(parent=self)
        view.show()

    @QtCore.pyqtSlot()
    def on_button_inclinometer_clicked(self):
        view = InclinometerView(parent=self)
        view.show()

    @QtCore.pyqtSlot()
    def on_button_license_clicked(self):
        view = LicenseView(parent=self)
        view.show()

    def close_application(self):
        # Stop reading
        inclinometer.stop_readings()

        # Stop sound card reading
        vlfrx.stop_reading()

        # Close App
        QtCore.QCoreApplication.instance().quit()

    def set_interval(self, val):
        SETTINGS.setValue('last_session/profile_interval', int(val))
        self.input_interval.setText(str(val))
