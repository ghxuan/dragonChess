from PySide2.QtCore import Qt, QRect
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPaintEvent, QPainter, QPen, QColor


class MBorderWidget(QWidget):
    def __init__(self, *args, length=30, **kwargs):
        super(MBorderWidget, self).__init__(*args, **kwargs)
        self.length = length
        self.resize(length * 2, length * 2)
        self.center = length * 10, length * 9

    def pos(self):
        x, y = super(MBorderWidget, self).pos().toTuple()
        return int(x - self.center[0]), int(y - self.center[1])

    def move(self, *arg__1):
        x, y = arg__1
        super(MBorderWidget, self).move(x + self.center[0], y + self.center[1])

    def mousePressEvent(self, e):
        super(MBorderWidget, self).mousePressEvent(e)

    def paintEvent(self, event: QPaintEvent):
        x, y = self.pos()
        painter = QPainter()
        painter.begin(self)
        # painter.setRenderHints(QPainter.SmoothPixmapTransform)
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        painter.setPen(pen)
        # 右上
        painter.drawLine(40, 5, 55, 5)
        painter.drawLine(55, 5, 55, 20)
        # 左上
        painter.drawLine(5, 5, 20, 5)
        painter.drawLine(5, 5, 5, 20)

        # 右下
        painter.drawLine(40, 55, 55, 55)
        painter.drawLine(55, 40, 55, 55)
        # 左下
        painter.drawLine(5, 55, 20, 55)
        painter.drawLine(5, 55, 5, 40)
        painter.setPen(QPen(QColor(0, 160, 230), 2))
        # painter.setBrush(QColor(255, 160, 90))
        painter.drawRect(QRect(0, 0, self.length * 2, self.length * 2))
        painter.end()


class BorderWidget(QWidget):
    def __init__(self, *args, length=30, **kwargs):
        super(BorderWidget, self).__init__(*args, **kwargs)
        self.length = length
        self.lengths = dict((i, length * i / 6) for i in range(1, 13))
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.resize(self.lengths[12], self.lengths[12])
        self.center = length * 10, length * 9

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter()
        painter.begin(self)
        # painter.setRenderHints(QPainter.SmoothPixmapTransform)
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        painter.setPen(pen)
        # 右上
        painter.drawLine(self.lengths[8], self.lengths[1], self.lengths[11], self.lengths[1])
        painter.drawLine(self.lengths[11], self.lengths[1], self.lengths[11], self.lengths[4])
        # 左上
        painter.drawLine(self.lengths[1], self.lengths[1], self.lengths[4], self.lengths[1])
        painter.drawLine(self.lengths[1], self.lengths[1], self.lengths[1], self.lengths[4])

        # 右下
        painter.drawLine(self.lengths[8], self.lengths[11], self.lengths[11], self.lengths[11])
        painter.drawLine(self.lengths[11], self.lengths[8], self.lengths[11], self.lengths[11])
        # 左下
        painter.drawLine(self.lengths[1], self.lengths[11], self.lengths[4], self.lengths[11])
        painter.drawLine(self.lengths[1], self.lengths[11], self.lengths[1], self.lengths[8])
        # painter.setPen(QPen(QColor(0, 160, 230), 2))
        # # painter.setBrush(QColor(255, 160, 90))
        # painter.drawRect(QRect(0, 0, self.length * 2, self.length * 2))
        painter.end()
