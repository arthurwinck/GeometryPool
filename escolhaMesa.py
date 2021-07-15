from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow
from PyQt5.Qt import pyqtSignal
class EscolhaMesa(QMainWindow):
    sinalIniciar = pyqtSignal()

    def __init__(self, widget):
        super(EscolhaMesa, self).__init__()
        self.widget = widget
        loadUi("gui/escolha_mesa.ui", self)
        
        self.EMbuttonVoltar.clicked.connect(self.voltar)
        self.EMbuttonComecar.clicked.connect(self.iniciarJogo)

    def voltar(self):
        self.widget.setCurrentIndex(0)

    def iniciarJogo(self):
        self.sinalIniciar.emit()
