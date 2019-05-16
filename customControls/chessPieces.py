from PySide2.QtWidgets import QPushButton
from PySide2.QtCore import QPropertyAnimation, QSize
from PySide2.QtGui import QPaintEvent


from PySide2.QtCore import QPointF
from PySide2.QtGui import QPaintEvent, QPainter, QPen, QColor


# noinspection PyArgumentList,PyUnboundLocalVariable
class ChessPieces(QPushButton):
    def __init__(self, *args, length=30, **kwargs):
        super(ChessPieces, self).__init__(*args, **kwargs)
        self.can = set()
        self.length = length
        self.area = length ** 2
        self.radius = length * 5 / 6
        self.diam = self.radius * 2
        self.center = length * (10 + 1 / 6), length * (9 + 1 / 6)
        self.resize(self.diam, self.diam)
        self.animation = QPropertyAnimation(self, b'size')
        self.animation.setStartValue(QSize(self.diam, self.diam))
        self.animation.setEndValue(QSize(self.length * 2, self.length * 2))
        if self.parent():
            self.base = self.parent().base

    def check(self):
        pass

    def pos(self):
        x, y = super(ChessPieces, self).pos().toTuple()
        return int(x - self.center[0]), int(y - self.center[1])

    def move(self, *arg__1):
        x, y = arg__1
        super(ChessPieces, self).move(x + self.center[0], y + self.center[1])
        pass

    def paintEvent(self, event: QPaintEvent):
        # super(ChessPieces, self).paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(QPen(QColor(0, 160, 230), 2))
        painter.setBrush(QColor(255, 160, 90))
        painter.drawEllipse(QPointF(self.length, self.length), self.radius, self.radius)
        pass

    def mousePressEvent(self, e):
        super(ChessPieces, self).mousePressEvent(e)
        self.can.clear()
        self.check()

    def enterEvent(self, event):
        super(ChessPieces, self).enterEvent(event)
        self.animation.start()
        pass
