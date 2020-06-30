#必须加入的
import sys


from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

# 读取excel 生成二维lists
lists = xlsxOpenpyxl.read_excel_xlsx('../test4.xlsx', 'Sheet1')
print(lists)
