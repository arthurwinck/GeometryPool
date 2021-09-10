from pygame.sprite import Sprite
#Será que precisa importar pygame inteiro?
import pygame as py

class TelaMesa(Sprite):
    def __init__(self, superficie):
        super().__init__()
        self.superficie = superficie
        self.telaX, self.telaY = py.display.get_surface().get_size()
        self.tamX = 1000
        self.tamY = 500
        #variável que teria que ser colocada em um arquivo de configuração
        self.green = (34, 161, 65)


    def desenharMesa(self):
        py.draw.rect(self.superficie, self.green, self.tamPos)
        
        for i in range(3):
            for j in range(2):
                py.draw.circle(self.superficie, self.green, ((self.telaX - self.tamX)/2 + (self.tamX/2)*i, (self.telaY - self.tamY)/2 + (self.tamY)*j), 25)

        self.rect = ((self.telaX - self.tamX)/2,(self.telaY - self.tamY)/2, self.tamX, self.tamY)

    def desenharBolas(self):
        pos_x = int(self.corpo.position.x)
        pos_y = int(self.corpo.position.y)
        if self.corpo.velocity.x > 0:
            self.corpo.velocity = self.corpo.velocity.x - 0.1, 0

        py.draw.circle(self.superficie, (255,0,0), (pos_x,pos_y), 15)   