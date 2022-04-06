import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QIcon, QSize



# 타일 생성 및 클릭시 흰돌 타일 변환

form_class = uic.loadUiType("omok02.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
    
        # btn2 = QPushButton(self)
        # btn2.setIcon(QIcon('0.png'))
        # btn2.setGeometry(0, 0, 40, 40)
        # btn2.setIconSize(QSize(40, 40))
        #
        # btn3 = QPushButton(self)
        # btn3.setIcon(QIcon('0.png'))
        # btn3.setGeometry(40, 0, 40, 40)
        # btn3.setIconSize(QSize(40, 40))

        for i in range(10) :
            for j in range(10) :
                btn = QPushButton(self)
                btn.setIcon(QIcon('0.png'))
                btn.setGeometry(i*40, j*40, 40, 40)
                btn.setIconSize(QSize(40, 40))
                btn.clicked.connect(self.click)
        
        
    def click(self):
        self.sender().setIcon(QIcon('1.png'))
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    