from customControls.piecesWidget import PiecesWidget


class Car(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(Car, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.move(x, y)
        if x < 0:
            self.chess.setText('车')
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.chess.setText('車')
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    def check_one(self, x, y, ):
        x, y = self.pos()
        print(x, y)
        pass


class Horse(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(Horse, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.move(x, y)
        if x < 0:
            self.chess.setText('马')
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.chess.setText('馬')
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    pass


class Elephant(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(Elephant, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.move(x, y)
        if x < 0:
            self.chess.setText('相')
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.chess.setText('象')
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    pass


class Bodyguard(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(Bodyguard, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.move(x, y)
        if x < 0:
            self.chess.setText('士')
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.chess.setText('仕')
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    pass


class General(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(General, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.move(x, y)
        if x < 0:
            self.chess.setText('帅')
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.chess.setText('将')
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    pass


class Gun(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(Gun, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.chess.setText('炮')
        self.move(x, y)
        if x < 0:
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    pass


class Soldier(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(Soldier, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.move(x, y)
        if x < 0:
            self.chess.setText('兵')
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.chess.setText('卒')
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    pass
