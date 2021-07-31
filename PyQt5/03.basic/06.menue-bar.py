## Ex 3-6. 메뉴바 만들기.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        exitAction = QAction(QIcon('sorce/exit.png'), 'exit', self)     # 아이콘과 exit라는 라벨을 가진 하나의 action 생성
        exitAction.setShortcut('Ctrl+Q')                                # 단축키 지정
        exitAction.setStatusTip('Exit application')                     # 마우스 올렸을때 상태바에 출력됨
        exitAction.triggered.connect(qApp.quit)                         # 동작지정(종료)

        self.statusBar()                                                # 상태창 생성

        menubar = self.menuBar()                                        # 메뉴바 생성
        menubar.setNativeMenuBar(False)                                 # ???
        fileMenu = menubar.addMenu('&File')                             # 메뉴바에 File 메뉴 생성 &는 단축키로 ALT + F 가 file메뉴를 여는 단축키이다.
        fileMenu.addAction(exitAction)                                  # file 메뉴에 action 붙이기

        self.setWindowTitle("menubar")
        self.setGeometry(300, 300, 300, 200)
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())