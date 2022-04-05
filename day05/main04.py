import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("main04.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.playGame)
        self.leMine.returnPressed.connect(self.playGame) # enter key event

    def playGame(self) :
        mine = self.leMine.text()
        com = "";
        
        rnd = random.randrange(2)
        print(rnd)
        if rnd > 0 :
            com = "홀"
        else :
            com = "짝"

        self.leCom.setText(com)
        
        
        if mine == com :
            self.leResult.setText("승리")
        else :
            self.leResult.setText("패배")
            
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()