from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from PySide2.QtGui import QPaintEvent, QPainter, QPen


# noinspection PyArgumentList,PyUnboundLocalVariable
class BoardWidget(QWidget):
    def __init__(self, *args, length=30, **kwargs):
        super(BoardWidget, self).__init__(*args, **kwargs)
        # self.resize(361, 321)
        # 小正方形的边长
        self.length = length * 2
        self.resize(self.length * 11, self.length * 10)
        self.lengths = dict([(i, i * self.length) for i in range(1, 11)])

    def paintEvent(self, event: QPaintEvent):
        return
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHints(QPainter.SmoothPixmapTransform)
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        # pen1 = QPen(Qt.black, 2, Qt.SolidLine)
        # painter.setPen(pen1)
        # painter.drawLine(0, 0, self.size().width(), 0)
        # painter.drawLine(0, 0, 0, self.size().height())
        # painter.drawLine(self.size().width(), 0, self.size().width(), self.size().height())
        # painter.drawLine(0, self.size().height(), self.size().width(), self.size().height())
        painter.setPen(pen)

        # 棋盘的大致框架
        for i in range(9):
            painter.drawLine(self.lengths[1], self.lengths[i + 1], self.lengths[5], self.lengths[i + 1])
            painter.drawLine(self.lengths[6], self.lengths[i + 1], self.lengths[10], self.lengths[i + 1])
            # painter.drawLine(self.lengths[5], self.lengths[i + 1], self.lengths[6], self.lengths[i + 1])
            painter.drawLine(self.lengths[i + 1], self.lengths[1], self.lengths[i + 1], self.lengths[9])
        painter.drawLine(self.lengths[5], self.lengths[1], self.lengths[6], self.lengths[1])
        painter.drawLine(self.lengths[5], self.lengths[i + 1], self.lengths[6], self.lengths[i + 1])
        painter.drawLine(self.lengths[i + 2], self.lengths[1], self.lengths[i + 2], self.lengths[9])

        # 兵下面的图形
        # pen1 = QPen(Qt.red, 2, Qt.SolidLine)
        # painter.setPen(pen1)
        for j in (4, 7):
            for i in range(0, 9, 2):
                if i != 0:
                    # 右上
                    painter.drawLine(self.lengths[j] + 5, self.lengths[i + 1] - 5, self.lengths[j] + 10,
                                     self.lengths[i + 1] - 5)
                    painter.drawLine(self.lengths[j] + 5, self.lengths[i + 1] - 5, self.lengths[j] + 5,
                                     self.lengths[i + 1] - 10)
                    # 左上
                    painter.drawLine(self.lengths[j] - 5, self.lengths[i + 1] - 5, self.lengths[j] - 10,
                                     self.lengths[i + 1] - 5)
                    painter.drawLine(self.lengths[j] - 5, self.lengths[i + 1] - 5, self.lengths[j] - 5,
                                     self.lengths[i + 1] - 10)
                    pass
                if i != 8:
                    # 右下
                    painter.drawLine(self.lengths[j] + 5, self.lengths[i + 1] + 5, self.lengths[j] + 10,
                                     self.lengths[i + 1] + 5)
                    painter.drawLine(self.lengths[j] + 5, self.lengths[i + 1] + 5, self.lengths[j] + 5,
                                     self.lengths[i + 1] + 10)
                    # 左下
                    painter.drawLine(self.lengths[j] - 5, self.lengths[i + 1] + 5, self.lengths[j] - 10,
                                     self.lengths[i + 1] + 5)
                    painter.drawLine(self.lengths[j] - 5, self.lengths[i + 1] + 5, self.lengths[j] - 5,
                                     self.lengths[i + 1] + 10)

        # 炮下面的图形
        for j in (3, 8):
            for i in (1, 7):
                if i != 0:
                    # 右上
                    painter.drawLine(self.lengths[j] + 5, self.lengths[i + 1] - 5, self.lengths[j] + 10,
                                     self.lengths[i + 1] - 5)
                    painter.drawLine(self.lengths[j] + 5, self.lengths[i + 1] - 5, self.lengths[j] + 5,
                                     self.lengths[i + 1] - 10)
                    # 左上
                    painter.drawLine(self.lengths[j] - 5, self.lengths[i + 1] - 5, self.lengths[j] - 10,
                                     self.lengths[i + 1] - 5)
                    painter.drawLine(self.lengths[j] - 5, self.lengths[i + 1] - 5, self.lengths[j] - 5,
                                     self.lengths[i + 1] - 10)
                    pass
                if i != 8:
                    # 右下
                    painter.drawLine(self.lengths[j] + 5, self.lengths[i + 1] + 5, self.lengths[j] + 10,
                                     self.lengths[i + 1] + 5)
                    painter.drawLine(self.lengths[j] + 5, self.lengths[i + 1] + 5, self.lengths[j] + 5,
                                     self.lengths[i + 1] + 10)
                    # 左下
                    painter.drawLine(self.lengths[j] - 5, self.lengths[i + 1] + 5, self.lengths[j] - 10,
                                     self.lengths[i + 1] + 5)
                    painter.drawLine(self.lengths[j] - 5, self.lengths[i + 1] + 5, self.lengths[j] - 5,
                                     self.lengths[i + 1] + 10)

        # 士所走的 X
        for j in (2, 9):
            for i in (4,):
                painter.drawLine(self.lengths[j] - self.length, self.lengths[i + 1] - self.length,
                                 self.lengths[j] + self.length,
                                 self.lengths[i + 1] + self.length)
                painter.drawLine(self.lengths[j] - self.length, self.lengths[i + 1] + self.length,
                                 self.lengths[j] + self.length,
                                 self.lengths[i + 1] - self.length)
        painter.end()
