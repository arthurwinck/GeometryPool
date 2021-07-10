from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow

class EscolhaMesa(QMainWindow):
    def __init__(self, widget):
        super(EscolhaMesa, self).__init__()
        self.widget = widget
        loadUi("gui/escolha_mesa.ui", self)
        #self.EMbuttonComecar.clicked.connect(comecarJogo)
        self.EMbuttonVoltar.clicked.connect(self.voltar)

    def voltar(self):
        self.widget.setCurrentIndex(0)
