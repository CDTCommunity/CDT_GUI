# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mappingeditwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ServiceMappingEditorDialog(object):
    def setupUi(self, ServiceMappingEditorDialog):
        if not ServiceMappingEditorDialog.objectName():
            ServiceMappingEditorDialog.setObjectName(u"ServiceMappingEditorDialog")
        ServiceMappingEditorDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(ServiceMappingEditorDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(ServiceMappingEditorDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cbOrgName = QComboBox(ServiceMappingEditorDialog)
        self.cbOrgName.setObjectName(u"cbOrgName")

        self.horizontalLayout.addWidget(self.cbOrgName)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(ServiceMappingEditorDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.editMappedName = QLineEdit(ServiceMappingEditorDialog)
        self.editMappedName.setObjectName(u"editMappedName")

        self.verticalLayout.addWidget(self.editMappedName)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.btnSave = QPushButton(ServiceMappingEditorDialog)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(ServiceMappingEditorDialog)

        QMetaObject.connectSlotsByName(ServiceMappingEditorDialog)
    # setupUi

    def retranslateUi(self, ServiceMappingEditorDialog):
        ServiceMappingEditorDialog.setWindowTitle(QCoreApplication.translate("ServiceMappingEditorDialog", u"Service Mapping Editor", None))
        self.label.setText(QCoreApplication.translate("ServiceMappingEditorDialog", u"Service original name", None))
        self.label_2.setText(QCoreApplication.translate("ServiceMappingEditorDialog", u"Service mapped name", None))
        self.btnSave.setText(QCoreApplication.translate("ServiceMappingEditorDialog", u"Save", None))
    # retranslateUi

