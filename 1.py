import sys

# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class Widget(QPushButton):
    def __init__(self):
        super(Widget, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.pixmap = QPixmap('resource/ico/title.ico')
        pass

    def paintEvent(self, a0: QPaintEvent):
        # r1 = QRegion(QRect(0, 0, 50, 50), QRegion.Ellipse)
        self.animation = QPropertyAnimation(self, b'size')
        self.animation.setStartValue(QRect(0, 0, 50, 50))
        self.animation.setEndValue(QRect(0, 0, 60, 60))
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        # r2 = QRegion(QRect(self.rect().x() + self.rect().width() // 4, self.rect().y() + self.rect().height() // 4,
        #                    self.rect().width() // 4, self.rect().height() // 4))
        # r3 = r1.xored(r2)
        # self.setMask(r1)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawPixmap(0, 0, self.pixmap.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        pass

    def enterEvent(self, a0: QEvent):
        self.animation.start()
        pass


def main():
    app = QApplication(sys.argv)
    label = Widget()
    label.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
