import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("main05.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.googoodan)

    def googoodan(self) :
        dan = int(self.le.text())
        txt = ""
        
        for i in range(1, 9+1) :
            txt += "{} * {} = {}\n".format(dan, i, dan*i)
        
        self.te.setText(txt)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    