from PySide6.QtGui import QIcon, QImage
from PySide6.QtCore import Qt, QThread
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

import sys


class LearnQLabel(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(640,480)
        self.btn = QPushButton(self)


if __name__ == '__main__':
    print(sys.argv)
    app = QApplication(sys.argv)
    ui = LearnQLabel()
    ui.show()
    sys.exit(app.exec())
