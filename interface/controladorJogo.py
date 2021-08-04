import pygame as py
import pymunk

from .telaMesa import TelaMesa
from .telaBola import TelaBola

#Mudar para SistemaJogo
class ControladorJogo():
    def __init__(self):
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
        self.mesa = TelaMesa(self.superficie)
        self.bola1 = TelaBola(200, 200, 20, self.superficie)
        self.bola2 = TelaBola(250, 200, 0, self.superficie)

        self.space.add(self.bola1.corpo, self.bola1.forma)
        self.space.add(self.bola2.corpo, self.bola2.forma)
        #self.space.gravity = (0,500)

        #self.colisao = self.space.add_collision_handler()
        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()

            self.superficie.fill((82,91,247))
            self.mesa.atualizar()
            self.bola1.atualizar_pos()
            self.bola2.atualizar_pos()

            self.tela.update()
            self.clock.tick(self.fps)
            self.space.step(1/self.fps)



  

