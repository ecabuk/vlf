# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/ecabuk/Projects/vlf/ui/intro.ui'
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

class Ui_IntroView(object):
    def setupUi(self, IntroView):
        IntroView.setObjectName(_fromUtf8("IntroView"))
        IntroView.resize(800, 480)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(IntroView)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(13, 90, 779, 387))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.logo_itu = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.logo_itu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.logo_itu.setText(_fromUtf8(""))
        self.logo_itu.setPixmap(QtGui.QPixmap(_fromUtf8(":/logo/assets/itu_logo.png")))
        self.logo_itu.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.logo_itu.setObjectName(_fromUtf8("logo_itu"))
        self.verticalLayout_2.addWidget(self.logo_itu)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem2 = QtGui.QSpacerItem(20, 50, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.label_itu = QtGui.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_itu.setFont(font)
        self.label_itu.setStyleSheet(_fromUtf8(""))
        self.label_itu.setTextFormat(QtCore.Qt.RichText)
        self.label_itu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_itu.setObjectName(_fromUtf8("label_itu"))
        self.verticalLayout.addWidget(self.label_itu)
        self.label_faculty = QtGui.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_faculty.setFont(font)
        self.label_faculty.setTextFormat(QtCore.Qt.RichText)
        self.label_faculty.setAlignment(QtCore.Qt.AlignCenter)
        self.label_faculty.setObjectName(_fromUtf8("label_faculty"))
        self.verticalLayout.addWidget(self.label_faculty)
        self.label_department = QtGui.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_department.setFont(font)
        self.label_department.setTextFormat(QtCore.Qt.RichText)
        self.label_department.setAlignment(QtCore.Qt.AlignCenter)
        self.label_department.setObjectName(_fromUtf8("label_department"))
        self.verticalLayout.addWidget(self.label_department)
        spacerItem3 = QtGui.QSpacerItem(20, 50, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_gunal = QtGui.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_gunal.setFont(font)
        self.label_gunal.setTextFormat(QtCore.Qt.RichText)
        self.label_gunal.setObjectName(_fromUtf8("label_gunal"))
        self.horizontalLayout_2.addWidget(self.label_gunal)
        spacerItem4 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.line_2 = QtGui.QFrame(self.horizontalLayoutWidget_3)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_2.addWidget(self.line_2)
        spacerItem5 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.label_evrim = QtGui.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_evrim.setFont(font)
        self.label_evrim.setTextFormat(QtCore.Qt.RichText)
        self.label_evrim.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_evrim.setObjectName(_fromUtf8("label_evrim"))
        self.horizontalLayout_2.addWidget(self.label_evrim)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtGui.QSpacerItem(20, 50, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem6)
        self.label_year = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.label_year.setAlignment(QtCore.Qt.AlignCenter)
        self.label_year.setObjectName(_fromUtf8("label_year"))
        self.verticalLayout.addWidget(self.label_year)
        spacerItem7 = QtGui.QSpacerItem(20, 50, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayoutWidget = QtGui.QWidget(IntroView)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 59))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_appname = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_appname.setTextFormat(QtCore.Qt.RichText)
        self.label_appname.setScaledContents(True)
        self.label_appname.setAlignment(QtCore.Qt.AlignCenter)
        self.label_appname.setWordWrap(True)
        self.label_appname.setObjectName(_fromUtf8("label_appname"))
        self.horizontalLayout.addWidget(self.label_appname)
        self.line_h = QtGui.QFrame(IntroView)
        self.line_h.setGeometry(QtCore.QRect(0, 70, 801, 20))
        self.line_h.setFrameShape(QtGui.QFrame.HLine)
        self.line_h.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h.setObjectName(_fromUtf8("line_h"))

        self.retranslateUi(IntroView)
        QtCore.QMetaObject.connectSlotsByName(IntroView)

    def retranslateUi(self, IntroView):
        IntroView.setWindowTitle(_translate("IntroView", "Intro", None))
        self.label_itu.setText(_translate("IntroView", "<html><head/><body><p>Istanbul Technical University</p></body></html>", None))
        self.label_faculty.setText(_translate("IntroView", "<html><head/><body><p>Faculty of Mines</p></body></html>", None))
        self.label_department.setText(_translate("IntroView", "<html><head/><body><p><span style=\" font-weight:600;\">Department of Geophysics Engineering</span></p></body></html>", None))
        self.label_gunal.setText(_translate("IntroView", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Günal Baki</span><br/>gunalbaki@gmail.com</p></body></html>", None))
        self.label_evrim.setText(_translate("IntroView", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Evrim Çabuk</span><br/>evrimcabuk@gmail.com</p></body></html>", None))
        self.label_year.setText(_translate("IntroView", "2015", None))
        self.label_appname.setText(_translate("IntroView", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">VLF 1500</span></p></body></html>", None))

import resources_rc
