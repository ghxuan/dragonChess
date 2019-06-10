from PySide2.QtCore import Qt, QRect, QSize

from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPaintEvent, QPainter, QPen, QColor

from customControls.borderWidget import BorderWidget
from customControls.chessPieces import ChessPieces


class PiecesWidget(QWidget):
    def __init__(self, *args, length=30, **kwargs):
        super(PiecesWidget, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.can = set()
        self.length = length
        self.area = length ** 2
        self.diam = self.length * 2
        self.center = length * 10, length * 9
        self.resize(self.diam, self.diam)
        if self.parent():
            self.base = self.parent().base
        self.chess = ChessPieces(self)
        self.border = BorderWidget(self)
        self.animation = self.border.animation

    def check(self):
        pass

    def pos(self):
        x, y = super(PiecesWidget, self).pos().toTuple()
        return int(x - self.center[0]), int(y - self.center[1])

    def move(self, *arg__1):
        x, y = arg__1
        super(PiecesWidget, self).move(x + self.center[0], y + self.center[1])
        pass

    def paintEvent(self, event: QPaintEvent):
        super(PiecesWidget, self).paintEvent(event)
        # painter = QPainter(self)
        # painter.setPen(QPen(QColor(0, 160, 230), 2))
        # # painter.setBrush(QColor(255, 160, 90))
        # painter.drawRect(QRect(0, 0, self.length * 2, self.length * 2))
        pass

    def press(self):
        pass

    def enter(self):
        self.animation.start()
        pass

    def leave(self):
        self.animation.stop()
        self.border.opacity.setOpacity(0)
        pass

    def mousePressEvent(self, e):
        super(PiecesWidget, self).mousePressEvent(e)
        # self.can.clear()
        # self.check()
        pass

    def enterEvent(self, event):
        super(PiecesWidget, self).enterEvent(event)
        pass

    pass
