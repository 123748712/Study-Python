import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QIcon, QSize



# 2차원 배열 만들어 오목에 적용시키기

form_class = uic.loadUiType("omok03ver2.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb2D = []
        self.arr2D = [
            [0,0,0,1,0, 0,0,1,0,0],
            [0,0,0,2,0, 0,0,0,2,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],

            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
        ]
    

        for i in range(10) :
            line = [] # 2차원 배열을 만들 배열 생성
            for j in range(10) :
                pb = QPushButton(self)
                pb.setIcon(QIcon('0.png'))
                pb.setGeometry(j*40, i*40, 40, 40)
                pb.setIconSize(QSize(40, 40))
                pb.clicked.connect(self.click)
                line.append(pb) # 배열안에 pb를 담아줌
            self.pb2D.append(line) # pb 10개가 담긴 배열을 다시 배열에 담아줌
        
        
        self.myrander()
        
    
    def myrander(self):
        for i in range(10) :
            for j in range(10) :
                if self.arr2D[i][j] == 0 :
                      self.pb2D[i][j].setIcon(QIcon('0.png'))
                if self.arr2D[i][j] == 1 :
                      self.pb2D[i][j].setIcon(QIcon('1.png'))
                if self.arr2D[i][j] == 2 :
                      self.pb2D[i][j].setIcon(QIcon('2.png'))
                
        
        
    def click(self):
        
        # print(self.sender().geometry().x() / 40)
        # print(self.sender().geometry().y() / 40)
        i = int(self.sender().geometry().x() / 40)
        j = int(self.sender().geometry().y() / 40)
        
        
        self.arr2D[j][i] = 1
        # self.sender().setIcon(QIcon('1.png'))
        # self.arr2Ds
        self.myrander()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    