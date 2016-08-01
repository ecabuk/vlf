from PyQt4 import QtGui, QtCore

from tools import set_mic_vol, get_mic_vol, translate
from settings import SETTINGS
from transmitters import TransmittersTableModel
from ui.spectrum_options import Ui_SpectrumOptionsView

option_lock = QtCore.QMutex()


class SpectrumOptionsView(QtGui.QWidget, Ui_SpectrumOptionsView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Initiate Channel Buttons
        self.ch_buttons()

        # Mic Volume
        self.bar_volume.setValue(get_mic_vol())

        # Resolution
        self.create_row(
            title=translate('SpectrumOptions', 'Resolution'),
            option_key='spectrum/resolution',
            default=10,
            min_=5,
            max_=100,
            step=5,
            format_='%d'
        )

        # Measurement Time
        self.create_row(
            title=translate('SpectrumOptions', 'Frames'),
            option_key='spectrum/frames',
            default=100,
            min_=10,
            max_=200,
            step=10,
            format_='%d'
        )

        # Y Max
        self.create_row(
            title=translate('SpectrumOptions', 'Y Max'),
            option_key='spectrum/y_max',
            default=0.1,
            min_=0,
            max_=1,
            step=0.05,
            format_='%.2f'
        )

        # X Min
        self.create_row(
            title=translate('SpectrumOptions', 'X Min'),
            option_key='spectrum/x_min',
            default=15000,
            min_=0,
            max_=47999,
            step=1000,
            format_='%d'
        )

        # X Max
        self.create_row(
            title=translate('SpectrumOptions', 'X Max'),
            option_key='spectrum/x_max',
            default=30000,
            min_=1,
            max_=48000,
            step=1000,
            format_='%d'
        )

        # Selected Transmitters
        self.tx_model = TransmittersTableModel()
        self.table_tx.setModel(self.tx_model)

        # Set Row Height
        v_header = self.table_tx.verticalHeader()
        v_header.setResizeMode(QtGui.QHeaderView.Fixed)
        v_header.setDefaultSectionSize(42)

        selected = self.get_selected_frequencies()
        for row_id in range(self.tx_model.rowCount()):
            idx = self.tx_model.index(row_id, 1)
            if self.tx_model.itemData(idx) in selected:
                self.table_tx.selectionModel().select(
                    idx,
                    QtGui.QItemSelectionModel.Select | QtGui.QItemSelectionModel.Rows
                )
        self.table_tx.selectionModel().selectionChanged.connect(self.changed_tx)

    @staticmethod
    def get_selected_frequencies():
        option_lock.lock()
        out = str(SETTINGS.value('spectrum/frequencies', '')).split(',')

        def is_float(val):
            try:
                float(val)
                return True
            except ValueError:
                return False

        out = list(map(float, filter(is_float, out)))
        option_lock.unlock()
        return out

    def ch_buttons(self):
        option_lock.lock()

        # Uncheck all buttons
        self.button_c_h.setChecked(False)
        self.button_c_v.setChecked(False)
        self.button_c_vh.setChecked(False)

        chs = SETTINGS.value('spectrum/channels', '1,2', str).split(',')
        ch_h = '1' in chs
        ch_v = '2' in chs

        if ch_v and ch_h:
            self.button_c_vh.setChecked(True)
        elif ch_h:
            self.button_c_h.setChecked(True)
        elif ch_v:
            self.button_c_v.setChecked(True)

        option_lock.unlock()

    @QtCore.pyqtSlot()
    def on_button_vol_up_clicked(self):
        option_lock.lock()
        new = int(get_mic_vol()) + 10
        new = new if new <= 100 else 100
        set_mic_vol(new)
        self.bar_volume.setValue(get_mic_vol())
        option_lock.unlock()

    @QtCore.pyqtSlot()
    def on_button_vol_down_clicked(self):
        option_lock.lock()
        new = int(get_mic_vol()) - 10
        new = new if new >= 0 else 0
        set_mic_vol(new)
        self.bar_volume.setValue(get_mic_vol())
        option_lock.unlock()

    @QtCore.pyqtSlot()
    def on_button_c_h_clicked(self):
        SETTINGS.setValue('spectrum/channels', '1')
        self.ch_buttons()

    @QtCore.pyqtSlot()
    def on_button_c_v_clicked(self):
        SETTINGS.setValue('spectrum/channels', '2')
        self.ch_buttons()

    @QtCore.pyqtSlot()
    def on_button_c_vh_clicked(self):
        SETTINGS.setValue('spectrum/channels', '1,2')
        self.ch_buttons()

    def create_row(self, title, option_key, default, min_, max_, step, format_):
        def get_val():
            option_lock.lock()
            out = SETTINGS.value(option_key, default, float)
            option_lock.unlock()
            return out

        def set_val(new_val):
            option_lock.lock()
            SETTINGS.setValue(option_key, new_val)
            option_lock.unlock()

        def show_val():
            lcd.display(str(format_ % get_val()))

        def up_clicked():
            new_val = get_val() + step
            new_val = new_val if new_val <= max_ else max_
            set_val(new_val)
            show_val()

        def down_clicked():
            new_val = get_val() - step
            new_val = new_val if new_val >= min_ else min_
            set_val(new_val)
            show_val()

        # Add spacer before
        self.left_layout.addItem(QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding))

        # Row
        row = QtGui.QHBoxLayout()

        # Title
        title_o = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        title_o.setFont(font)
        title_o.setText(title)
        row.addWidget(title_o)

        # Spacer
        row.addItem(QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))

        # LCD
        lcd = QtGui.QLCDNumber(self.verticalLayoutWidget)
        lcd.setMinimumSize(QtCore.QSize(110, 0))
        lcd.setNumDigits(5)
        row.addWidget(lcd)

        # Down Button
        button_down = QtGui.QPushButton(self.verticalLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/down_arrow_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button_down.setIcon(icon)
        button_down.setIconSize(QtCore.QSize(32, 32))
        row.addWidget(button_down)

        # Up Button
        button_up = QtGui.QPushButton(self.verticalLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/assets/icons/up_arrow_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button_up.setIcon(icon1)
        button_up.setIconSize(QtCore.QSize(32, 32))
        row.addWidget(button_up)

        button_up.clicked.connect(up_clicked)
        button_down.clicked.connect(down_clicked)

        show_val()

        self.left_layout.addLayout(row)

    def changed_resolution(self, val, save_val=True):
        self.label_resolution_val.setText("%d Hz" % val)
        if save_val:
            SETTINGS.setValue('spectrum/resolution', val)

    def changed_tx(self, *args, **kwargs):
        selected = sorted(map(self.tx_model.itemData, self.table_tx.selectionModel().selectedRows()))
        SETTINGS.setValue('spectrum/frequencies', ','.join(map(str, selected)))
