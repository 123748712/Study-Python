import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("main08.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.playGame)
        self.leMine.returnPressed.connect(self.playGame) # enter key event

    def playGame(self) :
        mine = self.leMine.text()
        com = "";
        
        rnd = random.randrange(3)
        print(rnd)
        if rnd < 1 :
            com = "가위"
        elif rnd < 2 :
            com = "바위"
        else :
            com = "보"
        
        print(com)

        self.leCom.setText(com)
        
        
        if mine == com :
            self.leResult.setText("비김")
        elif (mine == "가위" and com == "보") or (mine == "바위" and com == "가위") or (mine == "보" and com == "바위") :
            self.leResult.setText("승리")
        else :
            self.leResult.setText("패배")
            
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()