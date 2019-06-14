from PySide2.QtCore import Qt, QRect, QSize

from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QRegion


class PressWidget(QWidget):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(PressWidget, self).__init__(*args, **kwargs)
        self.length = length
        self.area = length ** 2
        self.diam = self.length * 2
        self.center = length * 10, length * 9
        self.resize(self.diam, self.diam)
        x, y = pos
        self.move(x, y)
        self.setMask(QRegion(0, 0, self.diam, self.diam, QRegion.Ellipse))

    def pos(self):
        x, y = super(PressWidget, self).pos().toTuple()
        return int(x - self.center[0]), int(y - self.center[1])

    def move(self, *arg__1):
        x, y = arg__1
        super(PressWidget, self).move(x + self.center[0], y + self.center[1])
        pass

    def mousePressEvent(self, e):
        super(PressWidget, self).mousePressEvent(e)
        pass

    def enterEvent(self, event):
        super(PressWidget, self).enterEvent(event)
        pass
