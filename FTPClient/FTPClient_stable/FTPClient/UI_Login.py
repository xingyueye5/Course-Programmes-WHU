# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget_login(object):
    def setupUi(self, widget_login):
        widget_login.setObjectName("widget_login")
        widget_login.resize(291, 161)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget_login.sizePolicy().hasHeightForWidth())
        widget_login.setSizePolicy(sizePolicy)
        widget_login.setMinimumSize(QtCore.QSize(0, 0))
        widget_login.setMaximumSize(QtCore.QSize(1024, 1024))
        self.formLayoutWidget = QtWidgets.QWidget(widget_login)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 291, 112))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_lineEdit = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_lineEdit.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_lineEdit.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_lineEdit.setContentsMargins(10, 10, 10, 10)
        self.formLayout_lineEdit.setHorizontalSpacing(11)
        self.formLayout_lineEdit.setVerticalSpacing(20)
        self.formLayout_lineEdit.setObjectName("formLayout_lineEdit")
        self.label_user = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_user.setObjectName("label_user")
        self.formLayout_lineEdit.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_user)
        self.lineEdit_user = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.formLayout_lineEdit.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_user)
        self.label_pwd = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_pwd.setObjectName("label_pwd")
        self.formLayout_lineEdit.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_pwd)
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.formLayout_lineEdit.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_pwd)
        self.horizontalLayoutWidget = QtWidgets.QWidget(widget_login)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 110, 291, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_pushButton = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_pushButton.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_pushButton.setSpacing(9)
        self.horizontalLayout_pushButton.setObjectName("horizontalLayout_pushButton")
        self.pushButton_login = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout_pushButton.addWidget(self.pushButton_login)
        self.pushButton_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_pushButton.addWidget(self.pushButton_cancel)

        self.retranslateUi(widget_login)
        QtCore.QMetaObject.connectSlotsByName(widget_login)

    def retranslateUi(self, widget_login):
        _translate = QtCore.QCoreApplication.translate
        widget_login.setWindowTitle(_translate("widget_login", "登录"))
        self.label_user.setText(_translate("widget_login", "用户名："))
        self.label_pwd.setText(_translate("widget_login", "密码："))
        self.pushButton_login.setText(_translate("widget_login", "登录"))
        self.pushButton_cancel.setText(_translate("widget_login", "取消"))
