import sys
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QTableWidgetItem
from merge_UI import Ui_Merge_QDialog
import sys
import fitz
1  # coding: utf-8
3  # Author：kirin丶7
4  # Date ：2021/6/11 9:25
5  # Tool ：PyCharm

class MergeForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Merge_QDialog()
        self.ui.setupUi(self)
        self.rowCount = 0 #当前文件个数
        self.currentRow = 0 #当前行

        self.ui.pushButton_w2_add.clicked.connect(self.w2_add)
        self.ui.pushButton_w2_remove.clicked.connect(self.w2_remove)
        self.ui.pushButton_w2_up.clicked.connect(self.w2_up)
        self.ui.pushButton_w2_down.clicked.connect(self.w2_down)
        self.ui.pushButton_w2_start.clicked.connect(self.w2_start)
        self.show()

    def w2_add(self):
        file_names = QFileDialog.getOpenFileNames(self,
                                                  'Add PDF',
                                                  "C:/Users/admin/Desktop/",
                                                  "PDF Files (*.pdf)")
        file_names = file_names[0]
        #
        self.rowCount = len(file_names) + self.rowCount
        self.ui.tableWidget_w2_fileList.setRowCount(self.rowCount)

        for name in file_names:
            print(name)
            doc = fitz.open(name)

            page = doc.pageCount
            self.ui.tableWidget_w2_fileList.setItem(self.currentRow, 0, QTableWidgetItem(name))
            self.ui.tableWidget_w2_fileList.setItem(self.currentRow, 1, QTableWidgetItem(str(page))) #页数

            print(self.currentRow)
            self.currentRow = self.currentRow + 1

    def w2_remove(self):
        current_rows = self.ui.tableWidget_w2_fileList.selectedItems()
        self.currentRow = self.rowCount = self.rowCount - len(current_rows)
        for i in current_rows:
            self.ui.tableWidget_w2_fileList.removeRow(i.row())

    def w2_up(self):
        pass

    def w2_down(self):
        pass

    def w2_start(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MergeForm()
    w.show()
    sys.exit(app.exec_())
