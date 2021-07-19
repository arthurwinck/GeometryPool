import pygame as py
from time import sleep

from telaMesa import TelaMesa

class TelaJogo():
    def __init__(self):
        self.tela = py.display

        self.configurar_tela()
        self.adicionar_mesa()
        
    def configurar_tela(self):

        azul = (82,91,247)
        verde = ()

        self.tela.set_caption('Geometry Pool')
        self.superficie = self.tela.set_mode((1280,720))
        self.superficie.fill(azul)
        self.tela.update()
        
    def adicionar_mesa(self):
        self.mesa = TelaMesa(self.superficie)
        self.tela.update()




