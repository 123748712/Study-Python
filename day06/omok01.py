import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QIcon



# button 오목 타일 설정 및 클릭시 백돌, 흰돌, 타일 이미지 변환

form_class = uic.loadUiType("omok01.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        self.cnt = 0;
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.clicked)
        
    def clicked(self):
        self.cnt += 1
        if self.cnt%3 == 1 :
            self.pb.setIcon(QIcon('1.png'))
        elif self.cnt%3 == 2 :
            self.pb.setIcon(QIcon('2.png'))
        elif self.cnt%3 == 0 :
            self.pb.setIcon(QIcon('0.png'))
            
        print(self.cnt)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    