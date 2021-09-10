import pygame as py
import pymunk

def converter_coord(coord):
    return float(coord[0]), float(720-coord[1])

class Bola():
    def __init__(self, x,y, velocidade,superificie):
        self.superficie = superificie
        self.corpo = pymunk.Body(1,1)   
        self.corpo.position = (x,y)
        self.forma = pymunk.Circle(self.corpo, 15)
        self.corpo.velocity = velocidade,0

