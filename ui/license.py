# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/ecabuk/Projects/vlf/ui/license.ui'
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

class Ui_LicenseView(object):
    def setupUi(self, LicenseView):
        LicenseView.setObjectName(_fromUtf8("LicenseView"))
        LicenseView.resize(800, 480)
        LicenseView.setMaximumSize(QtCore.QSize(5000, 5000))
        LicenseView.setAutoFillBackground(True)
        self.verticalLayoutWidget = QtGui.QWidget(LicenseView)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 461))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.license_txt_small = QtGui.QLabel(self.verticalLayoutWidget)
        self.license_txt_small.setTextFormat(QtCore.Qt.RichText)
        self.license_txt_small.setAlignment(QtCore.Qt.AlignCenter)
        self.license_txt_small.setWordWrap(True)
        self.license_txt_small.setObjectName(_fromUtf8("license_txt_small"))
        self.verticalLayout.addWidget(self.license_txt_small)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.img_cc = QtGui.QLabel(self.verticalLayoutWidget)
        self.img_cc.setText(_fromUtf8(""))
        self.img_cc.setPixmap(QtGui.QPixmap(_fromUtf8(":/cc/assets/cc/cc.svg")))
        self.img_cc.setAlignment(QtCore.Qt.AlignCenter)
        self.img_cc.setObjectName(_fromUtf8("img_cc"))
        self.horizontalLayout.addWidget(self.img_cc)
        self.img_by = QtGui.QLabel(self.verticalLayoutWidget)
        self.img_by.setText(_fromUtf8(""))
        self.img_by.setPixmap(QtGui.QPixmap(_fromUtf8(":/cc/assets/cc/by.svg")))
        self.img_by.setAlignment(QtCore.Qt.AlignCenter)
        self.img_by.setObjectName(_fromUtf8("img_by"))
        self.horizontalLayout.addWidget(self.img_by)
        self.img_nc = QtGui.QLabel(self.verticalLayoutWidget)
        self.img_nc.setText(_fromUtf8(""))
        self.img_nc.setPixmap(QtGui.QPixmap(_fromUtf8(":/cc/assets/cc/nc.svg")))
        self.img_nc.setAlignment(QtCore.Qt.AlignCenter)
        self.img_nc.setObjectName(_fromUtf8("img_nc"))
        self.horizontalLayout.addWidget(self.img_nc)
        self.img_sa = QtGui.QLabel(self.verticalLayoutWidget)
        self.img_sa.setText(_fromUtf8(""))
        self.img_sa.setPixmap(QtGui.QPixmap(_fromUtf8(":/cc/assets/cc/sa.svg")))
        self.img_sa.setAlignment(QtCore.Qt.AlignCenter)
        self.img_sa.setObjectName(_fromUtf8("img_sa"))
        self.horizontalLayout.addWidget(self.img_sa)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.license_txt = QtGui.QTextBrowser(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("PT Mono"))
        self.license_txt.setFont(font)
        self.license_txt.setStyleSheet(_fromUtf8("QScrollBar:vertical { width: 30px; }"))
        self.license_txt.setObjectName(_fromUtf8("license_txt"))
        self.verticalLayout.addWidget(self.license_txt)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.button_close = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.button_close.setFont(font)
        self.button_close.setObjectName(_fromUtf8("button_close"))
        self.horizontalLayout_2.addWidget(self.button_close)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(LicenseView)
        QtCore.QMetaObject.connectSlotsByName(LicenseView)

    def retranslateUi(self, LicenseView):
        LicenseView.setWindowTitle(_translate("LicenseView", "License", None))
        self.license_txt_small.setText(_translate("LicenseView", "<html><head/><body><p>This work is licensed under the <span style=\" font-weight:600;\">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</span>.</p></body></html>", None))
        self.license_txt.setHtml(_translate("LicenseView", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PT Mono\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.button_close.setText(_translate("LicenseView", "Close", None))

import resources_rc
