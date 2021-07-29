import sys
from PyQt5.QtWidgets import QApplication

from interfaceSistema import InterfaceSistema

app = QApplication(sys.argv)
main = InterfaceSistema()
app.exec_()