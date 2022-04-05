import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("main09.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.pb1.clicked.connect(self.numClick)
        self.pb2.clicked.connect(self.numClick)
        self.pb3.clicked.connect(self.numClick)
        self.pb4.clicked.connect(self.numClick)
        self.pb5.clicked.connect(self.numClick)
        self.pb6.clicked.connect(self.numClick)
        self.pb7.clicked.connect(self.numClick)
        self.pb8.clicked.connect(self.numClick)
        self.pb9.clicked.connect(self.numClick)
        self.pb0.clicked.connect(self.numClick)
        self.pbCall.clicked.connect(self.call)

    def numClick(self, cnt) :
        print(self.sender().text())
        self.le.setText(self.le.text() + self.sender().text())
        
    def call(self):
        QMessageBox.about(self, 'calling', self.le.text())
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    