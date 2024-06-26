# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 347)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bigtitle = QtWidgets.QLabel(Form)
        self.bigtitle.setGeometry(QtCore.QRect(0, 50, 431, 61))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bigtitle.setFont(font)
        self.bigtitle.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(180, 217, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 20pt \"华文隶书\";")
        self.bigtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.bigtitle.setWordWrap(False)
        self.bigtitle.setObjectName("bigtitle")
        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(3, 1, 411, 341))
        self.background.setStyleSheet("background-image: url(:/media/img/wechat_20240525190026(3).jpg);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.knowBUPT = QtWidgets.QCommandLinkButton(Form)
        self.knowBUPT.setGeometry(QtCore.QRect(240, 290, 161, 41))
        self.knowBUPT.setStyleSheet("font: 8pt \"微软雅黑\";\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.knowBUPT.setObjectName("knowBUPT")
        self.login_pushButton = QtWidgets.QPushButton(Form)
        self.login_pushButton.setGeometry(QtCore.QRect(220, 240, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.login_pushButton.setFont(font)
        self.login_pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(180, 217, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.login_pushButton.setObjectName("login_pushButton")
        self.register_pushButton = QtWidgets.QPushButton(Form)
        self.register_pushButton.setGeometry(QtCore.QRect(120, 240, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.register_pushButton.setFont(font)
        self.register_pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(180, 217, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.register_pushButton.setObjectName("register_pushButton")
        self.password_lineEdit = QtWidgets.QLineEdit(Form)
        self.password_lineEdit.setGeometry(QtCore.QRect(161, 202, 135, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.password_picture = QtWidgets.QLabel(Form)
        self.password_picture.setGeometry(QtCore.QRect(120, 200, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.password_picture.setFont(font)
        self.password_picture.setStyleSheet("border-image: url(:/media/img/28573c3e022bf47.jpg);")
        self.password_picture.setObjectName("password_picture")
        self.username_picture = QtWidgets.QLabel(Form)
        self.username_picture.setGeometry(QtCore.QRect(120, 150, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.username_picture.setFont(font)
        self.username_picture.setStyleSheet("border-image: url(:/media/img/user.jpg);")
        self.username_picture.setObjectName("username_picture")
        self.username_lineEdit = QtWidgets.QLineEdit(Form)
        self.username_lineEdit.setGeometry(QtCore.QRect(160, 150, 139, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.background.raise_()
        self.bigtitle.raise_()
        self.knowBUPT.raise_()
        self.login_pushButton.raise_()
        self.register_pushButton.raise_()
        self.password_lineEdit.raise_()
        self.password_picture.raise_()
        self.username_picture.raise_()
        self.username_lineEdit.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bigtitle.setText(_translate("Form", "北邮图书管理系统"))
        self.knowBUPT.setText(_translate("Form", "了解更多北邮图书馆"))
        self.login_pushButton.setText(_translate("Form", "登录"))
        self.register_pushButton.setText(_translate("Form", "注册"))
        self.password_lineEdit.setText(_translate("Form", "admin"))
        self.password_picture.setText(_translate("Form", "——"))
        self.username_picture.setText(_translate("Form", "——"))
        self.username_lineEdit.setText(_translate("Form", "admin"))
import ui.pictures
