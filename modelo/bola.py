import pygame as py
import pymunk

class Bola():
    def __init__(self, x,y, velocidade,superficie):
        self.superficie = superficie
        self.corpo = pymunk.Body(1,1)   
        self.corpo.position = (x,y)
        self.forma = pymunk.Circle(self.corpo, 15)
        self.corpo.velocity = velocidade,0

    def getVelocidade(self):
        return self.corpo.velocity

    def getPosicao(self):
        return self.corpo.posicao

    def getBody(self):
        return self.corpo
