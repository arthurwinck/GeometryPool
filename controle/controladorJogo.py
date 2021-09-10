import pygame as py
import pymunk

#imports dos modelos
from interface.telaMesa import TelaMesa

#imports das bolas
from modelo.bola import Bola
from modelo.bolaPontos import BolaPontos

#Esse deveria ser ControladorJogo, já que inicializa os objetos Pygame
class ControladorJogo():
    def __init__(self):
        #criação das variáveis utilizadas dentro do pygame
        py.init()
        self.tela = py.display
        self.clock = py.time.Clock()
        self.fps = 60
        self.space = pymunk.Space()

        self.configurar_tela()
        self.iniciar_jogo()
        
    def configurar_tela(self):

        azul = (82,91,247)

        self.tela.set_caption('Geometry Pool')
        self.superficie = self.tela.set_mode((1280,720))
        self.superficie.fill(azul)
        self.tela.update()
        
    def iniciar_jogo(self):
        #Instanciar os objetos necessários para o início do jogo
        self.telaMesa = TelaMesa(self.superficie)
        #instanciando uma bola branca
        self.bola1 = Bola(200, 200, 20, (255,255,255))
        #instanciando uma bola vermelha 
        self.bola2 = BolaPontos(250, 200, 0, (255,0,0), 5)

        #criando o espaço físico da simulação, e adicionando as bolas nele
        self.space.add(self.bola1.corpo, self.bola1.forma)
        self.space.add(self.bola2.corpo, self.bola2.forma)

        #Loop do jogo -- talvez tenha que estar na verdade na classe Mesa
        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()

            self.superficie.fill((82,91,247))
            self.telaMesa.desenharMesa()
            self.telaMesa.desenharBolas([self.bola1, self.bola2])

            self.tela.update()
            self.clock.tick(self.fps)
            self.space.step(1/self.fps)



  

