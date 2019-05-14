from PySide2.QtWidgets import QWidget, QPushButton
from PySide2.QtCore import Qt
from PySide2.QtGui import QPaintEvent, QPainter, QPen

from customControls.boardWidget import BoardWidget


class MainWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWidget, self).__init__(*args, **kwargs)
        self.board = BoardWidget(self)
        # print(self.board.size())
        # self.board.resize(361, 321)
        # self.board.move(50, 50)
