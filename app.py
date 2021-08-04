import sys
from PyQt5.QtWidgets import QApplication

from interface.controladorInterface import ControladorInterface

app = QApplication(sys.argv)
main = ControladorInterface()
app.exec_()