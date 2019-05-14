from PySide2.QtWidgets import QWidget


class BoardWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(BoardWidget, self).__init__(*args, **kwargs)
        if self.parent():
            self.setGeometry(self.parent().geometry())
