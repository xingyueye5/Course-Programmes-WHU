# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Client.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Client(object):
    def setupUi(self, MainWindow_Client):
        MainWindow_Client.setObjectName("MainWindow_Client")
        MainWindow_Client.resize(801, 610)
        self.centralwidget_client = QtWidgets.QWidget(MainWindow_Client)
        self.centralwidget_client.setObjectName("centralwidget_client")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget_client)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_path = QtWidgets.QLineEdit(self.centralwidget_client)
        self.lineEdit_path.setText("")
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.verticalLayout.addWidget(self.lineEdit_path)
        self.listWidget_files = QtWidgets.QListWidget(self.centralwidget_client)
        self.listWidget_files.setMidLineWidth(0)
        self.listWidget_files.setIconSize(QtCore.QSize(2, 2))
        self.listWidget_files.setObjectName("listWidget_files")
        self.verticalLayout.addWidget(self.listWidget_files)
        self.textBrowser_history = QtWidgets.QTextBrowser(self.centralwidget_client)
        self.textBrowser_history.setDocumentTitle("")
        self.textBrowser_history.setObjectName("textBrowser_history")
        self.verticalLayout.addWidget(self.textBrowser_history)
        self.lineEdit_cmd = QtWidgets.QLineEdit(self.centralwidget_client)
        self.lineEdit_cmd.setText("")
        self.lineEdit_cmd.setObjectName("lineEdit_cmd")
        self.verticalLayout.addWidget(self.lineEdit_cmd)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow_Client.setCentralWidget(self.centralwidget_client)
        self.menubar_client = QtWidgets.QMenuBar(MainWindow_Client)
        self.menubar_client.setGeometry(QtCore.QRect(0, 0, 801, 26))
        self.menubar_client.setObjectName("menubar_client")
        self.menu_system = QtWidgets.QMenu(self.menubar_client)
        self.menu_system.setObjectName("menu_system")
        self.menu_file = QtWidgets.QMenu(self.menubar_client)
        self.menu_file.setObjectName("menu_file")
        MainWindow_Client.setMenuBar(self.menubar_client)
        self.statusbar_client = QtWidgets.QStatusBar(MainWindow_Client)
        self.statusbar_client.setObjectName("statusbar_client")
        MainWindow_Client.setStatusBar(self.statusbar_client)
        self.action_logout = QtWidgets.QAction(MainWindow_Client)
        self.action_logout.setObjectName("action_logout")
        self.action_quit = QtWidgets.QAction(MainWindow_Client)
        self.action_quit.setObjectName("action_quit")
        self.action_exit = QtWidgets.QAction(MainWindow_Client)
        self.action_exit.setObjectName("action_exit")
        self.action_upload = QtWidgets.QAction(MainWindow_Client)
        self.action_upload.setObjectName("action_upload")
        self.action_download = QtWidgets.QAction(MainWindow_Client)
        self.action_download.setObjectName("action_download")
        self.action_delete = QtWidgets.QAction(MainWindow_Client)
        self.action_delete.setObjectName("action_delete")
        self.menu_system.addAction(self.action_quit)
        self.menu_system.addAction(self.action_exit)
        self.menu_file.addAction(self.action_upload)
        self.menu_file.addAction(self.action_download)
        self.menu_file.addAction(self.action_delete)
        self.menubar_client.addAction(self.menu_system.menuAction())
        self.menubar_client.addAction(self.menu_file.menuAction())

        self.retranslateUi(MainWindow_Client)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Client)

    def retranslateUi(self, MainWindow_Client):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Client.setWindowTitle(_translate("MainWindow_Client", "FTP客户端"))
        self.lineEdit_path.setPlaceholderText(_translate("MainWindow_Client", "当前文件路径"))
        self.textBrowser_history.setPlaceholderText(_translate("MainWindow_Client", "response结果(响应码，返回值）"))
        self.lineEdit_cmd.setPlaceholderText(_translate("MainWindow_Client", "命令行"))
        self.menu_system.setTitle(_translate("MainWindow_Client", "系统"))
        self.menu_file.setTitle(_translate("MainWindow_Client", "文件"))
        self.action_logout.setText(_translate("MainWindow_Client", "注销"))
        self.action_quit.setText(_translate("MainWindow_Client", "断连"))
        self.action_exit.setText(_translate("MainWindow_Client", "退出"))
        self.action_upload.setText(_translate("MainWindow_Client", "上传"))
        self.action_download.setText(_translate("MainWindow_Client", "下载"))
        self.action_delete.setText(_translate("MainWindow_Client", "删除"))
