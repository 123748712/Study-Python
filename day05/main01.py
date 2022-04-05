# 파이썬 Designer
# button 클릭시 label 변경

import sys

form_class = uic.loadUiType("main01.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb.clicked.connect(self.clicked)

    def clicked(self):
        self.lbl.setText("Good Evening")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()