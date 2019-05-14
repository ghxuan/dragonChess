import sys
from PySide2.QtWidgets import QApplication
from customControls.chessWidget import ChessWidget


def main():
    app = QApplication(sys.argv)
    label = ChessWidget()
    label.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
