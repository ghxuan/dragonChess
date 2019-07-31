from PySide2.QtCore import Qt, QRect, QSize, QPointF
from PySide2.QtWidgets import QWidget, QLabel
from PySide2.QtGui import QPaintEvent, QPainter, QPen, QColor, QRegion

from customControls.chessPieces import ChessPieces


class PiecesWidget(QWidget):
    def __init__(self, *args, length=30, **kwargs):
        super(PiecesWidget, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.length = length
        self.radius = length * 5 / 6
        self.area = length ** 2
        self.diam = self.length * 2
        self.center = length * 10, length * 9
        self.resize(self.diam, self.diam)
        if self.parent():
            self.ptc = self.parent().ptc
            self.can = self.parent().can
        self.case = {'x': (length * 9, '(cur, y)'), 'y': (length * 8, '(x, cur)')}
        self.chess = ChessPieces(self)
        self.setStyleSheet('')
        self.pre = False

    def check(self):
        self.can.clear()
        x, y = self.pos()
        self.check_(x, y, f=1, k='x')
        self.check_(x, y, f=-1, k='x')
        self.check_(x, y, f=1, k='y')
        self.check_(x, y, f=-1, k='y')
        # print(x, y)
        pass

    def pos(self):
        x, y = super(PiecesWidget, self).pos().toTuple()
        return int(x - self.center[0]), int(y - self.center[1])

    def move(self, *arg__1):
        x, y = arg__1
        super(PiecesWidget, self).move(x + self.center[0], y + self.center[1])
        pass
