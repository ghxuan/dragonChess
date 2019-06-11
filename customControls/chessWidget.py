import os
from random import choice

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow

from customControls.mainWidget import MainWidget
# from customControls.startWidget import StartWidget


class ChessWidget(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ChessWidget, self).__init__(*args, **kwargs)
        self.setStyleSheet("""
                QMainWindow{
                    font-size:26px;
                    font-family:Microsoft YaHei;
                    background-color:#fff;
                    color:#000000;
                }
                BoardWidget{
                    font-size:26px;
                    border:1px solid lightgrey;
                    font-family:Microsoft YaHei;
                    border:1px solid lightgrey;
                    color:#000000;
                    background-color:black;
                }
                """)

        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.resize(680, 620)
        self.setFixedSize(self.width(), self.height())
        if os.path.exists('resource'):
            icon = QIcon('resource/ico/title.ico')
        else:
            icon = QIcon('title.ico')
        self.setWindowIcon(icon)
        # self.setWindowTitle('中国象棋')

        self.start = MainWidget()
        # self.start = StartWidget()
        # self.home = MainWidget()

        self.setCentralWidget(self.start)
        # self.home.new.clicked.connect(lambda: self.play(self.start))
        # self.start.easy.clicked.connect(lambda: self.play(self.home, n=choice(range(40, 46))))
        # self.start.normal.clicked.connect(lambda: self.play(self.home, n=choice(range(46, 51))))
        # self.start.hard.clicked.connect(lambda: self.play(self.home, n=51))
        # self.start.very_hard.clicked.connect(lambda: self.play(self.home, n=52))
        pass

    def play(self, widget, n=0):
        self.home.push.move(self.home.out)
        self.home.rotate_push.move(self.home.out)
        self.centralWidget().setParent(None)
        self.setCentralWidget(widget)
        if widget == self.home:
            widget.write_all_button(n)
