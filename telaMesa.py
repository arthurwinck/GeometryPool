from pygame.sprite import Sprite
import pygame as py

class TelaMesa(Sprite):
    def __init__(self, superficie):
        super().__init__()
        self.superficie = superficie
        self.desenhar_mesa()

    def desenhar_mesa(self):
        X = 1280
        Y = 720
        
        tamX = 1000
        tamY = 500


        tamPos = ((X - tamX)/2,(Y - tamY)/2, tamX, tamY)
        green = (34, 161, 65)

        py.draw.rect(self.superficie, green, tamPos)
        
        for i in range(3):
            for j in range(2):
                py.draw.circle(self.superficie, green, ((X - tamX)/2 + (tamX/2)*i, (Y - tamY)/2 + (tamY)*j), 25)

        self.rect = ((X - tamX)/2,(Y - tamY)/2, tamX, tamY)