# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'jvmgetter.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_JVMInfoGetterDialog(object):
    def setupUi(self, JVMInfoGetterDialog):
        if not JVMInfoGetterDialog.objectName():
            JVMInfoGetterDialog.setObjectName(u"JVMInfoGetterDialog")
        JVMInfoGetterDialog.resize(500, 260)
        self.verticalLayout = QVBoxLayout(JVMInfoGetterDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(JVMInfoGetterDialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.chkJstack = QCheckBox(JVMInfoGetterDialog)
        self.chkJstack.setObjectName(u"chkJstack")
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.chkJstack.setFont(font1)
        self.chkJstack.setChecked(True)

        self.horizontalLayout.addWidget(self.chkJstack)

        self.chkJmap = QCheckBox(JVMInfoGetterDialog)
        self.chkJmap.setObjectName(u"chkJmap")
        self.chkJmap.setFont(font1)
        self.chkJmap.setChecked(True)

        self.horizontalLayout.addWidget(self.chkJmap)

        self.chkJstat = QCheckBox(JVMInfoGetterDialog)
        self.chkJstat.setObjectName(u"chkJstat")
        self.chkJstat.setFont(font1)

        self.horizontalLayout.addWidget(self.chkJstat)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(JVMInfoGetterDialog)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"QLabel{\n"
"    color: red;\n"
"}")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(JVMInfoGetterDialog)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(10)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color: red;\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(JVMInfoGetterDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"QLabel{\n"
"	color: red;\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.btnGet = QPushButton(JVMInfoGetterDialog)
        self.btnGet.setObjectName(u"btnGet")

        self.horizontalLayout_5.addWidget(self.btnGet)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(JVMInfoGetterDialog)

        QMetaObject.connectSlotsByName(JVMInfoGetterDialog)
    # setupUi

    def retranslateUi(self, JVMInfoGetterDialog):
        JVMInfoGetterDialog.setWindowTitle(QCoreApplication.translate("JVMInfoGetterDialog", u"JVM Info Getter", None))
        self.label.setText(QCoreApplication.translate("JVMInfoGetterDialog", u"What kind of JVM information do you want to collect?", None))
        self.chkJstack.setText(QCoreApplication.translate("JVMInfoGetterDialog", u"JSTACK", None))
        self.chkJmap.setText(QCoreApplication.translate("JVMInfoGetterDialog", u"JMAP", None))
        self.chkJstat.setText(QCoreApplication.translate("JVMInfoGetterDialog", u"JSTAT", None))
        self.label_2.setText(QCoreApplication.translate("JVMInfoGetterDialog", u"WARNING", None))
        self.label_3.setText(QCoreApplication.translate("JVMInfoGetterDialog", u"JMAP maybe cause a full GC;", None))
        self.label_4.setText(QCoreApplication.translate("JVMInfoGetterDialog", u"JSTAT will take much time to collect.", None))
        self.btnGet.setText(QCoreApplication.translate("JVMInfoGetterDialog", u"GET", None))
    # retranslateUi

