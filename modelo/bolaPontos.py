import pygame as py
import pymunk

from .bola import Bola

class BolaPontos(Bola):
    def __init__(self, x,y, velocidade,superficie, valor):
        super.__init__(self, x, y, velocidade, superficie)
        self.valor = valor

    def getValor(self):
        return self.valor
    