# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'multinodeeditwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MultiNodeEditWindow(object):
    def setupUi(self, MultiNodeEditWindow):
        if not MultiNodeEditWindow.objectName():
            MultiNodeEditWindow.setObjectName(u"MultiNodeEditWindow")
        MultiNodeEditWindow.resize(800, 600)
        self.centralwidget = QWidget(MultiNodeEditWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnNew = QPushButton(self.centralwidget)
        self.btnNew.setObjectName(u"btnNew")

        self.horizontalLayout.addWidget(self.btnNew)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 776, 436))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnSave = QPushButton(self.centralwidget)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lbStatement = QLabel(self.centralwidget)
        self.lbStatement.setObjectName(u"lbStatement")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        self.lbStatement.setFont(font)
        self.lbStatement.setStyleSheet(u"QLabel{\n"
"	color: red;\n"
"}")

        self.verticalLayout.addWidget(self.lbStatement)

        MultiNodeEditWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MultiNodeEditWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MultiNodeEditWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MultiNodeEditWindow)
        self.statusbar.setObjectName(u"statusbar")
        MultiNodeEditWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MultiNodeEditWindow)

        QMetaObject.connectSlotsByName(MultiNodeEditWindow)
    # setupUi

    def retranslateUi(self, MultiNodeEditWindow):
        MultiNodeEditWindow.setWindowTitle(QCoreApplication.translate("MultiNodeEditWindow", u"Multiple Node Editor", None))
        self.btnNew.setText(QCoreApplication.translate("MultiNodeEditWindow", u"New", None))
        self.btnSave.setText(QCoreApplication.translate("MultiNodeEditWindow", u"Save", None))
        self.lbStatement.setText(QCoreApplication.translate("MultiNodeEditWindow", u"TextLabel", None))
    # retranslateUi

