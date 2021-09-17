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
    def colisao(self):
        pass