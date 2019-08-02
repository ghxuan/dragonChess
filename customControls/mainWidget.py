from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt

from customControls.rootPieces import FWidget
from customControls.boardWidget import BoardWidget
from customControls.pieces import Car, Horse, Elephant, Bodyguard, General, Gun, Soldier


class MainWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWidget, self).__init__(*args, **kwargs)
        self.mouse = {
            Qt.LeftButton: self.left_button,
            Qt.RightButton: self.right_button,
        }
        self.foot = []
        self.red, self.black = {}, {}
        # ChessPieces to point, point to ChessPieces, widget to point, point to widget
        self.ctp, self.ptc, self.wtp, self.ptw = {}, {}, {}, {}
        # 第几次点击
        self.first = self.one = None
        self.length = 30
        self.diam = self.length * 2
        self.area = (self.length * 5 / 6) ** 2
        self.center = self.diam * 5
        self.setMouseTracking(True)
        self.board = BoardWidget(self, length=self.length)
        rad = str(self.length * 5 // 6)
        self.base_pieces = {2940: Car, 2880: Horse, 2820: Elephant, 2760: Bodyguard, 2700: General,
                            1680: Gun, 900: Soldier, 1020: Soldier, 1140: Soldier}
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
        self.copy = self.can = set()
        self.base = {
            (90, 0), (210, -60), (30, 60), (210, 240), (-90, 120), (270, 60), (30, 0), (-30, -180), (90, -180),
            (210, 0), (-270, -180), (270, -60), (-150, -180), (-150, 120), (30, -60), (150, 0), (-30, -120),
            (270, 120), (90, 240), (-30, 240), (-210, 60), (-90, -120), (-210, -240), (-270, -240), (270, 0),
            (-150, 60), (-30, -240), (210, -180), (30, 180), (210, 120), (90, 60), (-90, 180), (270, 180),
            (150, 180), (-150, -240), (90, -60), (90, -240), (210, -120), (30, 120), (210, 180), (-150, -60),
            (-150, 240), (-270, 240), (150, -120), (-150, -120), (270, 240), (150, 240), (150, -60), (-30, 120),
            (-210, 180), (-90, -240), (-210, -120), (-90, -60), (150, -240), (-150, 180), (-270, 180), (90, 180),
            (-90, 60), (-30, 180), (-210, 120), (-210, -180), (30, -240), (150, 60), (-270, 0), (270, -240),
            (90, -120), (210, -240), (30, 240), (210, 60), (-90, 240), (-270, 120), (30, -120), (-150, 0),
            (-30, -60), (150, 120), (150, -180), (-270, -60), (270, -180), (-210, 0), (-90, -180), (30, -180),
            (-30, 0), (-270, 60), (90, 120), (-30, 60), (-210, 240), (-210, -60), (-90, 0), (-270, -120), (270, -120)
        }
        self.set_pieces()
        self.set_can()

    def set_pieces(self):
        self.can.clear()
        for x, y in self.base:
            press = FWidget(self, pos=(x, y), length=self.length)
            self.ptw[x, y] = press
            self.wtp[press] = (x, y)
            val = abs(x) * 10 + abs(y)
            if val not in self.base_pieces:
                self.ptc[x, y] = ''
            else:
                piece = self.base_pieces[val](self, pos=(x, y), length=self.length)
                if x < 0:
                    self.red[piece] = (x, y)
                    piece.same = True
                else:
                    self.black[piece] = (x, y)
                    piece.same = False
                self.ptc[x, y] = piece
                self.ctp[piece] = (x, y)

    def set_can(self):
        if len(self.foot) % 2 == 0:
            self.can = set(self.red.values())
        else:
            self.can = set(self.black.values())
        self.copy = self.can.copy()

    def get_exist(self, x, y):
        x, y = int(x - self.center), int(y - self.center)
        k, v = x % self.diam, y % self.diam
        # print([(x - k - self.length, y - v),
        #        (x - k + self.length + self.diam, y - v),
        #        (x - k - self.length, y - v + self.diam),
        #        (x - k + self.length + self.diam, y - v + self.diam)])
        for c, t in [(k, v), (k - self.diam, v), (k, v - self.diam), (k - self.diam, v - self.diam)]:
            if c ** 2 + t ** 2 <= self.area:
                return x - self.length - c, y - t

    def retreat(self):
        point_b, before, point_a, after = self.foot.pop()
        print(point_b, before, point_a, after)
        before.move(*point_b)
        self.ptc[point_b] = before
        self.ctp[before] = point_b
        if before.same:
            self.red[before] = point_b
            temp = self.black
        else:
            self.black[before] = point_b
            temp = self.red
        if after:
            self.ptc[point_a] = after
            self.ctp[after] = point_a
            temp[after] = point_a
        else:
            self.ptc[point_a] = ''
        for i in [self.first, self.one]:
            if hasattr(i, 'animation'):
                i.animation.stop()
                i.opacity.setOpacity(0)
        self.first = self.one = None
        self.set_can()
        pass

    def right_button(self, event):
        # print('right')
        # print([self.one, self.first, self.two, self.second])
        if hasattr(self.first, 'animation'):
            self.first.animation.stop()
            self.first.opacity.setOpacity(0)
            self.first = self.one = None
        self.can = self.copy.copy()
        pass

    def left_button(self, event):
        # print('left', self.first)
        x, y = event.pos().toTuple()
        temp = self.get_exist(x, y)
        if temp not in self.can:
            return
        x, y = temp
        if not self.first:
            self.first = self.ptc[x, y]
            self.first.check()
            self.one.animation.stop()
            self.one.opacity.setOpacity(1)
            self.first, self.one = self.one, None
        else:
            self.first.opacity.setOpacity(0)
            point = self.wtp[self.first]
            cur = self.ptc.get((x, y), None)
            temp = self.ptc.get(point, None)
            self.foot.append((point, temp, (x, y), cur))
            self.ptc[(x, y)], self.ctp[temp] = temp, (x, y)
            self.ptc[point] = ''
            temp.move(x, y)
            if temp.same:
                self.red[temp] = (x, y)
                temp = self.black
            else:
                self.black[temp] = (x, y)
                temp = self.red
            if cur:
                temp.pop(cur)
                self.ctp[cur] = ''
                cur.close()
            self.one.animation.stop()
            self.one.opacity.setOpacity(0)
            self.first, self.one = None, None
            self.set_can()
            pass

    def mouseMoveEvent(self, event):
        x, y = event.pos().toTuple()
        temp = self.get_exist(x, y)
        if temp not in self.can:
            # if hasattr(self.one, 'animation') and self.wtp.get(self.one, None) != self.ctp.get(self.first, None):
            if hasattr(self.one, 'animation'):
                self.one.animation.stop()
                self.one.opacity.setOpacity(0)
            return
        x, y = temp
        temp = self.ptw[x, y]
        if temp != self.one:
            if hasattr(self.one, 'animation'):
                self.one.animation.stop()
                self.one.opacity.setOpacity(0)
            self.one = temp
        self.one.animation.start()
        pass

    def mousePressEvent(self, event):
        # print(dir(event))
        # x, y = event.pos().toTuple()
        # temp = self.get_exist(x, y)
        # if not (temp and temp in self.can):
        #     return
        # x, y = temp
        # if not self.second:
        #     self.first = self.ptc[x, y]
        #     self.first.check()
        #     self.one.animation.stop()
        #     self.one.opacity.setOpacity(1)
        self.mouse.get(event.button(), self.right_button)(event)
