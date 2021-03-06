# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/ecabuk/Projects/vlf/ui/spectrum.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SpectrumView(object):
    def setupUi(self, SpectrumView):
        SpectrumView.setObjectName(_fromUtf8("SpectrumView"))
        SpectrumView.resize(800, 480)
        SpectrumView.setAutoFillBackground(True)
        self.verticalLayoutWidget = QtGui.QWidget(SpectrumView)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 801, 481))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.layout_main = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_main.setObjectName(_fromUtf8("layout_main"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.layout_main.addItem(spacerItem)
        self.label_wait = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_wait.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wait.setObjectName(_fromUtf8("label_wait"))
        self.layout_main.addWidget(self.label_wait)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.layout_main.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_average = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_average.setFont(font)
        self.label_average.setObjectName(_fromUtf8("label_average"))
        self.horizontalLayout.addWidget(self.label_average)
        self.lcd_h_average = QtGui.QLCDNumber(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lcd_h_average.setFont(font)
        self.lcd_h_average.setFrameShape(QtGui.QFrame.Box)
        self.lcd_h_average.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcd_h_average.setSmallDecimalPoint(False)
        self.lcd_h_average.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_h_average.setProperty("value", 0.999)
        self.lcd_h_average.setObjectName(_fromUtf8("lcd_h_average"))
        self.horizontalLayout.addWidget(self.lcd_h_average)
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_average_2 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_average_2.setFont(font)
        self.label_average_2.setObjectName(_fromUtf8("label_average_2"))
        self.horizontalLayout.addWidget(self.label_average_2)
        self.lcd_v_average = QtGui.QLCDNumber(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lcd_v_average.setFont(font)
        self.lcd_v_average.setFrameShape(QtGui.QFrame.Box)
        self.lcd_v_average.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcd_v_average.setSmallDecimalPoint(False)
        self.lcd_v_average.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_v_average.setProperty("value", 0.999)
        self.lcd_v_average.setObjectName(_fromUtf8("lcd_v_average"))
        self.horizontalLayout.addWidget(self.lcd_v_average)
        spacerItem3 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_x = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_x.setFont(font)
        self.label_x.setObjectName(_fromUtf8("label_x"))
        self.horizontalLayout.addWidget(self.label_x)
        self.lcd_x = QtGui.QLCDNumber(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lcd_x.setFont(font)
        self.lcd_x.setStyleSheet(_fromUtf8(""))
        self.lcd_x.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcd_x.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_x.setProperty("value", 89.9)
        self.lcd_x.setObjectName(_fromUtf8("lcd_x"))
        self.horizontalLayout.addWidget(self.lcd_x)
        spacerItem4 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label_y = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_y.setFont(font)
        self.label_y.setObjectName(_fromUtf8("label_y"))
        self.horizontalLayout.addWidget(self.label_y)
        self.lcd_y = QtGui.QLCDNumber(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lcd_y.setFont(font)
        self.lcd_y.setStyleSheet(_fromUtf8(""))
        self.lcd_y.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcd_y.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_y.setProperty("value", 89.9)
        self.lcd_y.setObjectName(_fromUtf8("lcd_y"))
        self.horizontalLayout.addWidget(self.lcd_y)
        spacerItem5 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.lcd_time = QtGui.QLCDNumber(self.verticalLayoutWidget)
        self.lcd_time.setStyleSheet(_fromUtf8("color: #111111;"))
        self.lcd_time.setFrameShadow(QtGui.QFrame.Raised)
        self.lcd_time.setDigitCount(8)
        self.lcd_time.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_time.setProperty("value", 0.0)
        self.lcd_time.setProperty("intValue", 0)
        self.lcd_time.setObjectName(_fromUtf8("lcd_time"))
        self.horizontalLayout.addWidget(self.lcd_time)
        spacerItem6 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.button_options = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.button_options.setFont(font)
        self.button_options.setObjectName(_fromUtf8("button_options"))
        self.horizontalLayout.addWidget(self.button_options)
        self.button_save = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.button_save.setFont(font)
        self.button_save.setObjectName(_fromUtf8("button_save"))
        self.horizontalLayout.addWidget(self.button_save)
        self.button_close = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_close.setMinimumSize(QtCore.QSize(0, 0))
        self.button_close.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.button_close.setFont(font)
        self.button_close.setObjectName(_fromUtf8("button_close"))
        self.horizontalLayout.addWidget(self.button_close)
        self.layout_main.addLayout(self.horizontalLayout)

        self.retranslateUi(SpectrumView)
        QtCore.QObject.connect(self.button_close, QtCore.SIGNAL(_fromUtf8("clicked()")), SpectrumView.close)
        QtCore.QMetaObject.connectSlotsByName(SpectrumView)

    def retranslateUi(self, SpectrumView):
        SpectrumView.setWindowTitle(_translate("SpectrumView", "Spectrum", None))
        self.label_wait.setText(_translate("SpectrumView", "Please wait for the initial data...", None))
        self.label_average.setText(_translate("SpectrumView", "HA", None))
        self.label_average_2.setText(_translate("SpectrumView", "VA", None))
        self.label_x.setText(_translate("SpectrumView", "X", None))
        self.label_y.setText(_translate("SpectrumView", "Y", None))
        self.button_options.setText(_translate("SpectrumView", "Options", None))
        self.button_save.setText(_translate("SpectrumView", "Save", None))
        self.button_close.setText(_translate("SpectrumView", "Close", None))

import resources_rc
