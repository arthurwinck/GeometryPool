import pygame as py
import pymunk

from .bola import Bola

class BolaPontos(Bola):
    def __init__(self, x,y, velocidade, cor, valor):
        super().__init__(x, y, velocidade, cor)
        self.valor = valor

    def getValor(self):
        return self.valor
    