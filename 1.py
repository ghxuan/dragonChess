import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2.QtCore import Qt, QRect, QSize
from PySide2.QtGui import QPaintEvent, QPainter, QPen, QColor, QRegion


class Button(QPushButton):
    def __init__(self, *args, length=30, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.length = length
        self.area = length ** 2
        self.diam = self.length * 2
        self.center = length * 10, length * 9
        self.resize(self.diam + 10, self.diam + 10)
        self.setMask(QRegion(0, 0, self.diam, self.diam, QRegion.Ellipse))

    pass


class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        super(Widget, self).__init__(*args, **kwargs)
        self.but = Button(self)

    pass


def main():
    app = QApplication(sys.argv)
    label = Widget()
    label.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
