import datetime
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *


class SecondsAlive(QWidget):
    def __init__(self, year, month, day, hour = 0, minute = 0):
        QWidget.__init__(self)
        
        self.setFixedSize(950, 570)
        self.setWindowTitle('Seconds alive')
        self.setStyleSheet('background-color:rgb(255,255,255)')
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        
        self.birthday = datetime.datetime(year, month, day, hour = hour, minute = minute)

        dif = datetime.datetime.now() - self.birthday

        dif_secs = dif.days * 3600 * 24 + dif.seconds
        #print(dif_secs)
        
        self.timelbl = QLabel(str(dif_secs), self)
        self.timelbl.setFont(QtGui.QFont('Arial', 80))
        self.timelbl.resize(self.size())
        self.timelbl.setAlignment(QtCore.Qt.AlignCenter)
        self.timelbl.move(0, self.timelbl.pos().y() - 40)


        self.text1 = QLabel('You\'ve been alive for', self)
        self.text1.setFont(QtGui.QFont('Arial', 30))
        self.text1.resize(self.size().width(), 40)
        self.text1.move(0, 100)
        self.text1.setAlignment(QtCore.Qt.AlignCenter)
        
        self.text2 = QLabel('seconds', self)
        self.text2.setFont(QtGui.QFont('Arial', 30))
        self.text2.resize(self.size().width(), 40)
        self.text2.move(0, 340)
        self.text2.setAlignment(QtCore.Qt.AlignCenter)
        
        self.timer = QtCore.QTimer(parent = self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update)
        self.timer.start()

        yearlist = []
        for year in range(2017, 1920, -1):
            yearlist.append(str(year))

        daylist = []
        for day in range(1, 32):
            daylist.append(str(day))

        hourlist = []
        for hour in range(24):
            hourlist.append(str(hour))

        minlist = []
        for minute in range(60):
            minlist.append(str(minute))
                

        monthlist = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        yearl = QLabel('Year:', self)
        yearl.move(50, 450)
        yearl.setFont(QtGui.QFont('Arial', 10))

        ml = QLabel('Month:', self)
        ml.move(200, 450)
        ml.setFont(QtGui.QFont('Arial', 10))

        dayl = QLabel('Day:', self)
        dayl.move(350, 450)
        dayl.setFont(QtGui.QFont('Arial', 10))

        hourl = QLabel('Hour:', self)
        hourl.move(500, 450)
        hourl.setFont(QtGui.QFont('Arial', 10))

        minl = QLabel('Minute:', self)
        minl.move(650, 450)
        minl.setFont(QtGui.QFont('Arial', 10))

        self.okbtn = QPushButton('OK', self)
        self.okbtn.setGeometry(800, 480, 100, 40)
        self.okbtn.clicked.connect(self.newDate)

        self.yearchoice = QComboBox(self)
        self.yearchoice.setGeometry(50,480, 100, 40)
        self.yearchoice.addItems(yearlist)
        self.yearchoice.setCurrentIndex(14)

        self.monthchoice = QComboBox(self)
        self.monthchoice.setGeometry(200,480, 100, 40)
        self.monthchoice.addItems(monthlist)
        self.monthchoice.setCurrentIndex(2)
        self.monthchoice.currentIndexChanged.connect(self.monthChange)
        
        self.daychoice = QComboBox(self)
        self.daychoice.setGeometry(350,480, 100, 40)
        self.daychoice.addItems(daylist)
        self.daychoice.setCurrentIndex(21)
        
        self.hourchoice = QComboBox(self)
        self.hourchoice.setGeometry(500,480, 100, 40)
        self.hourchoice.addItems(hourlist)
        self.hourchoice.setCurrentIndex(6)
        
        self.minchoice = QComboBox(self)
        self.minchoice.setGeometry(650,480, 100, 40)
        self.minchoice.addItems(minlist)
        self.minchoice.setCurrentIndex(0)
        
        self.monthdays = {'January' : 31, 'February' : 28, 'March' : 31, 'April' : 30, 'May' : 31, 'June' : 30, 'July' : 31,
                          'August' : 31, 'September' : 30, 'October' : 31, 'November' : 30, 'December' : 31}

        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                       'August', 'September', 'October', 'November', 'December']

    def newDate(self):
        year = int(self.yearchoice.currentText())
        month = self.months.index(self.monthchoice.currentText()) + 1
        day = int(self.daychoice.currentText())
        hour = int(self.hourchoice.currentText())
        minute = int(self.minchoice.currentText())

        print('New Date:', year, month, day, hour, minute)
        
        birthday = datetime.datetime(year, month, day, hour = hour, minute = minute)

        
        dif = datetime.datetime.now() - birthday
        dif_secs = dif.days * 3600 * 24 + dif.seconds

        self.timelbl.setText(str(dif_secs))
        
        
    def monthChange(self):

        #for item in range(31):
        #    try:
        #        self.daychoice.removeItem(item)
        #    except IndexError:
        #        break
        
        self.daychoice.clear()
        for item in range(1, self.monthdays[self.monthchoice.currentText()] + 1):
            self.daychoice.addItem(str(item))
        
    def update(self):
        self.timelbl.setText(str(int(self.timelbl.text()) + 1))
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = SecondsAlive(2003, 3, 22, hour = 6, minute = 0)
    ex.show()
    sys.exit(app.exec_())
