1  # coding: utf-8
3  # Author：kirin丶7
4  # Date ：2021/6/10 9:20
5  # Tool ：PyCharm
import ctypes
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PDFTools import Ui_Dialog
from callSplit import SplitForm
from callMerge import MergeForm
# from QCandyUi.CandyWindow import colorful
# @colorful('blueGreen')
class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_split.clicked.connect(self.split_Window)
        self.ui.pushButton_merge.clicked.connect(self.merge_Window)


    def split_Window(self):
        """
        拆分PDF
        :return:
        """
        self.w1 = SplitForm()
        self.w1.show()
    def merge_Window(self):
        """
        合并PDF
        :return:
        """
        self.w2 = MergeForm()
        self.w2.show()
    def toPicture_Window(self):
        """
        PDF转图片
        :return:
        """
        pass
    def getPicture_Window(self):
        pass

    def encryption_Window(self):
        pass

    def decryption_Window(self):
        pass

    def addWatermark_Window(self):
        pass

    def toExcel_Window(self):
        pass

    def toWord_Window(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
