import pygame as py
import pymunk

class Borda():
    def __init__(self, pontos):
        self.corpo = pymunk.Body(body_type=pymunk.Body.STATIC)  
        self.pontos = pontos
        self.forma = pymunk.Poly(self.corpo, pontos)
        self.forma.elasticity = 0.5

    def getPosicao(self):
        return self.pontos
