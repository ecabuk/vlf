# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/ecabuk/Projects/vlf/ui/main.ui'
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

class Ui_MainView(object):
    def setupUi(self, MainView):
        MainView.setObjectName(_fromUtf8("MainView"))
        MainView.resize(800, 480)
        self.button_new = QtGui.QPushButton(MainView)
        self.button_new.setGeometry(QtCore.QRect(600, 10, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_new.setFont(font)
        self.button_new.setStyleSheet(_fromUtf8("background-color:#5cb85c;\n"
"border: 1px solid #4cae4c;\n"
"color:#fff;\n"
"border-radius: 4px;"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/icons/camera_flash_24.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_new.setIcon(icon)
        self.button_new.setIconSize(QtCore.QSize(24, 24))
        self.button_new.setCheckable(False)
        self.button_new.setDefault(False)
        self.button_new.setFlat(False)
        self.button_new.setObjectName(_fromUtf8("button_new"))
        self.button_options = QtGui.QPushButton(MainView)
        self.button_options.setGeometry(QtCore.QRect(599, 90, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_options.setFont(font)
        self.button_options.setStyleSheet(_fromUtf8("background-color:#337ab7;\n"
"border: 1px solid #2e6da4;\n"
"color:#fff;\n"
"border-radius: 4px;"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/icons/settings_gears_24.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_options.setIcon(icon1)
        self.button_options.setIconSize(QtCore.QSize(24, 24))
        self.button_options.setObjectName(_fromUtf8("button_options"))
        self.button_license = QtGui.QPushButton(MainView)
        self.button_license.setGeometry(QtCore.QRect(600, 330, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_license.setFont(font)
        self.button_license.setStyleSheet(_fromUtf8("background-color:#5bc0de;\n"
"border: 1px solid #46b8da;\n"
"color:#fff;\n"
"border-radius: 4px;"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/icons/copyright_24.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_license.setIcon(icon2)
        self.button_license.setIconSize(QtCore.QSize(24, 24))
        self.button_license.setObjectName(_fromUtf8("button_license"))
        self.button_spectrum = QtGui.QPushButton(MainView)
        self.button_spectrum.setGeometry(QtCore.QRect(600, 170, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_spectrum.setFont(font)
        self.button_spectrum.setStyleSheet(_fromUtf8("background-color:#FFDC00;\n"
"border: 1px solid #e6c600;\n"
"color:#333;\n"
"border-radius: 4px;"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/icons/analytics_chart_24.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_spectrum.setIcon(icon3)
        self.button_spectrum.setIconSize(QtCore.QSize(24, 24))
        self.button_spectrum.setObjectName(_fromUtf8("button_spectrum"))
        self.button_close = QtGui.QPushButton(MainView)
        self.button_close.setGeometry(QtCore.QRect(600, 410, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_close.setFont(font)
        self.button_close.setStyleSheet(_fromUtf8("background-color:#d9534f;\n"
"border: 1px solid #d43f3a;\n"
"color:#fff;\n"
"border-radius: 4px;"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/icons/power_24.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_close.setIcon(icon4)
        self.button_close.setIconSize(QtCore.QSize(24, 24))
        self.button_close.setObjectName(_fromUtf8("button_close"))
        self.button_inclinometer = QtGui.QPushButton(MainView)
        self.button_inclinometer.setGeometry(QtCore.QRect(600, 250, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_inclinometer.setFont(font)
        self.button_inclinometer.setStyleSheet(_fromUtf8("background-color:#39CCCC;\n"
"border: 1px solid #30bbbb;\n"
"color:#333;\n"
"border-radius: 4px;"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/icons/angle_button_24.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_inclinometer.setIcon(icon5)
        self.button_inclinometer.setIconSize(QtCore.QSize(24, 24))
        self.button_inclinometer.setObjectName(_fromUtf8("button_inclinometer"))
        self.line_right = QtGui.QFrame(MainView)
        self.line_right.setGeometry(QtCore.QRect(570, 0, 20, 481))
        self.line_right.setFrameShape(QtGui.QFrame.VLine)
        self.line_right.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_right.setObjectName(_fromUtf8("line_right"))
        self.table_profiles = QtGui.QTableView(MainView)
        self.table_profiles.setGeometry(QtCore.QRect(20, 50, 551, 361))
        self.table_profiles.setStyleSheet(_fromUtf8("QScrollBar:vertical { width: 30px; }"))
        self.table_profiles.setDragDropOverwriteMode(False)
        self.table_profiles.setAlternatingRowColors(True)
        self.table_profiles.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table_profiles.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_profiles.setObjectName(_fromUtf8("table_profiles"))
        self.table_profiles.horizontalHeader().setVisible(True)
        self.table_profiles.horizontalHeader().setDefaultSectionSize(100)
        self.table_profiles.horizontalHeader().setMinimumSectionSize(100)
        self.table_profiles.horizontalHeader().setStretchLastSection(True)
        self.table_profiles.verticalHeader().setVisible(False)
        self.label_profiles = QtGui.QLabel(MainView)
        self.label_profiles.setGeometry(QtCore.QRect(20, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_profiles.setFont(font)
        self.label_profiles.setObjectName(_fromUtf8("label_profiles"))
        self.button_continue = QtGui.QPushButton(MainView)
        self.button_continue.setGeometry(QtCore.QRect(430, 420, 141, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_continue.setFont(font)
        self.button_continue.setStyleSheet(_fromUtf8("background-color:#fff;\n"
"border: 1px solid #ccc;\n"
"color:#333;\n"
"border-radius: 4px;"))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/icons/play_button_24.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_continue.setIcon(icon6)
        self.button_continue.setIconSize(QtCore.QSize(24, 24))
        self.button_continue.setObjectName(_fromUtf8("button_continue"))
        self.button_delete = QtGui.QPushButton(MainView)
        self.button_delete.setGeometry(QtCore.QRect(20, 420, 141, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_delete.setFont(font)
        self.button_delete.setStyleSheet(_fromUtf8("background-color:#fff;\n"
"border: 1px solid #ccc;\n"
"color:#333;\n"
"border-radius: 4px;"))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/icons/round_delete_button_24.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_delete.setIcon(icon7)
        self.button_delete.setIconSize(QtCore.QSize(24, 24))
        self.button_delete.setObjectName(_fromUtf8("button_delete"))

        self.retranslateUi(MainView)
        QtCore.QMetaObject.connectSlotsByName(MainView)

    def retranslateUi(self, MainView):
        MainView.setWindowTitle(_translate("MainView", "Main", None))
        self.button_new.setText(_translate("MainView", "New Profile", None))
        self.button_options.setText(_translate("MainView", "Options", None))
        self.button_license.setText(_translate("MainView", "License", None))
        self.button_spectrum.setText(_translate("MainView", "Spectrum", None))
        self.button_close.setText(_translate("MainView", "Close", None))
        self.button_inclinometer.setText(_translate("MainView", "Inclinometer", None))
        self.label_profiles.setText(_translate("MainView", "Profiles", None))
        self.button_continue.setText(_translate("MainView", "Continue", None))
        self.button_delete.setText(_translate("MainView", "Delete", None))

import resources_rc
