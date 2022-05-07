# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
        self.actionVersion = QAction(MainWindow)
        self.actionVersion.setObjectName(u"actionVersion")
        self.actionInitialize_configs = QAction(MainWindow)
        self.actionInitialize_configs.setObjectName(u"actionInitialize_configs")
        self.actionNode_configurate = QAction(MainWindow)
        self.actionNode_configurate.setObjectName(u"actionNode_configurate")
        self.actionService_configurate = QAction(MainWindow)
        self.actionService_configurate.setObjectName(u"actionService_configurate")
        self.actionTranswarp_Support = QAction(MainWindow)
        self.actionTranswarp_Support.setObjectName(u"actionTranswarp_Support")
        self.actionEnglish = QAction(MainWindow)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionChinese = QAction(MainWindow)
        self.actionChinese.setObjectName(u"actionChinese")
        self.actionJapanese = QAction(MainWindow)
        self.actionJapanese.setObjectName(u"actionJapanese")
        self.actionKorean = QAction(MainWindow)
        self.actionKorean.setObjectName(u"actionKorean")
        self.actionAbout_TDH_Collector = QAction(MainWindow)
        self.actionAbout_TDH_Collector.setObjectName(u"actionAbout_TDH_Collector")
        self.actionUpdate = QAction(MainWindow)
        self.actionUpdate.setObjectName(u"actionUpdate")
        self.actionTranswarp_Knowledge_Base = QAction(MainWindow)
        self.actionTranswarp_Knowledge_Base.setObjectName(u"actionTranswarp_Knowledge_Base")
        self.actionTranswarp_Docs = QAction(MainWindow)
        self.actionTranswarp_Docs.setObjectName(u"actionTranswarp_Docs")
        self.actionTranswarp_Class_Online = QAction(MainWindow)
        self.actionTranswarp_Class_Online.setObjectName(u"actionTranswarp_Class_Online")
        self.actionTDH_Collector_Manual = QAction(MainWindow)
        self.actionTDH_Collector_Manual.setObjectName(u"actionTDH_Collector_Manual")
        self.actionExport_metainfo = QAction(MainWindow)
        self.actionExport_metainfo.setObjectName(u"actionExport_metainfo")
        self.actionUpdate_Log = QAction(MainWindow)
        self.actionUpdate_Log.setObjectName(u"actionUpdate_Log")
        self.actionGUI_Log = QAction(MainWindow)
        self.actionGUI_Log.setObjectName(u"actionGUI_Log")
        self.actionCore_Log = QAction(MainWindow)
        self.actionCore_Log.setObjectName(u"actionCore_Log")
        self.actionChineseTraditional = QAction(MainWindow)
        self.actionChineseTraditional.setObjectName(u"actionChineseTraditional")
        self.actionBrowse = QAction(MainWindow)
        self.actionBrowse.setObjectName(u"actionBrowse")
        self.actionReset = QAction(MainWindow)
        self.actionReset.setObjectName(u"actionReset")
        self.actionQuick_Start = QAction(MainWindow)
        self.actionQuick_Start.setObjectName(u"actionQuick_Start")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.lbNodeNum = QLabel(self.groupBox)
        self.lbNodeNum.setObjectName(u"lbNodeNum")

        self.horizontalLayout.addWidget(self.lbNodeNum)

        self.btnNode = QPushButton(self.groupBox)
        self.btnNode.setObjectName(u"btnNode")
        self.btnNode.setFont(font1)

        self.horizontalLayout.addWidget(self.btnNode)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout.addWidget(self.label_3)

        self.lbSvcNum = QLabel(self.groupBox)
        self.lbSvcNum.setObjectName(u"lbSvcNum")

        self.horizontalLayout.addWidget(self.lbSvcNum)

        self.btnSvc = QPushButton(self.groupBox)
        self.btnSvc.setObjectName(u"btnSvc")
        self.btnSvc.setFont(font1)

        self.horizontalLayout.addWidget(self.btnSvc)

        self.btnMap = QPushButton(self.groupBox)
        self.btnMap.setObjectName(u"btnMap")
        self.btnMap.setFont(font1)

        self.horizontalLayout.addWidget(self.btnMap)

        self.horizontalSpacer = QSpacerItem(304, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnClstrEnvInfo = QPushButton(self.groupBox)
        self.btnClstrEnvInfo.setObjectName(u"btnClstrEnvInfo")
        self.btnClstrEnvInfo.setFont(font1)

        self.horizontalLayout.addWidget(self.btnClstrEnvInfo)


        self.verticalLayout.addWidget(self.groupBox)

        self.lbTipInfo = QLabel(self.centralwidget)
        self.lbTipInfo.setObjectName(u"lbTipInfo")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.lbTipInfo.setFont(font2)
        self.lbTipInfo.setStyleSheet(u"QLabel\n"
"{\n"
"color: rgb(255, 0, 0);\n"
"}")

        self.verticalLayout.addWidget(self.lbTipInfo)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font3 = QFont()
        font3.setPointSize(10)
        self.groupBox_2.setFont(font3)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)
        self.label_2.setFont(font4)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.cbQueryMode = QComboBox(self.groupBox_2)
        self.cbQueryMode.addItem("")
        self.cbQueryMode.addItem("")
        self.cbQueryMode.addItem("")
        self.cbQueryMode.setObjectName(u"cbQueryMode")

        self.horizontalLayout_3.addWidget(self.cbQueryMode)

        self.editKeyWord = QLineEdit(self.groupBox_2)
        self.editKeyWord.setObjectName(u"editKeyWord")

        self.horizontalLayout_3.addWidget(self.editKeyWord)

        self.btnQuery = QPushButton(self.groupBox_2)
        self.btnQuery.setObjectName(u"btnQuery")
        self.btnQuery.setFont(font4)

        self.horizontalLayout_3.addWidget(self.btnQuery)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.lbCheckListStatus = QLabel(self.groupBox_2)
        self.lbCheckListStatus.setObjectName(u"lbCheckListStatus")
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.lbCheckListStatus.setFont(font5)
        self.lbCheckListStatus.setStyleSheet(u"QLabel{\n"
"	color: red;\n"
"}")

        self.verticalLayout_2.addWidget(self.lbCheckListStatus)

        self.scrollArea = QScrollArea(self.groupBox_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 752, 276))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font6 = QFont()
        font6.setFamily(u"Arial Black")
        font6.setPointSize(8)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_4.setFont(font6)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lbWorkspace = QLabel(self.centralwidget)
        self.lbWorkspace.setObjectName(u"lbWorkspace")
        font7 = QFont()
        font7.setFamily(u"Arial")
        font7.setPointSize(8)
        self.lbWorkspace.setFont(font7)

        self.horizontalLayout_2.addWidget(self.lbWorkspace)

        self.btnReset = QPushButton(self.centralwidget)
        self.btnReset.setObjectName(u"btnReset")
        self.btnReset.setFont(font7)

        self.horizontalLayout_2.addWidget(self.btnReset)

        self.btnBrowse = QPushButton(self.centralwidget)
        self.btnBrowse.setObjectName(u"btnBrowse")
        self.btnBrowse.setFont(font7)

        self.horizontalLayout_2.addWidget(self.btnBrowse)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menuConfig = QMenu(self.menubar)
        self.menuConfig.setObjectName(u"menuConfig")
        self.menuLanguage = QMenu(self.menuConfig)
        self.menuLanguage.setObjectName(u"menuLanguage")
        self.menuWorkspace = QMenu(self.menuConfig)
        self.menuWorkspace.setObjectName(u"menuWorkspace")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuDeBug = QMenu(self.menuHelp)
        self.menuDeBug.setObjectName(u"menuDeBug")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuConfig.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuConfig.addAction(self.actionNode_configurate)
        self.menuConfig.addAction(self.actionService_configurate)
        self.menuConfig.addSeparator()
        self.menuConfig.addAction(self.actionInitialize_configs)
        self.menuConfig.addSeparator()
        self.menuConfig.addAction(self.actionExport_metainfo)
        self.menuConfig.addSeparator()
        self.menuConfig.addAction(self.menuWorkspace.menuAction())
        self.menuConfig.addSeparator()
        self.menuConfig.addAction(self.menuLanguage.menuAction())
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionChinese)
        self.menuLanguage.addAction(self.actionChineseTraditional)
        self.menuLanguage.addAction(self.actionJapanese)
        self.menuLanguage.addAction(self.actionKorean)
        self.menuWorkspace.addAction(self.actionBrowse)
        self.menuWorkspace.addAction(self.actionReset)
        self.menuHelp.addAction(self.actionAbout_TDH_Collector)
        self.menuHelp.addAction(self.actionUpdate)
        self.menuHelp.addAction(self.actionUpdate_Log)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionQuick_Start)
        self.menuHelp.addAction(self.actionTDH_Collector_Manual)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionTranswarp_Support)
        self.menuHelp.addAction(self.actionTranswarp_Knowledge_Base)
        self.menuHelp.addAction(self.actionTranswarp_Docs)
        self.menuHelp.addAction(self.actionTranswarp_Class_Online)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.menuDeBug.menuAction())
        self.menuDeBug.addAction(self.actionGUI_Log)
        self.menuDeBug.addAction(self.actionCore_Log)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Transwarp Case Diagnostic Tool (CDT)", None))
        self.actionVersion.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.actionInitialize_configs.setText(QCoreApplication.translate("MainWindow", u"Initialize configs", None))
        self.actionNode_configurate.setText(QCoreApplication.translate("MainWindow", u"Node configurate", None))
        self.actionService_configurate.setText(QCoreApplication.translate("MainWindow", u"Service configurate", None))
        self.actionTranswarp_Support.setText(QCoreApplication.translate("MainWindow", u"Transwarp Support", None))
        self.actionEnglish.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.actionChinese.setText(QCoreApplication.translate("MainWindow", u"\u7b80\u4f53\u4e2d\u6587", None))
        self.actionJapanese.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u672c\u8a9e", None))
        self.actionKorean.setText(QCoreApplication.translate("MainWindow", u"\ud55c\uad6d\uc5b4", None))
        self.actionAbout_TDH_Collector.setText(QCoreApplication.translate("MainWindow", u"About TDH Collector", None))
        self.actionUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.actionTranswarp_Knowledge_Base.setText(QCoreApplication.translate("MainWindow", u"Transwarp Knowledge Base", None))
        self.actionTranswarp_Docs.setText(QCoreApplication.translate("MainWindow", u"Transwarp Docs", None))
        self.actionTranswarp_Class_Online.setText(QCoreApplication.translate("MainWindow", u"Transwarp Class Online", None))
        self.actionTDH_Collector_Manual.setText(QCoreApplication.translate("MainWindow", u"TDH Collector Desktop Manual", None))
        self.actionExport_metainfo.setText(QCoreApplication.translate("MainWindow", u"Export metainfo", None))
        self.actionUpdate_Log.setText(QCoreApplication.translate("MainWindow", u"Update Log", None))
        self.actionGUI_Log.setText(QCoreApplication.translate("MainWindow", u"GUI Log", None))
        self.actionCore_Log.setText(QCoreApplication.translate("MainWindow", u"Core Log", None))
        self.actionChineseTraditional.setText(QCoreApplication.translate("MainWindow", u"\u7e41\u9ad4\u4e2d\u6587", None))
        self.actionBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.actionReset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.actionQuick_Start.setText(QCoreApplication.translate("MainWindow", u"Quick Start", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Cluster Information", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nodes:", None))
        self.lbNodeNum.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnNode.setText(QCoreApplication.translate("MainWindow", u"  Detail  ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Services:", None))
        self.lbSvcNum.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnSvc.setText(QCoreApplication.translate("MainWindow", u"  Detail  ", None))
        self.btnMap.setText(QCoreApplication.translate("MainWindow", u"Mapping", None))
        self.btnClstrEnvInfo.setText(QCoreApplication.translate("MainWindow", u"Cluster Environment Info", None))
        self.lbTipInfo.setText(QCoreApplication.translate("MainWindow", u"text", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Services", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.cbQueryMode.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.cbQueryMode.setItemText(1, QCoreApplication.translate("MainWindow", u"Services", None))
        self.cbQueryMode.setItemText(2, QCoreApplication.translate("MainWindow", u"Roles", None))

        self.btnQuery.setText(QCoreApplication.translate("MainWindow", u"  Query  ", None))
        self.lbCheckListStatus.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Output Path", None))
        self.lbWorkspace.setText(QCoreApplication.translate("MainWindow", u"somepath", None))
        self.btnReset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btnBrowse.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.menuConfig.setTitle(QCoreApplication.translate("MainWindow", u"Config", None))
        self.menuLanguage.setTitle(QCoreApplication.translate("MainWindow", u"Language", None))
        self.menuWorkspace.setTitle(QCoreApplication.translate("MainWindow", u"Workspace", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuDeBug.setTitle(QCoreApplication.translate("MainWindow", u"Debug", None))
    # retranslateUi

