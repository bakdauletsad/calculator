import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic

class UI(QWidget):
    def __init__(self):
        self.start()
        self.set()
    
    def start(self):
        self.ui = uic.loadUi('calendar.ui')
        self.ui.show()

    def set(self):
        self.ui.pb1.clicked.connect( lambda:self.click(num=1))
        self.ui.pb2.clicked.connect( lambda:self.click(num=2))
        self.ui.pb3.clicked.connect( lambda:self.click(num=3))
        self.ui.pb4.clicked.connect( lambda:self.click(num=4))
        self.ui.pb5.clicked.connect( lambda:self.click(num=5))
        self.ui.pb6.clicked.connect( lambda:self.click(num=6))
        self.ui.pb7.clicked.connect( lambda:self.click(num=7))
        self.ui.pb8.clicked.connect( lambda:self.click(num=8))
        self.ui.pb9.clicked.connect( lambda:self.click(num=9))
        self.ui.pb0.clicked.connect( lambda:self.click(num=0))

        self.ui.minus.clicked.connect( lambda:self.click('-'))
        self.ui.plus.clicked.connect( lambda:self.click('+'))
        self.ui.x.clicked.connect(lambda:self.delete())
        self.ui.dot.clicked.connect(lambda:self.click('.'))
        self.ui.mul.clicked.connect(lambda:self.click('*'))
        self.ui.div.clicked.connect(lambda:self.click('/'))
        self.ui.equal.clicked.connect(lambda:self.ravno())
    
    def delete(self):
        x = self.ui.label.text()
        x = x[:-1]
        self.ui.label.setText(x)

    def click(self, num=0):
        self.display(text=num)
    
    def ravno(self):
        x = self.ui.label.text()
        x = eval(x)
        self.ui.label.setText(str(x))


        

    def display(self, text='0'):
        old_text = self.ui.label.text()
        if old_text == '0':
            old_text = ''
        new_text = old_text+str(text)
        self.ui.label.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    uiWindow = UI()
    app.exec_()