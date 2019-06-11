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

    def check_(self, x, y, f=1, k='x'):
        cur, temp = eval(k), self.case.get(k, (self.length * 9, '(cur, y)'))
        temp, strings = temp
        while f * cur < temp:
            cur += f * self.diam
            tuple_xy = eval(strings)
            if self.base.get(tuple_xy) == '':
                self.can.add(tuple_xy)
            else:
                break


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


class Car(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(Car, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.move(x, y)
        if x < 0:
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    def check_(self, x, y, f=1, k='x'):
        cur, temp = eval(k), self.case.get(k, (self.length * 9, '(cur, y)'))
        temp, strings = temp
        while f * cur < temp:
            cur += f * self.diam
            tuples = eval(strings)
            res = self.base.get(tuples, 0)
            if res == '':
                self.can.add(tuples)
            else:
                if res != 0 and self.same != res.same:
                    self.can.add(tuples)
                break


class Horse(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(Horse, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.move(x, y)
        self.case = {'x': (length * 9, '(cur, y)', '[(cur, y - self.diam), (cur, y + self.diam)]'),
                     'y': (length * 8, '(x, cur)', '[(x - self.diam, cur), (x + self.diam, cur)]')}
        if x < 0:
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    def check_(self, x, y, f=1, k='x'):
        cur, temp = eval(k), self.case.get(k, (self.length * 9,
                                               '(x, cur)', '[(x - self.length, cur), (x + self.length, cur)]'))
        temp, strings, string = temp
        if f * cur < temp:
            cur += f * self.diam
            tuples = eval(strings)
            res = self.base.get(tuples, 0)
            if res == '':
                cur += f * self.diam
                lists = eval(string)
                for l in lists:
                    res = self.base.get(l, 0)
                    if res == '':
                        self.can.add(l)
                    elif res != 0 and self.same != res.same:
                        self.can.add(l)


class Elephant(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(Elephant, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.move(x, y)
        if x < 0:
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    pass


class Bodyguard(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(Bodyguard, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.move(x, y)
        if x < 0:
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    pass


class General(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(General, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        self.move(x, y)
        if x < 0:
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    def check_(self, x, y, f=1, k='x'):
        cur, temp = eval(k), self.case.get(k, (self.length * 9, '(cur, y)'))
        temp, strings = temp
        if f * cur < temp:
            cur += f * self.diam
            tuples = eval(strings)
            res = self.base.get(tuples, 0)
            if res == '':
                self.can.add(tuples)
            elif res != 0 and self.same != res.same:
                self.can.add(tuples)

    pass


class Gun(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), length=30, **kwargs):
        super(Gun, self).__init__(*args, length=length, **kwargs)
        x, y = pos
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
            self.setStyleSheet("color: #c6385a;background-color:#5d9eb2;")
        else:
            self.setStyleSheet("color: #232323;background-color:#5d9eb2;")

    pass
