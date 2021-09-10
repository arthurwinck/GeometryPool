import pygame as py
import pymunk

from bola import Bola

class BolaBranca(Bola):
    def __init__(self, x,y, velocidade,superficie):
        super.__init__(self, x, y, velocidade, superficie)

    def colisao(self):
        #TODO - colisão retornaria a Bola em que a bola branca colidiu? 
        # O objeto BolaBranca não sabe com quem colidiu
        pass

    