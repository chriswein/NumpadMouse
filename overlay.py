from settings import settings

from PyQt5 import QtCore, Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DesktopOverlay(QMainWindow):
    def __init__(self, screen, helper):
        QMainWindow.__init__(self)
        self.h = helper
        self.inv_map = {v: k for k, v in self.h.mapping.items()}
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
        )
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
                QtCore.QSize(screen.size().width(), screen.size().height()),
                QtWidgets.qApp.desktop().availableGeometry()
            ))

        self.quadrants = self.h.calculate_quadrants(
            screen.size().width(), screen.size().height(), 0, 0)
        self.last_width = screen.size().width()
        self.last_height = screen.size().height()

    def setQuadrants(self, currentQuadrants, last_width, last_height):
        self.quadrants = currentQuadrants
        self.last_width = last_width
        self.last_height = last_height 
        self.update()

    def paintEvent(self, event):
        """
        Will be called whenever user gives input and quadrants are updated
        """
        qp = QPainter()
        qp.begin(self)
        try: 
            for i, quadrant in enumerate(self.quadrants):
                qp.setPen(QColor(255, 0, 0))
                left, top = quadrant[0]-self.last_width//6, quadrant[1]-self.last_height//6
                # print(left,top,i)
                qp.drawRect(left,top, self.last_width//3, self.last_height//3)
                qp.setFont(QFont('Decorative', 12)) 
                qp.drawText(left+10,top+30, str(self.inv_map[i]))
        except Exception as e:
            # print(e)
            None
        qp.end()
