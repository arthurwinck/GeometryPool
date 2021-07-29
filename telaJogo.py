import pygame as py

from telaMesa import TelaMesa

class TelaJogo():
    def __init__(self):
        self.tela = py.display

        self.configurar_tela()
        self.iniciar_jogo()
        #self.adicionar_mesa()
        self.iniciar_jogo()
        
    def configurar_tela(self):

        azul = (82,91,247)

        self.tela.set_caption('Geometry Pool')
        self.superficie = self.tela.set_mode((1280,720))
        self.superficie.fill(azul)
        self.tela.update()
        
    def adicionar_mesa(self):
        pass

    def iniciar_jogo(self):
        self.mesa = TelaMesa(self.superficie)
        self.tela.update()

        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()


  

