import pygame as py
import numpy as np
import pymunk
from random import randint

#imports dos modelos
from .bola import Bola
from .bolaPontos import BolaPontos
from .borda import Borda
from .cacapa import Cacapa
from .taco import Taco
from interface.telaMesa import TelaMesa
from .jogador import Jogador

class Mesa:
    def __init__(self):
        py.init()
        self.bolas = []
        self.cacapas = []
        
        self.tela = py.display
        self.tela.set_caption('Geometry Pool')
        self.fps = 60

        self.jogadores = []
        
        self.telaMesa = TelaMesa(self.tela)
        self.clock = py.time.Clock()
        self.space = pymunk.Space()

        #self.space.gravity = 20,20
        self.criarBolas()

    def iniciarJogadores(self, nomes_jogadores):
        jogador1 = Jogador(nomes_jogadores[0])
        jogador2 = Jogador(nomes_jogadores[1])

        self.jogadores = [jogador1, jogador2]

    def definirOrdemJogadores(self):
        num = randint(0,1)

        if num == 0:
            self.setJogadorInicial(self.jogadores[0])
        else:
            self.setJogadorInicial(self.jogadores[1])

    def setJogadorInicial(self, jogador):
        jogador.setTurnoJogador()

    def ObterJogadorDaVez(self):
        if self.jogadores[0].turno:
            return self.jogadores[0]
        else:
            return self.jogadores[1]

    def criarBolas(self):
        #Instanciar os objetos necessários para o início do jogo
        #Bola Branca sempre será a primeira bola da lista
        bolaBranca = Bola(400, 200, 20, (255,255,255))
        self.bolas.append(bolaBranca)
        self.space.add(bolaBranca.corpo, bolaBranca.forma)
        
        #instanciando as 15 bolas vermelhas 
        #TODO - Instanciar as bolas de outras cores 

        for i in range(10):
            #TODO - fazer matemática de criação de bolas (formato de triângulo)
            bolaVermelha = BolaPontos(i*50 + 150, i*30 + 120, 0, (255,0,0), 5)
            #bolaVermelha = BolaPontos(200, 200, 20, (255,0,0), 5)
            self.bolas.append(bolaVermelha)
            self.space.add(bolaVermelha.corpo, bolaVermelha.forma)
        #criando o espaço físico da simulação, e adicionando as bolas nele

    #TODO - ATUALIZAR DIAGRAMA
    def inicializar(self, configuracoes_jogo):

        self.criarCacapas(configuracoes_jogo[1])
        self.criarBordas(configuracoes_jogo[0])
        texto_jogadores = self.telaMesa.desenharJogadores(self.jogadores)

        textRect1 = texto_jogadores[0].get_rect()
        textRect2 = texto_jogadores[1].get_rect()


        x = 600
        y = 400

        textRect1.center = (x/2,y/2)
        textRect2.center = (x/2,y/2)


        #Loop do jogo -- talvez tenha que estar na verdade na classe Mesa
        taco = Taco()
        clicking = False

        #Loop do jogo -- talvez tenha que estar na verdade na classe Mesa
        while True:

            for cacapa in self.cacapas:
                bola_colisao = cacapa.ChecarColisao(self.bolas)

                if bola_colisao != None:
                
                    if isinstance(bola_colisao, BolaPontos):
                        jogador = self.ObterJogadorDaVez()
                        jogador.bolas.append(bola_colisao)
                        self.bolas.remove(bola_colisao)
                        jogador.AdicionarPontos(bola_colisao.getValor())

                    else:
                        #TODO - Implementar lógica quando a bola branca é encaçapada
                        print("Você encaçapou a bola branca")

            movimento = False

            for bola in self.bolas:
                mov = bola.aplicarAtrito()
                if mov == True:
                    movimento = True
                

            mx, my = py.mouse.get_pos()
            bola_x, bola_y = self.bolas[0].getPosicao()

            # linalg stuff, talvez separar em outro lugar?
            vec_x, vec_y = bola_x - mx, bola_y - my
            vec_len = np.sqrt(vec_x ** 2 + vec_y**2)
            vec_x, vec_y = vec_x / vec_len, vec_y / vec_len

            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()
                if event.type == py.MOUSEBUTTONDOWN and movimento == False:
                    clicking = True
                if event.type == py.MOUSEBUTTONUP and movimento == False:
                    impulso_bola = taco.getForca(vec_x, vec_y)

                    # TODO: adicionar metodo na bola branca para impulso
                    self.bolas[0].corpo.apply_force_at_local_point(impulso_bola)

                    taco.reset()
                    clicking = False

            if clicking and movimento == False:
                taco.aumentarForca()

            self.telaMesa.superficie.fill((82,91,247))
            self.telaMesa.desenharMesa()
            self.telaMesa.desenharBolas(self.bolas)
            self.telaMesa.desenharLimites(self.limites)
            self.telaMesa.superficie.blit(texto_jogadores[0], textRect1)
            self.telaMesa.superficie.blit(texto_jogadores[1], textRect2)


            if movimento == False:
                self.telaMesa.desenharTaco(taco, vec_x, vec_y, bola_x, bola_y)
            
            
            self.tela.update()
            self.clock.tick(self.fps)
            self.space.step(1/self.fps)
            
            

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
                cacapa = Cacapa(((self.telaMesa.telaX - self.telaMesa.tamX)/2 + (self.telaMesa.tamX/2)*i, (self.telaMesa.telaY - self.telaMesa.tamY)/2 + (self.telaMesa.tamY)*j), 20)
                self.cacapas.append(cacapa)



