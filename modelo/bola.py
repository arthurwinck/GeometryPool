import pygame as py
import pymunk

class Bola():
    def __init__(self, x,y, velocidade, cor):
        self.corpo = pymunk.Body(1,1)   
        self.corpo.position = (x,y)
        self.forma = pymunk.Circle(self.corpo, 15)
        self.forma.elasticity = 0.5
        self.corpo.velocity = velocidade,0
        self.cor = cor
        self.movimento = False

    def aplicar_atrito(self):
        # Método para aplicar o atrito de uma maneira top-down (não existe no pymunk)
        # Estabelecendo um atrito, podemos parar a a movimentação se a velocidade for minúscula
        atrito = 0.99
        valor_minimo_velocidade = 1

        #Também é possível criar uma variável que indica se uma bola está em movimento ou não
        self.movimento = True

        # if abs(self.corpo.velocity.x) < atrito - 0.05 and abs(self.corpo.velocity.y) < atrito - 0.05:
        #     self.corpo.velocity = 0,0
        #     movimento = False
        # elif self.corpo.velocity.x > 0 and self.corpo.velocity.y > 0:
        #     self.corpo.velocity = (self.corpo.velocity.x - atrito), (self.corpo.velocity.y - atrito)
        # elif self.corpo.velocity.x > 0 and self.corpo.velocity.y < 0:
        #     self.corpo.velocity = (self.corpo.velocity.x - atrito), (self.corpo.velocity.y + atrito)
        # elif self.corpo.velocity.x < 0 and self.corpo.velocity.y < 0:
        #     self.corpo.velocity = (self.corpo.velocity.x + atrito), (self.corpo.velocity.y + atrito)

        self.corpo.velocity = (self.corpo.velocity.x*(atrito), self.corpo.velocity.y*(atrito))

        if abs(self.corpo.velocity.x) < valor_minimo_velocidade and abs(self.corpo.velocity.y) < valor_minimo_velocidade:
            self.corpo.velocity = 0,0
            self.movimento = False

        return self.movimento

    def getVelocidade(self):
        return self.corpo.velocity

    def getPosicao(self):
        return self.corpo.position

    def getBody(self):
        return self.corpo
