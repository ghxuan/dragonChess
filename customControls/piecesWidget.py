from PySide2.QtCore import Qt, QRect, QSize

from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPaintEvent, QPainter, QPen, QColor, QRegion

from customControls.borderWidget import BorderWidget
from customControls.chessPieces import ChessPieces


class PiecesWidget(QWidget):
    def __init__(self, *args, length=30, **kwargs):
        super(PiecesWidget, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.length = length
        self.area = length ** 2
        self.diam = self.length * 2
        self.center = length * 10, length * 9
        self.resize(self.diam, self.diam)
        if self.parent():
            self.base = self.parent().base
            self.can = self.parent().can
        self.case = {'x': (length * 9, '(cur, y)'), 'y': (length * 8, '(x, cur)')}
        self.chess = ChessPieces(self)
        self.border = BorderWidget(self)
        self.animation = self.border.animation
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.pre = False

    def check(self):
        x, y = self.pos()
        self.check_(x, y, f=1, k='x')
        self.check_(x, y, f=-1, k='x')
        self.check_(x, y, f=1, k='y')
        self.check_(x, y, f=-1, k='y')
        print(x, y)
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
        self.can.clear()
        self.check()
        self.animation.stop()
        self.border.opacity.setOpacity(1)
        print(self.can)
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
        pass

    def enterEvent(self, event):
        super(PiecesWidget, self).enterEvent(event)
        # print(self.same)
        pass

    pass
