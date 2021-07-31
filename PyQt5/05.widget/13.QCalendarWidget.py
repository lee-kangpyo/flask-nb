'''
    QCalendarWidget을 이용해서 사용자가 날짜를 선택할 수 있도록 달력을 표시할 수 있습니다.
    달력은 월 단위로 표시되고, 처음 실행될 때 현재의 연도, 월, 날짜로 선택되어 있습니다.
    자세한 내용은 QCalendarWidget 공식 문서에서 확인할 수 있습니다.
'''

## Ex 5-13. QCalenderWidget.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''
            QCalenderWidget의 객체(cal)를 하나 만듭니다.
            setGridVisible(True)로 설정하면, 날짜 사이에 그리드가 표시됩니다.
            날짜를 클릭했을 때 showDate 메서드가 호출되도록 연결해줍니다.
        '''
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        '''
            selectedDate는 현재 선택된 날짜 정보를 갖고 있습니다. (디폴트는 현재 날짜)
            현재 날짜 정보를 라벨에 표시되도록 해줍니다.
        '''
        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        #수직 박스 레이아웃을 이용해서, 달력과 라벨을 수직으로 배치해줍니다.
        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    #showDate 메서드에서, 날짜를 클릭할 때마다 라벨 텍스트가 선택한 날짜(date.toString())로 표시되도록 합니다.
    def showDate(self, date):
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())