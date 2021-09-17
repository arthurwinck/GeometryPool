import pygame as py
import pymunk

#imports dos modelos
from .bola import Bola
from .bolaPontos import BolaPontos
from .borda import Borda
from .cacapa import Cacapa
from interface.telaMesa import TelaMesa
from .jogador import Jogador

class Mesa:
    def __init__(self):
        py.init()
        self.bolas = []
        
        self.tela = py.display
        self.tela.set_caption('Geometry Pool')

        self.telaMesa = TelaMesa(self.tela)
        self.clock = py.time.Clock()
        self.space = pymunk.Space()

        #self.space.gravity = 20,20
        self.criarBolas()

    def iniciarJogadores(self, nomes_jogadores):
        pass

    def criarBolas(self):
        #Instanciar os objetos necessários para o início do jogo
        #Bola Branca sempre será a primeira bola da lista
        bolaBranca = Bola(200, 200, 20, (255,255,255))
        self.bolas.append(bolaBranca)
        self.space.add(bolaBranca.corpo, bolaBranca.forma)
        
        #instanciando as 15 bolas vermelhas 
        #TODO - Instanciar as bolas de outras cores 

        for i in range(10):
            #TODO - fazer matemática de criação de bolas (formato de triângulo)
            bolaVermelha = BolaPontos(i*20 + 150, i*30 + 120, 0, (255,0,0), 5)
            #bolaVermelha = BolaPontos(200, 200, 20, (255,0,0), 5)
            self.bolas.append(bolaVermelha)
            self.space.add(bolaVermelha.corpo, bolaVermelha.forma)
        #criando o espaço físico da simulação, e adicionando as bolas nele

    #TODO - ATUALIZAR DIAGRAMA
    def criarBordas(self, formato_mesa):
        #instanciar os limites da mesa
        #Bordas da mesa, x0,y0 (esquerdo inferior); x1,y0 (direito inferior); x0,y1 (esquerdo superior) e x1,y1 (direito superior)
        #TODO - PROVAVELMENTE TERÁ QUE SER UM MÉTODO POR SI SÓ
        x0 = self.telaMesa.tamPos[0]
        y0 = self.telaMesa.tamPos[1]
        x1 = x0 + self.telaMesa.tamX
        y1 = y0 + self.telaMesa.tamY

        borda1 = Borda([(x0+24,y0), ((x0+x1)/2-20,y0)])
        borda2 = Borda([((x0+x1)/2+20,y0), (x1-24,y0)])
        borda3 = Borda([(x0,y0+22), (x0,y1-22)])
        borda4 = Borda([(x0+24,y1-5), ((x0+x1)/2-20,y1-5)])
        borda5 = Borda([((x0+x1)/2+20,y1-5), (x1-24,y1-5)])
        borda6 = Borda([(x1-5,y0+22), (x1-5,y1-22)])

        self.limites = [borda1, borda2, borda3, borda4, borda5, borda6]
        for borda in self.limites:
            self.space.add(borda.corpo, borda.forma)

    def criarCacapas(self, numero_cacapas):

        for i in range(3):
            for j in range(2):
                #Argumento é a posição das cacapas
                Cacapa(((self.telaMesa.telaX - self.telaMesa.tamX)/2 + (self.telaMesa.tamX/2)*i, (self.telaMesa.telaY - self.telaMesa.tamY)/2 + (self.telaMesa.tamY)*j), 20)

    #TODO - ATUALIZAR DIAGRAMA
    def inicializar(self, configuracoes_jogo):

        self.criarCacapas(configuracoes_jogo[1])
        self.criarBordas(configuracoes_jogo[0])

        #Loop do jogo -- talvez tenha que estar na verdade na classe Mesa
        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()

            self.telaMesa.desenharMesa()
            
            for bola in self.bolas:
                movimento = bola.aplicar_atrito()

            self.telaMesa.desenharBolas(self.bolas)
            self.telaMesa.desenharLimites(self.limites)

            self.tela.update()
            self.clock.tick(60)
            self.space.step(1/60)

