from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow

class EscolhaJogador(QMainWindow):
    def __init__(self, widget):
        super(EscolhaJogador, self).__init__()
        self.widget = widget
        loadUi("interface/gui/escolha_jogador.ui", self)
        self.EJbuttonContinuar.clicked.connect(self.goto_escolha_mesa)
        self.EJbuttonVoltar.clicked.connect(self.voltar)

    def voltar(self):
        self.widget.setCurrentIndex(0)

    def goto_escolha_mesa(self):
        self.widget.setCurrentIndex(2)

