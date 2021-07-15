from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QDialog, QWidget
from PyQt5.Qt import pyqtSignal

class TelaInicial(QMainWindow):
    sinalSair = pyqtSignal()

    def __init__(self, widget):
        super(TelaInicial, self).__init__()
        self.widget = widget
        loadUi("gui/main.ui", self)
        
        #botões da UI
        self.buttonComecar.clicked.connect(self.goto_escolha_jogador)
        self.buttonRanking.clicked.connect(self.goto_ranking)
        self.buttonSair.clicked.connect(self.sair)

    def goto_escolha_jogador(self):
        self.widget.setCurrentIndex(1)

    def goto_ranking(self):
        self.widget.setCurrentIndex(3)

    def sair(self):
        self.sinalSair.emit()
