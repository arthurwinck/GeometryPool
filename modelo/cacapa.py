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
        for bola in bolas:
            distancia = (self.posicao[0] - bola.corpo.position.x)**2 + (self.posicao[1] - bola.corpo.position.y)**2

            if distancia + 10 < bola.raio or distancia - 10 < bola.raio:
                return bola
