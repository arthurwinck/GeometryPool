import pygame as py
from time import sleep

from mesa import Mesa

class TelaJogo():
    def __init__(self):

        azul = (82,91,247)

        screen = py.display
        screen.set_caption('Geometry Pool')
        surface = screen.set_mode((1280,720))
        surface.fill(azul)
        screen.update()
        mesa = Mesa(surface)
        screen.update()




