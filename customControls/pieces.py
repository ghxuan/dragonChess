from customControls.piecesWidget import PiecesWidget


class Car(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), shift=(0, 0), length=30, **kwargs):
        super(Car, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        a, b = shift
        self.move(x + a, y + b)
        if x < 0:
            self.chess.setText('车')
            self.setStyleSheet("color: #c6385a;")
        else:
            self.chess.setText('車')
            self.setStyleSheet("color: #232323;")

    def check_(self, x, y, f=1, k='x'):
        cur, temp = eval(k), self.case.get(k, (self.length * 9, '(cur, y)'))
        temp, strings = temp
        while f * cur < temp:
            cur += f * self.diam
            tuples = eval(strings)
            res = self.parent().ptc.get(tuples, 0)
            if res == '':
                self.parent().can.add(tuples)
            else:
                if res != 0 and self.same != res.same:
                    self.parent().can.add(tuples)
                break


class Horse(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), shift=(0, 0), length=30, **kwargs):
        super(Horse, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        a, b = shift
        self.move(x + a, y + b)
        self.case = {'x': (length * 9, '(cur, y)', '[(cur, y - self.diam), (cur, y + self.diam)]'),
                     'y': (length * 8, '(x, cur)', '[(x - self.diam, cur), (x + self.diam, cur)]')}
        if x < 0:
            self.chess.setText('马')
            self.setStyleSheet("color: #c6385a;")
        else:
            self.chess.setText('馬')
            self.setStyleSheet("color: #232323;")

    def check_(self, x, y, f=1, k='x'):
        cur, temp = eval(k), self.case.get(k, (self.length * 9,
                                               '(cur, y)', '[(cur, y - self.diam), (cur, y + self.diam)]'))
        temp, strings, string = temp
        if f * cur < temp:
            cur += f * self.diam
            tuples = eval(strings)
            res = self.parent().ptc.get(tuples, 0)
            if res == '':
                cur += f * self.diam
                lists = eval(string)
                for l in lists:
                    res = self.parent().ptc.get(l, 0)
                    if res == '':
                        self.parent().can.add(l)
                    elif res != 0 and self.same != res.same:
                        self.parent().can.add(l)


class Elephant(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), shift=(0, 0), length=30, **kwargs):
        super(Elephant, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        a, b = shift
        self.move(x + a, y + b)
        self.case = {
            (1, 'x'): (length * 9, '(x + self.diam, y - self.diam)', '[(x + 2 * self.diam, y - 2 * self.diam)]'),
            (-1, 'x'): (length * 9, '(x - self.diam, y - self.diam)', '[(x - 2 * self.diam, y - 2 * self.diam)]'),
            (1, 'y'): (length * 8, '(x - self.diam, y + self.diam)', '[(x - 2 * self.diam, y + 2 * self.diam)]'),
            (-1, 'y'): (length * 8, '(x + self.diam, y + self.diam)', '[(x + 2 * self.diam, y + 2 * self.diam)]'),
        }
        if x < 0:
            self.forward = -1
            self.chess.setText('相')
            self.setStyleSheet("color: #c6385a;")
        else:
            self.forward = 1
            self.chess.setText('象')
            self.setStyleSheet("color: #232323;")

    def check_(self, x, y, f=1, k='x'):
        cur, temp = eval(k), self.case.get((f, k),
                                           (self.length * 9,
                                            '(x + self.diam, y - self.diam)',
                                            '[(x + 2 * self.diam, y - 2 * self.diam)]'))
        temp, strings, string = temp
        if f * cur < temp:
            tuples = eval(strings)
            if tuples[0] * self.forward < 0:
                return
            res = self.parent().ptc.get(tuples, 0)
            if res == '':
                lists = eval(string)
                for l in lists:
                    res = self.parent().ptc.get(l, 0)
                    if res == '':
                        self.parent().can.add(l)
                    elif res != 0 and self.same != res.same:
                        self.parent().can.add(l)


class Bodyguard(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), shift=(0, 0), length=30, **kwargs):
        super(Bodyguard, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        a, b = shift
        self.move(x + a, y + b)
        self.case = {
            (1, 'x'): (length * 9, '(x + self.diam, y - self.diam)'),
            (-1, 'x'): (length * 9, '(x - self.diam, y - self.diam)'),
            (1, 'y'): (length * 8, '(x - self.diam, y + self.diam)'),
            (-1, 'y'): (length * 8, '(x + self.diam, y + self.diam)'),
        }
        if x < 0:
            self.chess.setText('士')
            self.setStyleSheet("color: #c6385a;")
        else:
            self.chess.setText('仕')
            self.setStyleSheet("color: #232323;")

    def check_(self, x, y, f=1, k='x'):
        cur, temp = eval(k), self.case.get((f, k),
                                           (self.length * 9,
                                            '(x + self.diam, y - self.diam)'))
        temp, strings = temp
        if f * cur < temp:
            tuples = eval(strings)
            if abs(tuples[1]) > 60 or abs(tuples[0]) < 210:
                return
            res = self.parent().ptc.get(tuples, 0)
            if res == '':
                self.parent().can.add(tuples)
            elif res != 0 and self.same != res.same:
                self.parent().can.add(tuples)


class General(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), shift=(0, 0), length=30, **kwargs):
        super(General, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        a, b = shift
        self.move(x + a, y + b)
        if x < 0:
            self.chess.setText('帅')
            self.setStyleSheet("color: #c6385a;")
        else:
            self.chess.setText('将')
            self.setStyleSheet("color: #232323;")

    def check_(self, x, y, f=1, k='x'):
        cur, temp = eval(k), self.case.get(k, (self.length * 9, '(cur, y)'))
        temp, strings = temp
        if f * cur < temp:
            cur += f * self.diam
            tuples = eval(strings)
            if abs(tuples[1]) > 60 or abs(tuples[0]) < 210:
                return
            res = self.parent().ptc.get(tuples, 0)
            if res == '':
                self.parent().can.add(tuples)
            elif res != 0 and self.same != res.same:
                self.parent().can.add(tuples)


class Gun(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), shift=(0, 0), length=30, **kwargs):
        super(Gun, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        a, b = shift
        self.move(x + a, y + b)
        self.chess.setText('炮')
        if x < 0:
            self.setStyleSheet("color: #c6385a;")
        else:
            self.setStyleSheet("color: #232323;")

    def check_(self, x, y, f=1, k='x'):
        cur, temp = eval(k), self.case.get(k, (self.length * 9, '(cur, y)'))
        temp, strings = temp
        while f * cur < temp:
            cur += f * self.diam
            tuples = eval(strings)
            res = self.parent().ptc.get(tuples, 0)
            if res == '':
                self.parent().can.add(tuples)
            else:
                break
        while f * cur < temp:
            cur += f * self.diam
            tuples = eval(strings)
            res = self.parent().ptc.get(tuples, 0)
            if res != '':
                if res != 0 and self.same != res.same:
                    self.parent().can.add(tuples)
                break


class Soldier(PiecesWidget):
    def __init__(self, *args, pos=(0, 0), shift=(0, 0), length=30, **kwargs):
        super(Soldier, self).__init__(*args, length=length, **kwargs)
        x, y = pos
        a, b = shift
        self.move(x + a, y + b)
        if x < 0:
            self.forward = -1
            self.chess.setText('兵')
            self.setStyleSheet("color: #c6385a;")
        else:
            self.forward = 1
            self.chess.setText('卒')
            self.setStyleSheet("color: #232323;")

    def check_(self, x, y, f=1, k='x'):
        if f == self.forward and k == 'x':
            return
        if self.forward * x > 0 and k == 'y':
            return
        cur, temp = eval(k), self.case.get(k, (self.length * 9, '(cur, y)'))
        temp, strings = temp
        if f * cur < temp:
            cur += f * self.diam
            tuples = eval(strings)
            res = self.parent().ptc.get(tuples, 0)
            if res == '':
                self.parent().can.add(tuples)
            elif res != 0 and self.same != res.same:
                self.parent().can.add(tuples)
