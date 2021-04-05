from settings import settings
from helper import mapping, calculate_quadrants

from PyQt5 import QtCore, Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

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

    def setQuadrants(self, currentQuadrants):
        self.quadrants = currentQuadrants
        self.update()
        pass

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        try:
            for i, quadrant in enumerate(self.quadrants):
                qp.fillRect(quadrant[0], quadrant[1], 22, 22, QColor(
                    settings["color"][0], settings["color"][1], settings["color"][2],
                    150))
                qp.setPen(QColor(255, 255, 255))
                qp.setFont(QFont('Decorative', 12))
                qp.drawText(quadrant[0], quadrant[1]+30, str(inv_map[i]))
        except Exception as e:
            print(e)
        qp.end()
