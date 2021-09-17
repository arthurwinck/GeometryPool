import pygame as py
import numpy as np
import pymunk

#imports dos modelos
from interface.telaMesa import TelaMesa

#imports das bolas
from modelo.bola import Bola
from modelo.bolaPontos import BolaPontos
from modelo.taco import Taco

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
    

    #No diagrama a responsabilidade de instanciar bola e cacapa é da Mesa
    #Instanciar a Mesa aqui, e a Mesa instancia o resto (bola e caçapa)
    def iniciar_jogo(self):
        #Instanciar os objetos necessários para o início do jogo
        self.telaMesa = TelaMesa(self.superficie)
        #instanciando uma bola branca
        self.bola1 = Bola(200, 200, 20, (255,255,255))
        #instanciando uma bola vermelha 
        self.bola2 = BolaPontos(500, 200, 0, (255,0,0), 5)

        #criando o espaço físico da simulação, e adicionando as bolas nele
        self.space.add(self.bola1.corpo, self.bola1.forma)
        self.space.add(self.bola2.corpo, self.bola2.forma)

        taco = Taco()
        clicking = False

        #Loop do jogo -- talvez tenha que estar na verdade na classe Mesa
        while True:
            mx, my = py.mouse.get_pos()
            bola_x, bola_y = self.bola1.getPosicao()

            # linalg stuff, talvez separar em outro lugar?
            vec_x, vec_y = bola_x - mx, bola_y - my
            vec_len = np.sqrt(vec_x ** 2 + vec_y**2)
            vec_x, vec_y = vec_x / vec_len, vec_y / vec_len

            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()
                if event.type == py.MOUSEBUTTONDOWN:
                    clicking = True
                if event.type == py.MOUSEBUTTONUP:
                    impulso_bola = taco.getForca(vec_x, vec_y)

                    # TODO: adicionar metodo na bola branca para impulso
                    self.bola1.corpo.apply_force_at_local_point(impulso_bola)

                    taco.reset()
                    clicking = False

            if clicking:
                taco.aumentarForca()

            self.superficie.fill((82,91,247))
            self.telaMesa.desenharMesa()
            self.telaMesa.desenharBolas([self.bola1, self.bola2])
            self.telaMesa.desenharTaco(taco, vec_x, vec_y, bola_x, bola_y)
            self.tela.update()
            self.clock.tick(self.fps)
            self.space.step(1/self.fps)



  

