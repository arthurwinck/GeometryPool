import sys
from PyQt5.QtWidgets import QApplication

from mainWindow import MainWindow

app = QApplication(sys.argv)
main = MainWindow()
app.exec_()