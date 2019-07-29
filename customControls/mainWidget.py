from PySide2.QtWidgets import QWidget, QPushButton
from PySide2.QtCore import Qt
from PySide2.QtGui import QPaintEvent, QPainter, QPen

from customControls.boardWidget import BoardWidget
from customControls.rootPieces import RootPieces
from customControls.pieces import Car, Horse, Elephant, Bodyguard, General, Gun, Soldier


class MainWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWidget, self).__init__(*args, **kwargs)
        self.length = 30
        self.setMouseTracking(True)
        self.base_pieces = {2940: 'Car', 2880: 'Horse', 2820: 'Elephant', 2760: 'Bodyguard', 2700: 'General',
                            1680: 'Gun', 900: 'Soldier', 1020: 'Soldier', 1140: 'Soldier'}
        self.board = BoardWidget(self, length=self.length)
        rad = str(self.length * 5 // 6)

        # self.setStyleSheet("""
        #     ChessPieces{
        #         border-color: #6ec672;
        #         color: #f3f3f3;
        #         font-size: """ + rad + """px;
        #         border-radius: """ + rad + """px;
        #         background-color: #46804a;
        #         font-family: "微软雅黑 light", "微软雅黑", Arial,sans-serif;
        #         text-align: center;
        #         border: 2px solid rgba(0, 0, 0, 0);
        #     }
        # """)
        self.setStyleSheet("""
            ChessPieces{
                font-family: "微软雅黑 light", "微软雅黑", Arial,sans-serif;
                font-size: """ + rad + """px;
                text-align: center;
                border: none;
            }
            PressWidget{
                font-family: "微软雅黑 light", "微软雅黑", Arial,sans-serif;
                font-size: """ + rad + """px;
                text-align: center;
                border: none;
            }
        """)
        self.can = set()
        self.base = {
            (30, 0): '', (-30, 0): '', (30, 60): '', (30, -60): '', (-30, 60): '', (-30, -60): '', (30, 120): '',
            (30, -120): '', (-30, 120): '', (-30, -120): '', (30, 180): '', (30, -180): '', (-30, 180): '',
            (-30, -180): '', (30, 240): '', (30, -240): '', (-30, 240): '', (-30, -240): '', (90, 0): '', (-90, 0): '',
            (90, 60): '', (90, -60): '', (-90, 60): '', (-90, -60): '', (90, 120): '', (90, -120): '', (-90, 120): '',
            (-90, -120): '', (90, 180): '', (90, -180): '', (-90, 180): '', (-90, -180): '', (90, 240): '',
            (90, -240): '', (-90, 240): '', (-90, -240): '', (150, 0): '', (-150, 0): '', (150, 60): '', (150, -60): '',
            (-150, 60): '', (-150, -60): '', (150, 120): '', (150, -120): '', (-150, 120): '', (-150, -120): '',
            (150, 180): '', (150, -180): '', (-150, 180): '', (-150, -180): '', (150, 240): '', (150, -240): '',
            (-150, 240): '', (-150, -240): '', (210, 0): '', (-210, 0): '', (210, 60): '', (210, -60): '',
            (-210, 60): '', (-210, -60): '', (210, 120): '', (210, -120): '', (-210, 120): '', (-210, -120): '',
            (210, 180): '', (210, -180): '', (-210, 180): '', (-210, -180): '', (210, 240): '', (210, -240): '',
            (-210, 240): '', (-210, -240): '', (270, 0): '', (-270, 0): '', (270, 60): '', (270, -60): '',
            (-270, 60): '', (-270, -60): '', (270, 120): '', (270, -120): '', (-270, 120): '', (-270, -120): '',
            (270, 180): '', (270, -180): '', (-270, 180): '', (-270, -180): '', (270, 240): '', (270, -240): '',
            (-270, 240): '', (-270, -240): ''
        }
        self.base_widget = {
            (30, 0): '', (-30, 0): '', (30, 60): '', (30, -60): '', (-30, 60): '', (-30, -60): '', (30, 120): '',
            (30, -120): '', (-30, 120): '', (-30, -120): '', (30, 180): '', (30, -180): '', (-30, 180): '',
            (-30, -180): '', (30, 240): '', (30, -240): '', (-30, 240): '', (-30, -240): '', (90, 0): '', (-90, 0): '',
            (90, 60): '', (90, -60): '', (-90, 60): '', (-90, -60): '', (90, 120): '', (90, -120): '', (-90, 120): '',
            (-90, -120): '', (90, 180): '', (90, -180): '', (-90, 180): '', (-90, -180): '', (90, 240): '',
            (90, -240): '', (-90, 240): '', (-90, -240): '', (150, 0): '', (-150, 0): '', (150, 60): '', (150, -60): '',
            (-150, 60): '', (-150, -60): '', (150, 120): '', (150, -120): '', (-150, 120): '', (-150, -120): '',
            (150, 180): '', (150, -180): '', (-150, 180): '', (-150, -180): '', (150, 240): '', (150, -240): '',
            (-150, 240): '', (-150, -240): '', (210, 0): '', (-210, 0): '', (210, 60): '', (210, -60): '',
            (-210, 60): '', (-210, -60): '', (210, 120): '', (210, -120): '', (-210, 120): '', (-210, -120): '',
            (210, 180): '', (210, -180): '', (-210, 180): '', (-210, -180): '', (210, 240): '', (210, -240): '',
            (-210, 240): '', (-210, -240): '', (270, 0): '', (-270, 0): '', (270, 60): '', (270, -60): '',
            (-270, 60): '', (-270, -60): '', (270, 120): '', (270, -120): '', (-270, 120): '', (-270, -120): '',
            (270, 180): '', (270, -180): '', (-270, 180): '', (-270, -180): '', (270, 240): '', (270, -240): '',
            (-270, 240): '', (-270, -240): ''
        }
        self.set_pieces()

    def set_pieces(self):
        for x, y in self.base.keys():
            press = RootPieces(self, pos=(x, y), length=self.length)
            self.base_widget[x, y] = press
            val = abs(x) * 10 + abs(y)
            if val not in self.base_pieces:
                self.base[x, y] = ''
            else:
                piece = eval(f'{self.base_pieces[val]}(self, pos=(x, y), length=self.length)')
                if x < 0:
                    piece.same = True
                else:
                    piece.same = False
                self.base[x, y] = piece

    def mouseMoveEvent(self, event):
        # print(event)
        # print(dir(event))
        pass

    def mousePressEvent(self, event):
        print(dir(event))
        print(event.pos())
