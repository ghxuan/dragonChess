from PySide2.QtWidgets import QWidget, QPushButton
from PySide2.QtCore import Qt
from PySide2.QtGui import QPaintEvent, QPainter, QPen

from customControls.boardWidget import BoardWidget
from customControls.chessPieces import ChessPieces


class MainWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWidget, self).__init__(*args, **kwargs)
        self.board = BoardWidget(self)
        self.base = {}
        for i in range(5):
            for j in range(5):
                x, y = 30 + i * 60, j * 60
                self.base[(x, y)] = ''
                self.base[(x, -y)] = ''
                self.base[(-x, y)] = ''
                self.base[(-x, -y)] = ''
                self.piece = ChessPieces(self)
                self.piece.move(x, y)
                self.piece = ChessPieces(self)
                self.piece.move(x, -y)
                self.piece = ChessPieces(self)
                self.piece.move(-x, y)
                self.piece = ChessPieces(self)
                self.piece.move(-x, -y)
