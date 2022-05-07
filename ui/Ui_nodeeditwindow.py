# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nodeeditwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NodeEditWindow(object):
    def setupUi(self, NodeEditWindow):
        if not NodeEditWindow.objectName():
            NodeEditWindow.setObjectName(u"NodeEditWindow")
        NodeEditWindow.resize(334, 550)
        self.centralwidget = QWidget(NodeEditWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.editAlias = QLineEdit(self.centralwidget)
        self.editAlias.setObjectName(u"editAlias")

        self.verticalLayout.addWidget(self.editAlias)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.editIP = QLineEdit(self.centralwidget)
        self.editIP.setObjectName(u"editIP")

        self.verticalLayout.addWidget(self.editIP)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.editPort = QLineEdit(self.centralwidget)
        self.editPort.setObjectName(u"editPort")

        self.verticalLayout.addWidget(self.editPort)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.editUser = QLineEdit(self.centralwidget)
        self.editUser.setObjectName(u"editUser")

        self.verticalLayout.addWidget(self.editUser)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.editPasswd = QLineEdit(self.centralwidget)
        self.editPasswd.setObjectName(u"editPasswd")
        self.editPasswd.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.editPasswd)

        self.chkIsMgr = QCheckBox(self.centralwidget)
        self.chkIsMgr.setObjectName(u"chkIsMgr")

        self.verticalLayout.addWidget(self.chkIsMgr)

        self.chkIsHttps = QCheckBox(self.centralwidget)
        self.chkIsHttps.setObjectName(u"chkIsHttps")

        self.verticalLayout.addWidget(self.chkIsHttps)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.editMgrPort = QLineEdit(self.centralwidget)
        self.editMgrPort.setObjectName(u"editMgrPort")

        self.verticalLayout.addWidget(self.editMgrPort)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.editMgrPasswd = QLineEdit(self.centralwidget)
        self.editMgrPasswd.setObjectName(u"editMgrPasswd")
        self.editMgrPasswd.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.editMgrPasswd)

        self.btnTest = QPushButton(self.centralwidget)
        self.btnTest.setObjectName(u"btnTest")

        self.horizontalLayout_2.addWidget(self.btnTest)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnSave = QPushButton(self.centralwidget)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout.addWidget(self.btnSave)


        self.verticalLayout.addLayout(self.horizontalLayout)

        NodeEditWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(NodeEditWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 334, 26))
        NodeEditWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(NodeEditWindow)
        self.statusbar.setObjectName(u"statusbar")
        NodeEditWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NodeEditWindow)

        QMetaObject.connectSlotsByName(NodeEditWindow)
    # setupUi

    def retranslateUi(self, NodeEditWindow):
        NodeEditWindow.setWindowTitle(QCoreApplication.translate("NodeEditWindow", u"Node Editor", None))
        self.label.setText(QCoreApplication.translate("NodeEditWindow", u"Node name/alias", None))
        self.label_2.setText(QCoreApplication.translate("NodeEditWindow", u"IP address", None))
        self.label_6.setText(QCoreApplication.translate("NodeEditWindow", u"Port", None))
        self.editPort.setText(QCoreApplication.translate("NodeEditWindow", u"22", None))
        self.label_7.setText(QCoreApplication.translate("NodeEditWindow", u"SSH user name (administrator privilege)", None))
        self.editUser.setText("")
        self.label_3.setText(QCoreApplication.translate("NodeEditWindow", u"Password of SSH user", None))
        self.chkIsMgr.setText(QCoreApplication.translate("NodeEditWindow", u"Is it an active Manager node?", None))
        self.chkIsHttps.setText(QCoreApplication.translate("NodeEditWindow", u"Is HTTPS enabled?", None))
        self.label_4.setText(QCoreApplication.translate("NodeEditWindow", u"Manager port", None))
        self.editMgrPort.setText(QCoreApplication.translate("NodeEditWindow", u"8180", None))
        self.label_5.setText(QCoreApplication.translate("NodeEditWindow", u"Password of Manager admin user", None))
        self.btnTest.setText(QCoreApplication.translate("NodeEditWindow", u"Test Connection", None))
        self.btnSave.setText(QCoreApplication.translate("NodeEditWindow", u"Save", None))
    # retranslateUi

