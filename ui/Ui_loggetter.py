# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loggetter.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LogGetDialog(object):
    def setupUi(self, LogGetDialog):
        if not LogGetDialog.objectName():
            LogGetDialog.setObjectName(u"LogGetDialog")
        LogGetDialog.resize(500, 350)
        self.verticalLayout = QVBoxLayout(LogGetDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(LogGetDialog)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.lbSvc = QLabel(LogGetDialog)
        self.lbSvc.setObjectName(u"lbSvc")

        self.horizontalLayout.addWidget(self.lbSvc)

        self.label_3 = QLabel(LogGetDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)

        self.lbRole = QLabel(LogGetDialog)
        self.lbRole.setObjectName(u"lbRole")

        self.horizontalLayout.addWidget(self.lbRole)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(LogGetDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.cbNode = QComboBox(LogGetDialog)
        self.cbNode.setObjectName(u"cbNode")

        self.horizontalLayout_2.addWidget(self.cbNode)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(LogGetDialog)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.cbMode = QComboBox(LogGetDialog)
        self.cbMode.addItem("")
        self.cbMode.addItem("")
        self.cbMode.addItem("")
        self.cbMode.setObjectName(u"cbMode")

        self.horizontalLayout_3.addWidget(self.cbMode)

        self.label_5 = QLabel(LogGetDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.spnNum = QSpinBox(LogGetDialog)
        self.spnNum.setObjectName(u"spnNum")
        self.spnNum.setMinimum(1)

        self.horizontalLayout_3.addWidget(self.spnNum)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(LogGetDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.dtStart = QDateTimeEdit(LogGetDialog)
        self.dtStart.setObjectName(u"dtStart")

        self.horizontalLayout_4.addWidget(self.dtStart)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(LogGetDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.dtEnd = QDateTimeEdit(LogGetDialog)
        self.dtEnd.setObjectName(u"dtEnd")

        self.horizontalLayout_5.addWidget(self.dtEnd)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(LogGetDialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.lbTargetDir = QLabel(LogGetDialog)
        self.lbTargetDir.setObjectName(u"lbTargetDir")

        self.horizontalLayout_6.addWidget(self.lbTargetDir)

        self.btnBrowse = QPushButton(LogGetDialog)
        self.btnBrowse.setObjectName(u"btnBrowse")
        self.btnBrowse.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.btnBrowse)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.chkMultiThread = QCheckBox(LogGetDialog)
        self.chkMultiThread.setObjectName(u"chkMultiThread")
        self.chkMultiThread.setChecked(False)

        self.horizontalLayout_7.addWidget(self.chkMultiThread)

        self.btnGet = QPushButton(LogGetDialog)
        self.btnGet.setObjectName(u"btnGet")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.btnGet.setFont(font1)

        self.horizontalLayout_7.addWidget(self.btnGet)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.lbState = QLabel(LogGetDialog)
        self.lbState.setObjectName(u"lbState")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        self.lbState.setFont(font2)
        self.lbState.setStyleSheet(u"color: rgb(255, 0, 0)")

        self.verticalLayout.addWidget(self.lbState)


        self.retranslateUi(LogGetDialog)

        QMetaObject.connectSlotsByName(LogGetDialog)
    # setupUi

    def retranslateUi(self, LogGetDialog):
        LogGetDialog.setWindowTitle(QCoreApplication.translate("LogGetDialog", u"Log Getter", None))
        self.label_2.setText(QCoreApplication.translate("LogGetDialog", u"Service", None))
        self.lbSvc.setText(QCoreApplication.translate("LogGetDialog", u"text", None))
        self.label_3.setText(QCoreApplication.translate("LogGetDialog", u"Role", None))
        self.lbRole.setText(QCoreApplication.translate("LogGetDialog", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("LogGetDialog", u"Node", None))
        self.label.setText(QCoreApplication.translate("LogGetDialog", u"Mode", None))
        self.cbMode.setItemText(0, QCoreApplication.translate("LogGetDialog", u"Simple", None))
        self.cbMode.setItemText(1, QCoreApplication.translate("LogGetDialog", u"by Number", None))
        self.cbMode.setItemText(2, QCoreApplication.translate("LogGetDialog", u"by Date & Time", None))

        self.label_5.setText(QCoreApplication.translate("LogGetDialog", u"Number", None))
        self.label_6.setText(QCoreApplication.translate("LogGetDialog", u"Start", None))
        self.dtStart.setDisplayFormat(QCoreApplication.translate("LogGetDialog", u"yyyy-MM-dd HH:mm:ss", None))
        self.label_7.setText(QCoreApplication.translate("LogGetDialog", u"End", None))
        self.dtEnd.setDisplayFormat(QCoreApplication.translate("LogGetDialog", u"yyyy-MM-dd HH:mm:ss", None))
        self.label_8.setText(QCoreApplication.translate("LogGetDialog", u"Target Directory", None))
        self.lbTargetDir.setText(QCoreApplication.translate("LogGetDialog", u"TextLabel", None))
        self.btnBrowse.setText(QCoreApplication.translate("LogGetDialog", u"Browse", None))
        self.chkMultiThread.setText(QCoreApplication.translate("LogGetDialog", u"Multithreading", None))
        self.btnGet.setText(QCoreApplication.translate("LogGetDialog", u"Get", None))
        self.lbState.setText(QCoreApplication.translate("LogGetDialog", u"TextLabel", None))
    # retranslateUi

