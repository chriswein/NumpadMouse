import sys
from settings import settings

from PyQt5 import QtCore, Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def calculate_quadrants(width, height, left=0, top=0):
    return [
        [left+width//6, top+height//6],
        [left+3*width//6, top+height//6],
        [left+5*width//6, top+height//6],
        [left+width//6, top+3*height//6],
        [left+3*width//6, top+3*height//6],
        [left+5*width//6, top+3*height//6],
        [left+width//6, top+5*height//6],
        [left+3*width//6, top+5*height//6],
        [left+5*width//6, top+5*height//6],
    ]


mapping = { 1: 6, 2: 7, 3: 8, 4: 3, 5: 4, 6: 5, 7: 0, 8: 1, 9: 2}

inv_map = {v: k for k, v in mapping.items()}



class DesktopOverlay(QMainWindow):
    def __init__(self, screen):
        QMainWindow.__init__(self)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
        )
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
                QtCore.QSize(screen.size().width(), screen.size().height()),
                QtWidgets.qApp.desktop().availableGeometry()
            ))

        self.quadrants = calculate_quadrants(
            screen.size().width(), screen.size().height(), 0, 0)

    # def mousePressEvent(self, event):
    #     QtWidgets.qApp.quit()

    def setQuadrants(self, currentQuadrants):
        self.quadrants = currentQuadrants
        self.update()
        pass

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        try:
            if(self.quadrants != None):
                for i, quadrant in enumerate(self.quadrants):
                    qp.fillRect(quadrant[0], quadrant[1], 22, 22, QColor(
                        settings["color"][0], settings["color"][1], settings["color"][2], 
                        150))
                    qp.setPen(QColor(255, 255, 255))
                    qp.setFont(QFont('Decorative', 12))
                    qp.drawText(quadrant[0], quadrant[1]+30, str(inv_map[i]))
            else:
                qp.setPen(QColor(168, 34, 3))
                qp.setFont(QFont('Decorative', 10))
                qp.fillRect(0, 0, 50, 50, QColor(168, 34, 34, 255))
                qp.drawText(event.rect(), QtCore.Qt.AlignCenter, "Hallo Welt")
        except Exception as e:
            print(e)
        qp.end()


