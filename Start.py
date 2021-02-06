# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore

from interface import Ui_MainWindow
import sys

class interface(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = interface()
    window.show()
    sys.exit(app.exec_())