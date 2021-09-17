from pygame.sprite import Sprite
#Será que precisa importar pygame inteiro?
import pygame as py
import numpy as np

class TelaMesa(Sprite):
    def __init__(self, superficie):
        super().__init__()
        self.superficie = superficie
        self.telaX, self.telaY = py.display.get_surface().get_size()
        self.tamX = 1000
        self.tamY = 500
        self.tamPos = ((self.telaX - self.tamX)/2,(self.telaY - self.tamY)/2, self.tamX, self.tamY)
        #variável que teria que ser colocada em um arquivo de configuração
        self.green = (34, 161, 65)


    def desenharMesa(self):
        py.draw.rect(self.superficie, self.green, self.tamPos)
        
        for i in range(3):
            for j in range(2):
                py.draw.circle(self.superficie, self.green, ((self.telaX - self.tamX)/2 + (self.tamX/2)*i, (self.telaY - self.tamY)/2 + (self.tamY)*j), 25)

        self.rect = ((self.telaX - self.tamX)/2,(self.telaY - self.tamY)/2, self.tamX, self.tamY)

    def desenharBolas(self, bolas):
        for bola in bolas:
            pos_x, pos_y = bola.getPosicao()
            vel_x, vel_y = bola.getVelocidade()
            
            py.draw.circle(self.superficie, bola.cor, (pos_x,pos_y), 15)

    def desenharTaco(self, taco, vec_x, vec_y, bola_x, bola_y):
        angle = np.arctan2(vec_x, vec_y)

        rotated_taco = py.transform.rotate(taco.taco_img, np.degrees(angle) - 90)

        taco_rect = rotated_taco.get_rect(center=(
            bola_x - vec_x * taco.forca_taco * 10 - 380 * vec_x,
            bola_y - vec_y * taco.forca_taco * 10 - 380 * vec_y,
        ))

        self.superficie.blit(rotated_taco, taco_rect)