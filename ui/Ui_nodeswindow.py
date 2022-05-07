# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nodeswindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NodesWindow(object):
    def setupUi(self, NodesWindow):
        if not NodesWindow.objectName():
            NodesWindow.setObjectName(u"NodesWindow")
        NodesWindow.resize(600, 400)
        self.centralwidget = QWidget(NodesWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 576, 288))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnAddMultiple = QPushButton(self.centralwidget)
        self.btnAddMultiple.setObjectName(u"btnAddMultiple")

        self.horizontalLayout.addWidget(self.btnAddMultiple)

        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName(u"btnAdd")

        self.horizontalLayout.addWidget(self.btnAdd)


        self.verticalLayout.addLayout(self.horizontalLayout)

        NodesWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(NodesWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 26))
        NodesWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(NodesWindow)
        self.statusbar.setObjectName(u"statusbar")
        NodesWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NodesWindow)

        QMetaObject.connectSlotsByName(NodesWindow)
    # setupUi

    def retranslateUi(self, NodesWindow):
        NodesWindow.setWindowTitle(QCoreApplication.translate("NodesWindow", u"Nodes", None))
        self.btnAddMultiple.setText(QCoreApplication.translate("NodesWindow", u"PushButton", None))
        self.btnAdd.setText(QCoreApplication.translate("NodesWindow", u"Add", None))
    # retranslateUi

