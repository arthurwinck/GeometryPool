from pygame.sprite import Sprite
import pygame as py

class TelaMesa(Sprite):
    def __init__(self, superficie):
        super().__init__()
        self.superficie = superficie
        self.telaX, self.telaY = py.display.get_surface().get_size()
        self.tamX = 1000
        self.tamY = 500
        self.desenhar_mesa()

    def desenhar_mesa(self):
        tamPos = ((self.telaX - self.tamX)/2,(self.telaY - self.tamY)/2, self.tamX, self.tamY)
        green = (34, 161, 65)

        py.draw.rect(self.superficie, green, tamPos)
        
        for i in range(3):
            for j in range(2):
                py.draw.circle(self.superficie, green, ((self.telaX - self.tamX)/2 + (self.tamX/2)*i, (self.telaY - self.tamY)/2 + (self.tamY)*j), 25)

        self.rect = ((self.telaX - self.tamX)/2,(self.telaY - self.tamY)/2, self.tamX, self.tamY)