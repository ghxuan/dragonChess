from PySide2.QtWidgets import QPushButton
from PySide2.QtCore import Qt, QPointF
from PySide2.QtGui import QPaintEvent, QPainter, QPen, QColor


# noinspection PyArgumentList,PyUnboundLocalVariable
class ChessPieces(QPushButton):
    def __init__(self, *args, length=30, **kwargs):
        super(ChessPieces, self).__init__(*args, **kwargs)
        self.length = length
        self.area = length ** 2
        self.radius = length * 5 / 6
        self.center = length * (10 + 1 / 6), length * (9 + 1 / 6)
        self.resize(self.radius * 2, self.radius * 2)
        if self.parent():
            self.base = self.parent().base

    def move(self, *arg__1):
        x, y = arg__1
        cx, cy = self.center
        super(ChessPieces, self).move(x + cx, y + cy)
        pass

    def paintEvent(self, event: QPaintEvent):
        super(ChessPieces, self).paintEvent(event)
        # painter = QPainter(self)
        # painter.setRenderHint(QPainter.Antialiasing, True)
        # painter.setPen(QPen(QColor(0, 160, 230), 2))
        # painter.setBrush(QColor(255, 160, 90))
        # painter.drawEllipse(QPointF(self.length, self.length), self.radius, self.radius)
        pass

    def mousePressEvent(self, e):
        super(ChessPieces, self).mousePressEvent(e)
