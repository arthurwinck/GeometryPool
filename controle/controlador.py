#imports de biblioteca
from PyQt5.QtCore import QObject
from PyQt5 import QtWidgets

#imports das classes de interface utilizadas
from interface.escolhaJogador import EscolhaJogador
from interface.escolhaMesa import EscolhaMesa
from interface.ranking import Ranking
from interface.telaInicial import TelaInicial

#import dos modelos
from modelo.mesa import Mesa


class Controlador(QObject):
    #Criação do widget, que será o display de todas as telas, além disso realizar os outros métodos
    def __init__(self):
        super(Controlador, self).__init__()
        self.widget = QtWidgets.QStackedWidget()

        self.gerar_telas()
        self.gerar_widgets()
        self.mostrar_tela()
        self.gerar_sinais()
    
    #Criar as classes que possuem os layouts das telas
    def gerar_telas(self):
        self.tela_inicial = TelaInicial(self.widget)
        self.escolha_jogador = EscolhaJogador(self.widget)
        self.escolha_mesa = EscolhaMesa(self.widget)
        self.ranking = Ranking(self.widget)
        
    #Adicionar essas telas ao widget principal
    def gerar_widgets(self):
        self.widget.addWidget(self.tela_inicial)
        self.widget.addWidget(self.escolha_jogador)
        self.widget.addWidget(self.escolha_mesa)
        self.widget.addWidget(self.ranking)

    #Definir tamanho e mostrar a tela
    def mostrar_tela(self):
        self.widget.setFixedHeight(600)
        self.widget.setFixedWidth(815)
        self.widget.show()

    #Conectar os botões do layout com as funções
    def gerar_sinais(self):
        self.escolha_mesa.sinal_iniciar.connect(self.iniciarJogo)
        self.tela_inicial.sinal_sair.connect(self.sair)
            
    #Ao apertar o botão de começar no layout de escolha de mesa, inicia-se o jogo (pygame)
    def iniciarJogo(self):
        nomeJogador1 = self.escolha_jogador.EJNomeJogador1.text()
        nomeJogador2 = self.escolha_jogador.EJNomeJogador2.text()

        nomes_jogadores = [nomeJogador1, nomeJogador2]
        
        formatoMesa = self.escolha_mesa.formatoMesa
        numeroCacapa = self.escolha_mesa.numeroCacapa

        configuracoes_jogo = [formatoMesa, numeroCacapa]

        self.mesa = Mesa()
        self.mesa.iniciarJogadores(nomes_jogadores)
        self.mesa.inicializar(configuracoes_jogo)
        self.widget.setCurrentIndex(0)

    #Ao sair do jogo, encerra-se a execução
    def sair(self):
        exit(0)
        
