import pygame as py
import pymunk

class Bola():
    def __init__(self, x,y, velocidade, cor):
        self.corpo = pymunk.Body(1,1)   
        self.corpo.position = (x,y)
        self.forma = pymunk.Circle(self.corpo, 15)
        self.corpo.velocity = velocidade,0
        self.cor = cor

    def aplicar_atrito(self):
        #TODO - ATUALIZAR DIAGRAMA COM NOVO MÉTODO
        atrito = 0.1
        if self.corpo.velocity.x > 0 and self.corpo.velocity.y > 0:
            self.corpo.velocity = (self.corpo.velocity.x - atrito), (self.corpo.velocity.y - atrito)
        elif self.corpo.velocity.x > 0 and self.corpo.velocity.y < 0:
            self.corpo.velocity = (self.corpo.velocity.x - atrito), (self.corpo.velocity.y + atrito)
        elif self.corpo.velocity.x < 0 and self.corpo.velocity.y < 0:
            self.corpo.velocity = (self.corpo.velocity.x + atrito), (self.corpo.velocity.y + atrito)

    def getVelocidade(self):
        return self.corpo.velocity

    def getPosicao(self):
        return self.corpo.position

    def getBody(self):
        return self.corpo
