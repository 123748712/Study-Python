import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("main07.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.starDraw)

    def starDraw(self) :
        first = int(self.le1.text())
        last =  int(self.le2.text())
        txt = ""
        
        for i in range(first, last+1) :
            for j in range(first) :
                txt += "*"
            txt += "\n"
            first += 1
        
        # print(txt)
    #     for i in range(first, last+1) :
    #         txt += self.draw(i)
    #
        self.te.setText(txt)
    #
    # def draw(self, cnt):
    #     ret = ""
    #     for i in range(cnt) :
    #         ret += "*"
    #     ret += "\n"
    #     return ret
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    