from PySide2.QtCore import Qt, QPropertyAnimation, QPointF
from PySide2.QtWidgets import QWidget, QGraphicsOpacityEffect
from PySide2.QtGui import QPaintEvent, QPainter, QPen, QRegion, QColor


class RootPieces(QWidget):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(RootPieces, self).__init__(*args, **kwargs)
        # self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.length = length
        self.radius = length * 5 / 6
        self.area = self.radius ** 2
        self.diam = self.radius * 2
        self.center = length * (10 + 1 / 6), length * (9 + 1 / 6)
        self.resize(self.diam, self.diam)
        x, y = pos
        self.move(x, y)
        # self.move(self.length / 6, self.length / 6)
        mask = QRegion(-1, -1, self.diam + 1, self.diam + 1, QRegion.Ellipse)
        self.setMask(mask)

    def pos(self):
        x, y = super(RootPieces, self).pos().toTuple()
        return int(x - self.center[0]), int(y - self.center[1])

    def move(self, *arg__1):
        x, y = arg__1
        super(RootPieces, self).move(x + self.center[0], y + self.center[1])
        pass

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        # pen = QPen(Qt.white, 0, Qt.SolidLine)
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setBrush(QColor(255, 160, 90))
        painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(QPointF(self.radius, self.radius), self.radius - 1, self.radius - 1)
        super(RootPieces, self).paintEvent(event)
        pass


class FWidget(QWidget):
    def __init__(self, *args, length=30, **kwargs):
        super(FWidget, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.length = length
        self.lengths = dict((i, length * i / 6) for i in range(1, 13))
        self.resize(self.lengths[12], self.lengths[12])
        self.center = length * 10, length * 9
        self.opacity = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity)
        self.opacity.setOpacity(0)
        self.animation = QPropertyAnimation(self.opacity, b'opacity')
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        # self.animation.setKeyValueAt(0.25, 0.67)
        self.animation.setKeyValueAt(0.5, 1)
        # self.animation.setKeyValueAt(0.75, 0.67)
        self.animation.setEndValue(0)
        self.animation.setLoopCount(-1)

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

    pass
