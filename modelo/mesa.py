from os import error
import time
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
from .ranking import Ranking
from interface.telaMesa import TelaMesa
from .jogador import Jogador

import time

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

    def iniciarJogadores(self, nomes_jogadores):

        taco1 = Taco()
        taco2 = Taco()

        jogador1 = Jogador(nomes_jogadores[0], taco1)
        jogador2 = Jogador(nomes_jogadores[1], taco2)

        self.jogadores = [jogador1, jogador2]

        self.definirOrdemJogadores()

    def definirOrdemJogadores(self):
        num = randint(0,1)

        if num == 0:
            self.setJogadorInicial(self.jogadores[0])
        else:
            self.setJogadorInicial(self.jogadores[1])

    def setJogadorInicial(self, jogador):
        jogador.setTurnoJogador()

    def obterJogadorDaVez(self):
        if self.jogadores[0].turno:
            return self.jogadores[0]
        else:
            return self.jogadores[1]

    def obterTodasCacapas(self):
        return self.cacapas

    def verificarVencedor(self):
        cacapas = self.obterTodasCacapas()
        quantidade_bolas = 0
        bola7 = True

        for cacapa in cacapas:
            bolas = cacapa.obterBolas()
            quantidade_bolas += len(bolas)

            for bola in bolas:
                valor = bola.getValor()

                if valor == 7:
                    bola7 = False

        total = self.obterTotalBolasJogo()
        #print("TOTAL = " + str(total))

        #Se só existir a bola branca na lista de bolas
        if len(total) == 1:
            jogador = self.obterJogadorMaiorPontuacao()
            jogador.definirVencedor()
            #Se existir um vencedor ele irá retornar esse jogador, se não, None
            return jogador

        else:

            #Se só existir a bola7 e a bola branca
            if bola7 == True and len(total) == 2:
                jogador = self.obterJogadorDaVez()
                falta = jogador.obterFaltaJogador()

                if falta:
                    pontos = self.obterDiferencaPontosJogadores()

                    if pontos > 7:
                        return
                    else:
                        jogador = self.obterProximoJogador()
                        jogador.definirVencedor()
                        #print("ACABOU!")
                        return jogador
                else:
                    return
            else:
                return

    def verificarJogada(self):
        jogador = self.obterJogadorDaVez()
        bolas = jogador.obterBolas()

        branca = self.verificarBolaBrancaEncacapada(bolas)
        #print('verificar jogada')

        if branca:
            jogador.setJogadaInvalida()
            #print('encacapou branca')
            jogador.adicionarPontos(-5)
            return False
        
        else:
            bolaTocada = jogador.obterBolaTocada()
            bolaVermelha = jogador.obterBolaVermelha()
            bolaNumerada = jogador.obterBolaNumerada()

            #print('bolaVermelha: ', bolaVermelha)
            #print('bolaNumerada: ', bolaNumerada)

            #if bolaTocada:
            #    print('bolaTocada: ', bolaTocada.getValor())


            if bolaTocada == None:
                jogador.setJogadaInvalida()
                #print('nao tocou nenhuma bola')
                return False

            if bolaTocada.getValor() == 1 and bolaVermelha:
                jogador.setJogadaValida()
                return True

            elif bolaTocada.getValor() != 1 and bolaNumerada:
                jogador.setJogadaValida()
                return True

            else:
                jogador.setJogadaInvalida()
                #print('encacapou erraad')
                return False

    def obterTodasCacapas(self):
        return self.cacapas

    def obterTotalBolasJogo(self):
        return self.bolas

    def verificarBolaBrancaEncacapada(self, bolas):
        for bola in bolas:
            if isinstance(bola, BolaPontos):
                continue
            else:
                return True

    def obterJogadorMaiorPontuacao(self):
        if self.jogadores[0].pontos > self.jogadores[1].pontos:
            return self.jogadores[0]
        elif self.jogadores[0].pontos > self.jogadores[1].pontos:
            return self.jogadores[1]
        else:
            #print("Os jogadores empataram")
            raise error

    def obterDiferencaPontosJogadores(self):
        return abs(self.jogadores[0].pontos - self.jogadores[1].pontos)

    def obterProximoJogador(self):
        if self.jogadores[0].turno:
            return self.jogadores[1]
        else:
            return self.jogadores[0]

    def trocarTurnoJogadores(self):
        if self.jogadores[0].turno == True:
            self.jogadores[0].passarTurno()
            self.jogadores[1].setTurnoJogador()
        else:
            self.jogadores[1].passarTurno()
            self.jogadores[0].setTurnoJogador()

    def calculaPontosJogador(self, bolas):
        pontos = 0
        for bola in bolas:
            bola_pontos = bola.getValor()
            pontos += bola_pontos

        return pontos

    def definirAnguloTaco(self, angulo):
        posicao = self.bolas[0].getPosicao()
        vec_x, vec_y = posicao[0] - angulo[0], posicao[1] - angulo[1]
        vec_len = np.sqrt(vec_x ** 2 + vec_y**2)
        vec_x, vec_y = vec_x / vec_len, vec_y / vec_len

        return (vec_x, vec_y)

    def criarBolas(self):
        #Instanciar os objetos necessários para o início do jogo
        #Bola Branca sempre será a primeira bola da lista
        bolaBranca = Bola(400, 410, 0, (255,255,255))
        self.bolas.append(bolaBranca)
        self.space.add(bolaBranca.corpo, bolaBranca.forma)

        #TODO definir posição das bolas para outros formatos

        # for i in range(0):
        #     #TODO - fazer matemática de criação de bolas (formato de triângulo)
        #     bolaVermelha = BolaPontos(i*50 + 250, i*30 + 200, 0, (255,0,0), 1)
        #     #bolaVermelha = BolaPontos(200, 200, 20, (255,0,0), 5)
        #     self.bolas.append(bolaVermelha)
        #     self.space.add(bolaVermelha.corpo, bolaVermelha.forma)
        # #criando o espaço físico da simulação, e adicionando as bolas nele

        # for i in range(1):
        #     bolaVermelha = BolaPontos(i*50 + 450, i*30 + 420, 0, (0,0,255), 7)
        #     self.bolas.append(bolaVermelha)
        #     self.space.add(bolaVermelha.corpo, bolaVermelha.forma)

        #return #FOR DEBUG
        
        #instanciando as 15 bolas vermelhas 

        posicao_inicial_x = 1000
        posicao_inicial_y = 320

        for i in range(5,0,-1):
            for j in range(1,i+1):
                bolaVermelha = BolaPontos(posicao_inicial_x + (i-5)*30, j*30 + (posicao_inicial_y-i*15), 0, (255,0,0), 1)
                #bolaVermelha = BolaPontos(200, 200, 20, (255,0,0), 5)
                self.bolas.append(bolaVermelha)
                self.space.add(bolaVermelha.corpo, bolaVermelha.forma)
            #criando o espaço físico da simulação, e adicionando as bolas nele

        # #Bola 7
        # bola7 = BolaPontos(posicao_inicial_x + 30, (posicao_inicial_y+15), 0, (0,0,0), 7)
        # self.bolas.append(bola7)
        # self.space.add(bola7.corpo, bola7.forma)
        self.colocarBola7()

        #Bola 6
        bola6 = BolaPontos(posicao_inicial_x + -250, (posicao_inicial_y+15), 0, (255,100,180), 6)
        self.bolas.append(bola6)
        self.space.add(bola6.corpo, bola6.forma)

        #Bola 5
        bola6 = BolaPontos(posicao_inicial_x + -350, (posicao_inicial_y+15), 0, (0,0,255), 5)
        self.bolas.append(bola6)
        self.space.add(bola6.corpo, bola6.forma)

        #Bola 4
        bola4 = BolaPontos(400, 200 , 0, (0,255,0), 4)
        self.bolas.append(bola4)
        self.space.add(bola4.corpo, bola4.forma)

        #Bola 3
        bola3 = BolaPontos(400, 340 , 0, (100,50,0), 3)
        self.bolas.append(bola3)
        self.space.add(bola3.corpo, bola3.forma)

        #Bola 2
        bola2 = BolaPontos(400, 480 , 0, (255,255,0), 2)
        self.bolas.append(bola2)
        self.space.add(bola2.corpo, bola2.forma)

    def colocarBola7(self):
        #Bola 7
        bola7 = BolaPontos(1000 + 30, (320+15), 0, (0,0,0), 7)
        self.bolas.append(bola7)
        self.space.add(bola7.corpo, bola7.forma)


    def criarBordas(self, formato_mesa):
        #instanciar os limites da mesa
        #Bordas da mesa, x0,y0 (esquerdo inferior); x1,y0 (direito inferior); x0,y1 (esquerdo superior) e x1,y1 (direito superior)
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

    def inicializar(self, configuracoes_jogo):

        self.criarBolas()
        self.criarCacapas(configuracoes_jogo[1])
        self.criarBordas(configuracoes_jogo[0])

        self.desenhar()
        ranking = Ranking("ranking.json")
        jogador = self.obterJogadorVencedor()
        ranking.inserir_jogador_ranking(jogador.nome, jogador.pontos)
        py.quit()


    def desenhar(self):

        texto_jogadores = self.telaMesa.desenharJogadores(self.jogadores)

        textRect1 = texto_jogadores[0].get_rect()
        textRect2 = texto_jogadores[1].get_rect()


        x = 600
        y = 400

        textRect1.center = (x/2,y/2)
        textRect2.center = (x/2,y/2)


        #taco = Taco()

        clicking = False
        movimento = False
        jogada = False

        #Loop do jogo -- talvez tenha que estar na verdade na classe Mesa
        while True:

            jogador = self.obterJogadorDaVez()
            taco = jogador.obterTaco()

            bola = self.bolas[0].checarColisao(self.bolas)
            
            if bola != None:
                #print('TOCOU!!!!', jogador.nome)
                jogador.salvarBolaTocadaJogador(bola)

            for cacapa in self.cacapas:
                bola_colisao = cacapa.ChecarColisao(self.bolas)

                if bola_colisao != None:

                    jogador.bolas.append(bola_colisao)
                    #print('removeu bolas')
                
                    if isinstance(bola_colisao, BolaPontos):
                        jogador.setFezPontos()
                        self.bolas.remove(bola_colisao)
                        for i in self.bolas:
                            if len(self.bolas) == 1:
                                break
                            elif bola_colisao.getValor() == 7:
                                self.colocarBola7()
                    else:
                        self.bolas[0].corpo.position = 400, 200
                        self.bolas[0].corpo.velocity = 0, 0

            algum_movimento = any([bola.aplicarAtrito() for bola in self.bolas])

            if algum_movimento:
                movimento = True
                jogada = True
            else:
                movimento = False

            if (not clicking):
                mx, my = py.mouse.get_pos()
                vetorTaco = self.definirAnguloTaco((mx,my))

            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()
                if event.type == py.MOUSEBUTTONDOWN and movimento == False:
                    clicking = True
                if event.type == py.MOUSEBUTTONUP and movimento == False:
                    impulso_bola = taco.getForca(vetorTaco[0], vetorTaco[1])

                    # TODO: adicionar metodo na bola branca para impulso
                    self.bolas[0].aplicarImpulso(impulso_bola)
                    taco.reset()
                    clicking = False

            if clicking and movimento == False:
                taco.aumentarForca()

            self.telaMesa.superficie.fill((82,91,247))
            self.telaMesa.desenharMesa()
            self.telaMesa.desenharBolas(self.bolas)
            self.telaMesa.desenharLimites(self.limites)
            self.telaMesa.desenharJogadores(self.jogadores)

            #Parada no movimento causa possibilidade de realizar jogada
            
            if movimento == False:
                bola_x, bola_y = self.bolas[0].getPosicao()
                self.telaMesa.desenharTaco(taco, vetorTaco[0], vetorTaco[1], bola_x, bola_y)
                
                if jogada == True:
                    jogada = False

                    
                    jogadaValida = self.verificarJogada()
                    #print('checou jogada')

                    if jogadaValida:
                        fezPontos = jogador.obterFezPontos()

                        if fezPontos:
                            bolas = jogador.obterBolas()
                            pontos = self.calculaPontosJogador(bolas)
                            jogador.adicionarPontos(pontos)
                            #print(f'jogador recebeu {pontos} pontos')

                            jogador.inverteBolaVermelha()
                            jogador.inverteBolaNumerada()

                        else:
                            #print('trocou nao fez pontos')
                            self.trocarTurnoJogadores()
                    
                    else:
                        bola = jogador.obterBolaTocada()
                        if bola:
                            pontos = self.calculaPontosJogador([bola])
                            jogador2 = self.obterProximoJogador()
                            jogador2.adicionarPontos(pontos)
                            #print(f'adicionou {pontos} oponente')

                        self.trocarTurnoJogadores()
                        #print('trocou jogada invalida')

                    vencedor = self.verificarVencedor()

                    #TODO - Criar texto na tela notificando a vitória do Jogador
                    if vencedor != None:
                        self.telaMesa.notificarFinal(jogador)
                        self.tela.update()
                        time.sleep(4)
                        break

                    
                    #Obtenho o "próximo" jogador toda vez que o movimento se encerra (?)
                           
        
            self.tela.update()
            self.clock.tick(self.fps)
            self.space.step(1/self.fps)

    def obterJogadorVencedor(self):
        if (self.jogadores[0].vencedor):
            return self.jogadores[0]
        if (self.jogadores[1].vencedor):
            return self.jogadores[1]