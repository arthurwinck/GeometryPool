from pygame.sprite import Sprite
#Será que precisa importar pygame inteiro?
import pygame as py

class TelaMesa(Sprite):
    def __init__(self, superficie):
        super().__init__()
        #Acho que não preciso de superfície (?)
        self.superficie = superficie
        self.telaX, self.telaY = py.display.get_surface().get_size()
        self.tamX = 1000
        self.tamY = 500
        #TelaMesa ira implementar apenas o desenho dela mesma, a outra classe ControladorTela irá criar esses objetos na tela
        self.tamPos = ((self.telaX - self.tamX)/2,(self.telaY - self.tamY)/2, self.tamX, self.tamY)
        self.green = (34, 161, 65)


    def atualizar(self):
        py.draw.rect(self.superficie, self.green, self.tamPos)
        
        for i in range(3):
            for j in range(2):
                py.draw.circle(self.superficie, self.green, ((self.telaX - self.tamX)/2 + (self.tamX/2)*i, (self.telaY - self.tamY)/2 + (self.tamY)*j), 25)

        self.rect = ((self.telaX - self.tamX)/2,(self.telaY - self.tamY)/2, self.tamX, self.tamY)
