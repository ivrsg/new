import sys
from random import randint

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication


class DrowKrug(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.yellowkrug.clicked.connect(self.paintkrug)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            a = randint(20, 200)
            qp.setBrush(QColor(250, 250, 10))
            qp.drawEllipse(170 - a // 2, 170 - a // 2, a, a)
            qp.end()
        self.do_paint = False

    def paintkrug(self):
        self.do_paint = True
        self.update()


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrowKrug()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
