# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'twts.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TwTSDialog(object):
    def setupUi(self, TwTSDialog):
        if not TwTSDialog.objectName():
            TwTSDialog.setObjectName(u"TwTSDialog")
        TwTSDialog.resize(454, 270)
        self.verticalLayout = QVBoxLayout(TwTSDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(TwTSDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.lbQrCode = QLabel(TwTSDialog)
        self.lbQrCode.setObjectName(u"lbQrCode")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbQrCode.sizePolicy().hasHeightForWidth())
        self.lbQrCode.setSizePolicy(sizePolicy)
        self.lbQrCode.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbQrCode)


        self.retranslateUi(TwTSDialog)

        QMetaObject.connectSlotsByName(TwTSDialog)
    # setupUi

    def retranslateUi(self, TwTSDialog):
        TwTSDialog.setWindowTitle(QCoreApplication.translate("TwTSDialog", u"Transwarp Support", None))
        self.label.setText(QCoreApplication.translate("TwTSDialog", u"If you have any questions about Transwarp productions, \n"
"plase scan the QRCode below with mobile WeChat.", None))
        self.lbQrCode.setText("")
    # retranslateUi

