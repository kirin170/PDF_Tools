
from split_UI import Ui_Split_Dialog

1  # coding: utf-8
3  # Author：kirin丶7
4  # Date ：2021/6/10 10:38
5  # Tool ：PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from split_UI import Ui_Split_Dialog
from splitFunctions import split_pdf_same_page, split_pdf_custom_page

# from QCandyUi.CandyWindow import colorful
# @colorful('blueGreen')
class SplitForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Split_Dialog()
        self.ui.setupUi(self)
        self.pathStr = "" #文件路径
        self.splitMode = 0  #初始化拆分模式 0 = invalid, 1 is splitSame, 2 is splitCustom
        self.PageSame = 0
        self.PageStr = ""
        self.tipStr = ""  #label_tip

        self.ui.pushButton_openPDF.clicked.connect(self.openPDF)
        self.ui.radioButton_everypage.toggled.connect(self.splitSame)
        self.ui.radioButton_selfSet.toggled.connect(self.splitCustom)
        self.ui.spinBox_page.editingFinished.connect(self.changePageSame)
        self.ui.lineEdit_pageSet.textChanged.connect(self.changePageStr)
        self.ui.pushButton_start.clicked.connect(self.startSplit)
        self.show()

    def openPDF(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File', 'C:/Users/admin/Desktop', "PDF Files(*.pdf)")  #打开pdf文件
        self.ui.lineEdit_openPDF.setText(file_name[0])
        self.pathStr = file_name[0]

    def splitSame(self):
        """
        分割相同的页数
        """
        self.splitMode = 1
        self.ui.spinBox_page.setReadOnly(False) #读写
        self.ui.lineEdit_pageSet.setReadOnly(True)#只读

    def splitCustom(self):
        """
        自定义分割页数
        """
        self.splitMode = 2
        self.ui.spinBox_page.setReadOnly(True)
        self.ui.lineEdit_pageSet.setReadOnly(False)

    def changePageSame(self):
        self.PageSame = int(self.ui.spinBox_page.text())

    def changePageStr(self):
        self.pageStr = self.ui.lineEdit_pageSet.text()
        self.ui.label_tip.setText(self.pageStr)

    def startSplit(self):
        if self.splitMode == 0 or self.pathStr ==' ':
            self.tipStr = "未添加pdf文件 或 未设置拆分模式 ! "
        elif self.splitMode == 1:
            self.tipStr = split_pdf_same_page(self.pathStr, self.PageSame)
        elif self.splitMode == 2:
            self.tipStr = split_pdf_custom_page(self.pathStr, self.pageStr)
        else:
            pass
        self.ui.label_tip.setText(self.tipStr)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SplitForm()
    w.show()
    sys.exit(app.exec_())

