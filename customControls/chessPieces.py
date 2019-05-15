from PySide2.QtWidgets import QPushButton
from PySide2.QtCore import Qt, QPointF
from PySide2.QtGui import QPaintEvent, QPainter, QPen, QColor


# noinspection PyArgumentList,PyUnboundLocalVariable
class ChessPieces(QPushButton):
    def __init__(self, *args, length=30, **kwargs):
        super(ChessPieces, self).__init__(*args, **kwargs)
        self.length = length
        # self.radius = length * 5 / 6
        self.radius = length
        self.center = length * 10, length * 9
        self.resize(self.radius * 2, self.radius * 2)
        self.setStyleSheet("""
            ChessPieces{
                    background-color:black;
            }
        """)

    def move(self, *arg__1):
        x, y = arg__1
        cx, cy = self.center
        super(ChessPieces, self).move(x + cx, y + cy)
        pass

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(QPen(QColor(0, 160, 230), 2))
        painter.setBrush(QColor(255, 160, 90))
        painter.drawEllipse(QPointF(30, 30), 25, 25)
        pass

    def mousePressEvent(self, e):
        x, y = e.x() - 30, e.y() - 30
        if x ** 2 + y ** 2 <= 525:
            super(ChessPieces, self).mousePressEvent(e)
            print(self.pos())
