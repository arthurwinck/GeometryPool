import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget, QMainWindow

from escolhaJogador import EscolhaJogador
from escolhaMesa import EscolhaMesa
from ranking import Ranking

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("gui/main.ui", self)

        self.gerarTelas()
        self.gerarWidgets()

        self.buttonComecar.clicked.connect(self.goto_escolha_jogador)
        self.buttonRanking.clicked.connect(self.goto_ranking)
        self.buttonSair.clicked.connect(self.sair)

    def gerarTelas(self):
        
        self.widget = QtWidgets.QStackedWidget()
        self.widget.addWidget(self)
        self.widget.setFixedHeight(600)
        self.widget.setFixedWidth(815)

        self.escolha_mesa = EscolhaMesa(self.widget)
        self.ranking = Ranking(self.widget)
        self.escolha_jogador = EscolhaJogador(self.widget)

        self.widget.show()
        

    def gerarWidgets(self):
        self.widget.addWidget(self.escolha_jogador)
        self.widget.addWidget(self.escolha_mesa)
        self.widget.addWidget(self.ranking)

    def sair(self):
        self.close()
        sys.exit()

    def goto_escolha_jogador(self):
        self.widget.setCurrentIndex(1)

    def goto_ranking(self):
        self.widget.setCurrentIndex(3)
