import pygame as py
import pymunk

def converter_coord(coord):
    return float(coord[0]), float(720-coord[1])

class TelaBola():
    def __init__(self, x,y, velocidade,superificie):
        self.superficie = superificie
        self.corpo = pymunk.Body(1,1)   
        self.corpo.position = (x,y)
        self.forma = pymunk.Circle(self.corpo, 15)
        self.corpo.velocity = velocidade,0

    def atualizar_pos(self):
        pos_x = int(self.corpo.position.x)
        pos_y = int(self.corpo.position.y)
        print(self.corpo.position.x)
        print(self.corpo.position.y)
        if self.corpo.velocity.x > 0:
            self.corpo.velocity = self.corpo.velocity.x - 0.1, 0


        py.draw.circle(self.superficie, (255,0,0), (pos_x,pos_y), 15)   
        #py.draw.circle(self.superficie, (255,0,0), (self.a,self.a), 15)
             
        





    