import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("main06.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.lotto)

    def lotto(self) :
        lotto = list(range(1, 45+1))
        
        for i in range(100) :
            rnd = int(random.random()*45)
        
            a = lotto[0]
            b = lotto[rnd]
        
            lotto[0] = b
            lotto[rnd] = a
        
        print(lotto[0],lotto[1],lotto[2],lotto[3],lotto[4],lotto[5])

        self.lbl1.setText(str(lotto[0]))
        self.lbl2.setText(str(lotto[1]))
        self.lbl3.setText(str(lotto[2]))
        self.lbl4.setText(str(lotto[3]))
        self.lbl5.setText(str(lotto[4]))
        self.lbl6.setText(str(lotto[5]))
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    