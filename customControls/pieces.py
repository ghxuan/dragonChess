from customControls.chessPieces import ChessPieces


class Car(ChessPieces):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(Car, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.move(x, y)
        if x < 0:
            self.setText('车')
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.setText('車')
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    pass


class Horse(ChessPieces):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(Horse, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.move(x, y)
        if x < 0:
            self.setText('马')
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.setText('馬')
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    pass


class Elephant(ChessPieces):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(Elephant, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.move(x, y)
        if x < 0:
            self.setText('相')
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.setText('象')
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    pass


class Bodyguard(ChessPieces):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(Bodyguard, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.move(x, y)
        if x < 0:
            self.setText('士')
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.setText('仕')
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    pass


class General(ChessPieces):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(General, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.move(x, y)
        if x < 0:
            self.setText('帅')
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.setText('将')
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    pass


class Gun(ChessPieces):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(Gun, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.setText('炮')
        self.move(x, y)
        if x < 0:
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    pass


class Soldier(ChessPieces):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(Soldier, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.move(x, y)
        if x < 0:
            self.setText('兵')
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.setText('卒')
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    pass
