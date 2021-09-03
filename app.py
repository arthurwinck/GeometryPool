import sys
from PyQt5.QtWidgets import QApplication

from controle.controladorInterface import ControladorInterface

app = QApplication(sys.argv)
main = ControladorInterface()
app.exec_()