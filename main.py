from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRect, QPoint
from PyQt5 import uic
import sys
import random


class CircleGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.w, self.h = self.width(), self.height()
        self.qp = QPainter()
        self.can_draw = False
        self.pushButton.clicked.connect(self.generate)

    def paintEvent(self, event):
        if self.can_draw:
            self.qp.begin(self)
            self.qp.setBrush(QColor(255, 255, 0))
            self.drawCircle()
            self.qp.end()

    def drawCircle(self):
        r_proj = int(random.randint(10, 200) / (2 ** 0.5))

        x, y = (random.randint(0, self.w - r_proj), random.randint(0, self.h - r_proj))

        self.qp.drawEllipse(QRect(QPoint(x, y), QPoint(x + r_proj, y + r_proj)))

    def generate(self):
        self.can_draw = True
        self.update()



def main():
    app = QApplication(sys.argv)
    window = CircleGenerator()
    window.show()
    sys.exit(app.exec())

main()