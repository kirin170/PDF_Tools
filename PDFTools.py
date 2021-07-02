# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PDFTools.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(607, 625)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        Dialog.setFont(font)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/PDF.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(229, 255, 251);")
        self.pushButton_split = QtWidgets.QPushButton(Dialog)
        self.pushButton_split.setGeometry(QtCore.QRect(50, 40, 130, 140))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_split.setFont(font)
        self.pushButton_split.setToolTip("")
        self.pushButton_split.setWhatsThis("")
        self.pushButton_split.setStyleSheet("background-image: url(:/img/PDF拆分.png);")
        self.pushButton_split.setText("")
        self.pushButton_split.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_split.setObjectName("pushButton_split")
        self.pushButton_merge = QtWidgets.QPushButton(Dialog)
        self.pushButton_merge.setGeometry(QtCore.QRect(240, 40, 130, 140))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_merge.setFont(font)
        self.pushButton_merge.setStyleSheet("background-image: url(:/img/PDF合并.png);")
        self.pushButton_merge.setText("")
        self.pushButton_merge.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_merge.setObjectName("pushButton_merge")
        self.pushButton_toWord = QtWidgets.QPushButton(Dialog)
        self.pushButton_toWord.setGeometry(QtCore.QRect(420, 430, 130, 140))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_toWord.setFont(font)
        self.pushButton_toWord.setStyleSheet("background-image: url(:/img/PDF转Word.png);")
        self.pushButton_toWord.setText("")
        self.pushButton_toWord.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_toWord.setObjectName("pushButton_toWord")
        self.pushButton_toExcel = QtWidgets.QPushButton(Dialog)
        self.pushButton_toExcel.setGeometry(QtCore.QRect(240, 430, 130, 140))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_toExcel.setFont(font)
        self.pushButton_toExcel.setStyleSheet("background-image: url(:/img/PDF转Excel.png);")
        self.pushButton_toExcel.setText("")
        self.pushButton_toExcel.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_toExcel.setObjectName("pushButton_toExcel")
        self.pushButton_toPicture = QtWidgets.QPushButton(Dialog)
        self.pushButton_toPicture.setGeometry(QtCore.QRect(420, 40, 130, 140))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_toPicture.setFont(font)
        self.pushButton_toPicture.setStyleSheet("background-image: url(:/img/PDF转图片.png);")
        self.pushButton_toPicture.setText("")
        self.pushButton_toPicture.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_toPicture.setObjectName("pushButton_toPicture")
        self.pushButton_getPicture = QtWidgets.QPushButton(Dialog)
        self.pushButton_getPicture.setGeometry(QtCore.QRect(50, 240, 130, 140))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_getPicture.setFont(font)
        self.pushButton_getPicture.setStyleSheet("background-image: url(:/img/PDF图片提取.png);")
        self.pushButton_getPicture.setText("")
        self.pushButton_getPicture.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_getPicture.setObjectName("pushButton_getPicture")
        self.pushButton_encryption = QtWidgets.QPushButton(Dialog)
        self.pushButton_encryption.setGeometry(QtCore.QRect(240, 240, 130, 140))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_encryption.setFont(font)
        self.pushButton_encryption.setStyleSheet("background-image: url(:/img/PDF加密.png);")
        self.pushButton_encryption.setText("")
        self.pushButton_encryption.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_encryption.setObjectName("pushButton_encryption")
        self.pushButton_addWatermark = QtWidgets.QPushButton(Dialog)
        self.pushButton_addWatermark.setGeometry(QtCore.QRect(50, 430, 130, 140))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_addWatermark.setFont(font)
        self.pushButton_addWatermark.setStyleSheet("background-image: url(:/img/PDF加水印.png);")
        self.pushButton_addWatermark.setText("")
        self.pushButton_addWatermark.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_addWatermark.setObjectName("pushButton_addWatermark")
        self.pushButton_decryption = QtWidgets.QPushButton(Dialog)
        self.pushButton_decryption.setGeometry(QtCore.QRect(420, 240, 130, 140))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_decryption.setFont(font)
        self.pushButton_decryption.setStyleSheet("background-image: url(:/img/PDF去密码.png);")
        self.pushButton_decryption.setText("")
        self.pushButton_decryption.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_decryption.setObjectName("pushButton_decryption")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PDF Tools"))
import img_rc
