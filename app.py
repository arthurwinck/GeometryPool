import sys
from PyQt5.QtWidgets import QApplication

from controle.controlador import Controlador

app = QApplication(sys.argv)
main = Controlador()
app.exec_()