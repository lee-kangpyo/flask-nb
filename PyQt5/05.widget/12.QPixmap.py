'''
    QPixmap은 이미지를 다룰 때 사용되는 위젯입니다.
    지원하는 파일 형식은 아래와 같습니다. 어떤 이미지 형식은 '읽기'만 가능합니다.

    지원 형색 : BMP(R/W) GIF(R) JPG(R/W) JPEG(R/W) PNG(R/W) PBM(R) PGM(R) PPM(R/W) XBM(R/W) XPM(R/W)

'''

## Ex 5-12. QPixmap.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('../03.basic/sorce/edit.png')

        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)
        lbl_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        lbl_size.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_img)
        vbox.addWidget(lbl_size)
        self.setLayout(vbox)

        self.setWindowTitle('QPixmap')
        self.move(300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())