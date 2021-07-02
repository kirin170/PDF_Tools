# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'split_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Split_Dialog(object):
    def setupUi(self, Split_Dialog):
        Split_Dialog.setObjectName("Split_Dialog")
        Split_Dialog.resize(611, 331)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Split_Dialog.sizePolicy().hasHeightForWidth())
        Split_Dialog.setSizePolicy(sizePolicy)
        Split_Dialog.setMinimumSize(QtCore.QSize(611, 331))
        Split_Dialog.setMaximumSize(QtCore.QSize(611, 331))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        Split_Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/PDF拆分.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Split_Dialog.setWindowIcon(icon)
        Split_Dialog.setWindowOpacity(1.5)
        Split_Dialog.setStyleSheet("font: 12pt \"微软雅黑\";")
        Split_Dialog.setSizeGripEnabled(False)
        self.lineEdit_openPDF = QtWidgets.QLineEdit(Split_Dialog)
        self.lineEdit_openPDF.setGeometry(QtCore.QRect(40, 20, 440, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_openPDF.sizePolicy().hasHeightForWidth())
        self.lineEdit_openPDF.setSizePolicy(sizePolicy)
        self.lineEdit_openPDF.setMinimumSize(QtCore.QSize(440, 30))
        self.lineEdit_openPDF.setMaximumSize(QtCore.QSize(440, 30))
        self.lineEdit_openPDF.setObjectName("lineEdit_openPDF")
        self.pushButton_openPDF = QtWidgets.QPushButton(Split_Dialog)
        self.pushButton_openPDF.setGeometry(QtCore.QRect(500, 20, 75, 30))
        self.pushButton_openPDF.setObjectName("pushButton_openPDF")
        self.groupBox_mode = QtWidgets.QGroupBox(Split_Dialog)
        self.groupBox_mode.setGeometry(QtCore.QRect(40, 70, 440, 150))
        self.groupBox_mode.setMinimumSize(QtCore.QSize(440, 150))
        self.groupBox_mode.setMaximumSize(QtCore.QSize(440, 150))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_mode.setFont(font)
        self.groupBox_mode.setObjectName("groupBox_mode")
        self.radioButton_everypage = QtWidgets.QRadioButton(self.groupBox_mode)
        self.radioButton_everypage.setGeometry(QtCore.QRect(20, 30, 130, 30))
        self.radioButton_everypage.setObjectName("radioButton_everypage")
        self.spinBox_page = QtWidgets.QSpinBox(self.groupBox_mode)
        self.spinBox_page.setGeometry(QtCore.QRect(70, 40, 35, 20))
        self.spinBox_page.setObjectName("spinBox_page")
        self.radioButton_selfSet = QtWidgets.QRadioButton(self.groupBox_mode)
        self.radioButton_selfSet.setGeometry(QtCore.QRect(20, 80, 411, 21))
        self.radioButton_selfSet.setObjectName("radioButton_selfSet")
        self.lineEdit_pageSet = QtWidgets.QLineEdit(self.groupBox_mode)
        self.lineEdit_pageSet.setGeometry(QtCore.QRect(20, 109, 401, 31))
        self.lineEdit_pageSet.setObjectName("lineEdit_pageSet")
        self.pushButton_start = QtWidgets.QPushButton(Split_Dialog)
        self.pushButton_start.setGeometry(QtCore.QRect(500, 80, 75, 141))
        self.pushButton_start.setObjectName("pushButton_start")
        self.label_tip = QtWidgets.QLabel(Split_Dialog)
        self.label_tip.setGeometry(QtCore.QRect(40, 250, 521, 51))
        self.label_tip.setObjectName("label_tip")

        self.retranslateUi(Split_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Split_Dialog)

    def retranslateUi(self, Split_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Split_Dialog.setWindowTitle(_translate("Split_Dialog", "PDF拆分"))
        Split_Dialog.setToolTip(_translate("Split_Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_openPDF.setText(_translate("Split_Dialog", "打开PDF"))
        self.groupBox_mode.setTitle(_translate("Split_Dialog", "拆分模式"))
        self.radioButton_everypage.setText(_translate("Split_Dialog", "每               页"))
        self.radioButton_selfSet.setText(_translate("Split_Dialog", "自定义提取为单个或多个pdf文件(1,3,5-7,8-10,10-81)"))
        self.pushButton_start.setText(_translate("Split_Dialog", "开始"))
        self.label_tip.setText(_translate("Split_Dialog", "1.打开pdf文件  2.设置拆分模式  3.点击开始"))
import img_rc