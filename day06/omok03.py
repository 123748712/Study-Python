import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QIcon, QSize




# 2차원 배열 만들어 오목에 적용시키기

form_class = uic.loadUiType("omok03.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.flag_wb = True 
        self.flag_ing = True
        self.pb2D = []
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
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
                pb.setToolTip("{}.{}".format(i, j)) # 툴팁에 pb의 좌표를 넣어준다.
                pb.setIcon(QIcon('0.png'))
                pb.setGeometry(j*40, i*40, 40, 40)
                pb.setIconSize(QSize(40, 40))
                pb.clicked.connect(self.click)
                line.append(pb) # 배열안에 pb를 담아줌
            self.pb2D.append(line) # pb 10개가 담긴 배열을 다시 배열에 담아줌
        
        
        self.myrander()
        self.pbReset.clicked.connect(self.reset)
        
    def reset(self): # 리셋 버튼 클릭시 리셋되는 메소드
        for i in range(10) :
            for j in range(10) :
                self.arr2D[i][j] = 0
        
        self.myrander()
        self.flag_ing = True
        self.flag_wb = True
    
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
        if not self.flag_ing :
            return
        
        ij = self.sender().toolTip().split(".") # 툴팁 정보를 가져와 . 을 기준으로 나눈다.
        i = int(ij[0])
        j = int(ij[1])
        
        if self.arr2D[i][j] > 0 : # 0보다 크다면 배열에 돟이 놓아진 상태
            return                # 그 밑의 함수가 실행되지 않게 리턴
        
        stone = -1
        # print(i , j)
        # self.cnt += 1
        # if self.cnt%2 == 0 :
        #     self.arr2D[i][j] = 2
        # if self.cnt%2 == 1 :
        #     self.arr2D[i][j] = 1
        
        # if self.arr2D[i][j] == 0 :
        if self.flag_wb :
            self.arr2D[i][j] = 1
            stone = 1
        else :
            self.arr2D[i][j] = 2
            stone = 2
        
        # 좌표를 구분해야하기 때문에 파라미터에 i, j, 자기자신을 준다.
        up = self.checkUP(i, j, stone) # 돌읗 놓은 위치 기준, 위쪽에 있는 돌을 구하는 메소드
        dw = self.checkDW(i, j, stone) # 돌읗 놓은 위치 기준, 아래쪽에 있는 돌을 구하는 메소드
        ri = self.checkRI(i, j, stone) # 돌읗 놓은 위치 기준, 오른쪽에 있는 돌을 구하는 메소드
        le = self.checkLE(i, j, stone) # 돌읗 놓은 위치 기준, 왼쪽에 있는 돌을 구하는 메소드
        ul = self.checkUL(i, j, stone) # 돌읗 놓은 위치 기준, 위,왼쪽에 있는 돌을 구하는 메소드
        ur = self.checkUR(i, j, stone) # 돌읗 놓은 위치 기준, 위,오른쪽에 있는 돌을 구하는 메소드
        dl = self.checkDL(i, j, stone) # 돌읗 놓은 위치 기준, 아래,왼쪽에 있는 돌을 구하는 메소드
        dr = self.checkDR(i, j, stone) # 돌읗 놓은 위치 기준, 아래,오른쪽에 있는 돌을 구하는 메소드
        
        # 한줄에 놓아진 돌의 갯수
        d1 = up + dw + 1
        d2 = ri + le + 1
        d3 = ul + dr + 1
        d4 = dl + ur + 1
        
        
        self.myrander()

        if d1 == 5 or d2 == 5  or d3 == 5  or d4 == 5 :
            if self.flag_wb :
                QMessageBox.about(self, '결과', '백 승리')
            else : 
                QMessageBox.about(self, '결과', '흑 승리')
            self.flag_ing = False
        
        self.flag_wb = not self.flag_wb
            
            
    def checkUP(self, i, j, stone):
        ret = 0 # 연결되어 있는 돌의 갯수를 세는 변수
        try :
            while True :
                i -= 1 
                if i < 0 : # -1 이상이 되는 순간부터 음수 인덱스를 인식하는걸 방지
                    return ret 
                if j < 0 :
                    return ret   
                
                if self.arr2D[i][j] == stone :
                    ret += 1
                else :
                    return ret
        except :
            return ret
    
    def checkDW(self, i, j, stone):
        ret = 0 # 연결되어 있는 돌의 갯수를 세는 변수
        try :
            while True :
                i += 1 
                if i < 0 : # -1 이상이 되는 순간부터 음수 인덱스를 인식하는걸 방지
                    return ret
                if j < 0 :
                    return ret   
    
                if self.arr2D[i][j] == stone :
                    ret += 1
                else :
                    return ret
        except :
            return ret
    
    
    def checkRI(self, i, j, stone):
        ret = 0 # 연결되어 있는 돌의 갯수를 세는 변수
        try :
            while True :
                j += 1 
                if i < 0 : # -1 이상이 되는 순간부터 음수 인덱스를 인식하는걸 방지
                    return ret  
                if j < 0 :
                    return ret  
    
                if self.arr2D[i][j] == stone :
                    ret += 1
                else :
                    return ret
        except :
            return ret
    
    def checkLE(self, i, j, stone):
        ret = 0 # 연결되어 있는 돌의 갯수를 세는 변수
        try :
            while True :
                j -= 1 
                if i < 0 : # -1 이상이 되는 순간부터 음수 인덱스를 인식하는걸 방지
                    return ret  
                if j < 0 :
                    return ret  
    
                if self.arr2D[i][j] == stone :
                    ret += 1
                else :
                    return ret
        except :
            return ret
    
    def checkUL(self, i, j, stone):
        ret = 0 # 연결되어 있는 돌의 갯수를 세는 변수
        try :
            while True :
                i -= 1
                j -= 1 
                if i < 0 : # -1 이상이 되는 순간부터 음수 인덱스를 인식하는걸 방지
                    return ret  
                if j < 0 :
                    return ret  
    
                if self.arr2D[i][j] == stone :
                    ret += 1
                else :
                    return ret
        except :
            return ret

    def checkUR(self, i, j, stone):
        ret = 0 # 연결되어 있는 돌의 갯수를 세는 변수
        try :
            while True :
                i -= 1
                j += 1 
                if i < 0 : # -1 이상이 되는 순간부터 음수 인덱스를 인식하는걸 방지
                    return ret  
                if j < 0 :
                    return ret  
    
                if self.arr2D[i][j] == stone :
                    ret += 1
                else :
                    return ret
        except :
            return ret
    
    def checkDR(self, i, j, stone):
        ret = 0 # 연결되어 있는 돌의 갯수를 세는 변수
        try :
            while True :
                i += 1
                j += 1 
                if i < 0 : # -1 이상이 되는 순간부터 음수 인덱스를 인식하는걸 방지
                    return ret  
                if j < 0 :
                    return ret  
    
                if self.arr2D[i][j] == stone :
                    ret += 1
                else :
                    return ret
        except :
            return ret
    
    def checkDL(self, i, j, stone):
        ret = 0 # 연결되어 있는 돌의 갯수를 세는 변수
        try :
            while True :
                i += 1
                j -= 1 
                if i < 0 : # -1 이상이 되는 순간부터 음수 인덱스를 인식하는걸 방지
                    return ret  
                if j < 0 :
                    return ret  
    
                if self.arr2D[i][j] == stone :
                    ret += 1
                else :
                    return ret
        except :
            return ret
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    