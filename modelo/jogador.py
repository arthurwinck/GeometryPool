import pygame as py
import pymunk

class Jogador():
    def __init__(self, nome):
        self.nome = nome
        self.bolas = []
        self.pontos = 0
        self.taco = None
        
        self.turno = False
        self.vencedor = False
        self.jogadaValida = False
        self.fezPontos = False
        self.bolaVermelha = False
        self.bolaNumerada = False
        self.bolaTocada = None

    def ObterTaco(self):
        return self.taco

    def ObterJogadaValida(self):
        return self.jogadaValida
        
    def ObterFezPontos(self):
        return self.fezPontos

    def AdicionarPontos(self, pontos):
        #mais lógica aqui?
        self.pontos += pontos

    def setTurnoJogador(self):
        self.turno = True

