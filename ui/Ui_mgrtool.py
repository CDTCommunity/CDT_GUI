# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mgrtool.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.lbUrl = QLabel(self.centralwidget)
        self.lbUrl.setObjectName(u"lbUrl")

        self.horizontalLayout.addWidget(self.lbUrl)

        self.btnCopyUrl = QPushButton(self.centralwidget)
        self.btnCopyUrl.setObjectName(u"btnCopyUrl")
        self.btnCopyUrl.setFont(font)

        self.horizontalLayout.addWidget(self.btnCopyUrl)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lbVersion = QLabel(self.centralwidget)
        self.lbVersion.setObjectName(u"lbVersion")

        self.horizontalLayout_2.addWidget(self.lbVersion)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lbHa = QLabel(self.centralwidget)
        self.lbHa.setObjectName(u"lbHa")

        self.horizontalLayout_2.addWidget(self.lbHa)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setFont(font)

        self.horizontalLayout_3.addWidget(self.btnStart)

        self.btnStop = QPushButton(self.centralwidget)
        self.btnStop.setObjectName(u"btnStop")
        self.btnStop.setFont(font)

        self.horizontalLayout_3.addWidget(self.btnStop)

        self.btnRestart = QPushButton(self.centralwidget)
        self.btnRestart.setObjectName(u"btnRestart")
        self.btnRestart.setFont(font)

        self.horizontalLayout_3.addWidget(self.btnRestart)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.btnAgentRestartAll = QPushButton(self.centralwidget)
        self.btnAgentRestartAll.setObjectName(u"btnAgentRestartAll")
        self.btnAgentRestartAll.setFont(font)

        self.horizontalLayout_4.addWidget(self.btnAgentRestartAll)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.btnChkStatus = QPushButton(self.centralwidget)
        self.btnChkStatus.setObjectName(u"btnChkStatus")
        self.btnChkStatus.setFont(font)

        self.horizontalLayout_5.addWidget(self.btnChkStatus)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.brStatus = QTextBrowser(self.centralwidget)
        self.brStatus.setObjectName(u"brStatus")

        self.verticalLayout.addWidget(self.brStatus)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Manager Toolkit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Access URL", None))
        self.lbUrl.setText(QCoreApplication.translate("MainWindow", u"Loading", None))
        self.btnCopyUrl.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.lbVersion.setText(QCoreApplication.translate("MainWindow", u"Loading", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"HA Mode", None))
        self.lbHa.setText(QCoreApplication.translate("MainWindow", u"Loading", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Actions", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btnStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btnRestart.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Agents", None))
        self.btnAgentRestartAll.setText(QCoreApplication.translate("MainWindow", u"Restart All", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.btnChkStatus.setText(QCoreApplication.translate("MainWindow", u"Check", None))
    # retranslateUi

