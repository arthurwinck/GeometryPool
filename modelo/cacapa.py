import pygame as py
import pymunk

class Cacapa():
    def __init__(self, posicao, raio):
        self.posicao = posicao
        self.raio = raio
        self.bolas = []

    def obterBolas(self):
        return self.bolas
    
    #método no diagrama
    def ChecarColisao(self, bolas):
        #TODO - Consertar colisão, pois distancia (nesse caso raio da bola, precisa ser ao quadrado)
        for bola in bolas:
            distancia = (self.posicao[0] - bola.corpo.position.x)**2 + (self.posicao[1] - bola.corpo.position.y)**2

            if distancia < (bola.raio)**2 or distancia - 10 < (bola.raio)**2:
                return bola
