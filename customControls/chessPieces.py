from PySide2.QtCore import QPointF, Qt
from PySide2.QtWidgets import QPushButton
from PySide2.QtGui import QPaintEvent, QPainter, QPen, QColor, QRegion, QPainterPath


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
        mask = QRegion(-1, -1, self.diam + 1, self.diam + 1, QRegion.Ellipse)
        self.setMask(mask)

    def mousePressEvent(self, e):
        print(self.pos())

    def check(self):
        pass

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setBrush(QColor(255, 160, 90))
        painter.drawEllipse(QPointF(self.radius, self.radius), self.radius - 1, self.radius - 1)
        super(ChessPieces, self).paintEvent(event)
        pass
