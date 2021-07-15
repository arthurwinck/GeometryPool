import sys
import PyQt5
from PyQt5.QtCore import QObject
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget, QMainWindow
from PyQt5.Qt import pyqtSignal

from escolhaJogador import EscolhaJogador
from escolhaMesa import EscolhaMesa
from ranking import Ranking
from telaInicial import TelaInicial
from telaJogo import TelaJogo

class MainWindow(QObject):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.widget = QtWidgets.QStackedWidget()

        self.gerarTelas()
        self.gerarWidgets()
        self.mostrarTela()
        self.gerarSinais()
        
    def gerarTelas(self):
        self.tela_inicial = TelaInicial(self.widget)
        self.escolha_jogador = EscolhaJogador(self.widget)
        self.escolha_mesa = EscolhaMesa(self.widget)
        self.ranking = Ranking(self.widget)
        
    def gerarWidgets(self):
        self.widget.addWidget(self.tela_inicial)
        self.widget.addWidget(self.escolha_jogador)
        self.widget.addWidget(self.escolha_mesa)
        self.widget.addWidget(self.ranking)

    def mostrarTela(self):
        self.widget.setFixedHeight(600)
        self.widget.setFixedWidth(815)
        self.widget.show()

    def gerarSinais(self):
        self.escolha_mesa.sinalIniciar.connect(self.iniciarJogo)
        self.tela_inicial.sinalSair.connect(self.sair)
            
    def iniciarJogo(self):
        jogo = TelaJogo()
        print("jogo iniciou!")

        #método para iniciar a execução do pygame

    def sair(self):
        self.close()
        
