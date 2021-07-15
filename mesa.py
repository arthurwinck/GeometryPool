from pygame.sprite import Sprite
import pygame as py

class Mesa(Sprite):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        
        X = 1280
        Y = 720
        
        tamX = 1000
        tamY = 500


        tamPos = ((X - tamX)/2,(Y - tamY)/2, tamX, tamY)
        green = (34, 161, 65)

        py.draw.rect(self.surface, green, tamPos)
        
        for i in range(3):
            for j in range(2):
                py.draw.circle(self.surface, green, ((X - tamX)/2 + (tamX/2)*i, (Y - tamY)/2 + (tamY)*j), 30)

        self.rect = ((X - tamX)/2,(Y - tamY)/2, tamX, tamY)