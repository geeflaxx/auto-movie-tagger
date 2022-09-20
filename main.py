
#import functions

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from main_window import Ui_Dialog

class MyMainWindow(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())
