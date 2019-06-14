from PySide2.QtCore import QPointF
from PySide2.QtWidgets import QPushButton
from PySide2.QtGui import QPaintEvent, QPainter, QPen, QColor


# noinspection PyArgumentList,PyUnboundLocalVariable
class ChessPieces(QPushButton):
    def __init__(self, *args, length=30, **kwargs):
        super(ChessPieces, self).__init__(*args, **kwargs)
        self.can = set()
        self.length = length
        self.radius = length * 5 / 6
        self.area = self.radius ** 2
        self.diam = self.radius * 2
        self.center = length * (10 + 1 / 6), length * (9 + 1 / 6)
        self.resize(self.diam, self.diam)
        if self.parent():
            self.base = self.parent().base
        self.move(self.length / 6, self.length / 6)

    def check(self):
        pass

    def paintEvent(self, event: QPaintEvent):
        super(ChessPieces, self).paintEvent(event)
        # painter = QPainter(self)
        # painter.setRenderHint(QPainter.Antialiasing, True)
        # painter.setBrush(QColor(255, 160, 90))
        # painter.drawEllipse(QPointF(self.radius, self.radius), self.radius, self.radius)
        pass

    def mousePressEvent(self, e):
        super(ChessPieces, self).mousePressEvent(e)
        self.parent().press()
        self.parent().pre = True
        # x, y = e.pos().toTuple()
        # if (x - self.radius) ** 2 + (y - self.radius) ** 2 <= self.area:
        #     pass

    def enterEvent(self, event):
        super(ChessPieces, self).enterEvent(event)
        if not self.parent().pre:
            self.parent().enter()
        # x, y = event.pos().toTuple()
        # if (x - self.radius) ** 2 + (y - self.radius) ** 2 <= self.area:
        #     self.parent().enter()
        # self.parent().animation.stop()
        pass

    def leaveEvent(self, event):
        super(ChessPieces, self).leaveEvent(event)
        if not self.parent().pre:
            self.parent().leave()
