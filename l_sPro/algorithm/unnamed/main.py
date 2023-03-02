import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_choose import Ui_Dialog

class mywindow(QtWidgets.QWidget,Ui_Dialog):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
