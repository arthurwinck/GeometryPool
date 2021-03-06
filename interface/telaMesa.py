from pygame.sprite import Sprite
#Será que precisa importar pygame inteiro?
import pygame as py
import numpy as np

class TelaMesa(Sprite):
    #TODO - ATUALIZAR DIAGRAMA PARA PARAMETRO DISPLAY
    #TODO - ATUALIZAR DIAGRAMA PARA RETIRAR RECT?
    def __init__(self, display):
        super().__init__()
        self.superficie = display.set_mode((1280,720))
        self.telaX, self.telaY = py.display.get_surface().get_size()
        self.tamX = 1000
        self.tamY = 500
        #calculo para descobrir os pontos x e y para iniciar o desenho da mesa
        #x e y inicial e largura e altura
        self.tamPos = ((self.telaX - self.tamX)/2,(self.telaY - self.tamY)/2, self.tamX, self.tamY)
        #variável que teria que ser colocada em um arquivo de configuração
        self.green = (34, 161, 65)

    def desenharMesa(self):
        self.superficie.fill((82,91,247))
        py.draw.rect(self.superficie, self.green, self.tamPos)
        
        for i in range(3):
            for j in range(2):
                py.draw.circle(self.superficie, self.green, ((self.telaX - self.tamX)/2 + (self.tamX/2)*i, (self.telaY - self.tamY)/2 + (self.tamY)*j), 20)

    def desenharBolas(self, bolas):
        for bola in bolas:
            pos_x, pos_y = bola.getPosicao()
            vel_x, vel_y = bola.getVelocidade()
            
            py.draw.circle(self.superficie, bola.cor, (pos_x,pos_y), 15)

    def desenharLimites(self, limites):
        for limite in limites:
            #Pontos é uma lista de 2 tuplas
            pontos = limite.getPosicao()
            #Aqui fiz uma matemática pra n precisar reescrever muitas vezes o código, ele checa se 
            #a altura ou a largura (que é o ponto xy)
            if pontos[1][1] - pontos[0][1]  == 0:
                py.draw.rect(self.superficie, (255,248,220), (pontos[0][0], pontos[0][1], pontos[1][0] - pontos[0][0], 5 ))
            elif pontos[1][0] - pontos[0][0] == 0 and pontos[0][0] == self.tamPos[0]:
                py.draw.rect(self.superficie, (255,248,220), (pontos[0][0], pontos[0][1], 5, pontos[1][1] - pontos[0][1] ))
            else:
                py.draw.rect(self.superficie, (255,248,220), (pontos[0][0], pontos[0][1], 5, pontos[1][1] - pontos[0][1] ))

    def desenharTaco(self, taco, vec_x, vec_y, bola_x, bola_y):
        angle = np.arctan2(vec_x, vec_y)

        rotated_taco = py.transform.rotate(taco.taco_img, np.degrees(angle) - 90)

        taco_rect = rotated_taco.get_rect(center=(
            bola_x - vec_x * taco.forca_taco * 10 - 380 * vec_x,
            bola_y - vec_y * taco.forca_taco * 10 - 380 * vec_y,
        ))

        self.superficie.blit(rotated_taco, taco_rect)
