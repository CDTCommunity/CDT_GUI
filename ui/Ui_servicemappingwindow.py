# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'servicemappingwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ServiceMappingWindow(object):
    def setupUi(self, ServiceMappingWindow):
        if not ServiceMappingWindow.objectName():
            ServiceMappingWindow.setObjectName(u"ServiceMappingWindow")
        ServiceMappingWindow.resize(600, 500)
        self.centralwidget = QWidget(ServiceMappingWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName(u"btnAdd")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(16)
        self.btnAdd.setFont(font)

        self.horizontalLayout.addWidget(self.btnAdd)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 576, 333))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lbDescription = QLabel(self.centralwidget)
        self.lbDescription.setObjectName(u"lbDescription")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(14)
        self.lbDescription.setFont(font1)
        self.lbDescription.setStyleSheet(u"QLabel{\n"
"	color: red;\n"
"}")

        self.verticalLayout.addWidget(self.lbDescription)

        ServiceMappingWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ServiceMappingWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 26))
        ServiceMappingWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ServiceMappingWindow)
        self.statusbar.setObjectName(u"statusbar")
        ServiceMappingWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ServiceMappingWindow)

        QMetaObject.connectSlotsByName(ServiceMappingWindow)
    # setupUi

    def retranslateUi(self, ServiceMappingWindow):
        ServiceMappingWindow.setWindowTitle(QCoreApplication.translate("ServiceMappingWindow", u"Service Mapping", None))
        self.btnAdd.setText(QCoreApplication.translate("ServiceMappingWindow", u"Add a new mapping", None))
        self.lbDescription.setText(QCoreApplication.translate("ServiceMappingWindow", u"TextLabel", None))
    # retranslateUi

