import pygame as py
import pymunk

class Jogador():
    def __init__(self, nome, taco):
        self.nome = nome
        self.bolas = []
        self.pontos = 0
        self.taco = taco
        
        self.turno = False
        self.vencedor = False
        self.jogadaValida = False
        self.fezPontos = False
        self.bolaVermelha = True
        self.bolaNumerada = False
        self.bolaTocada = None

    def obterTaco(self):
        return self.taco

    def obterJogadaValida(self):
        return self.jogadaValida

    def setJogadaInvalida(self):
        self.jogadaValida = False

    def setJogadaValida(self):
        self.jogadaValida = True

    def setFezPontos(self):
        self.fezPontos = True
        
    def obterFezPontos(self):
        return self.fezPontos

    def adicionarPontos(self, pontos):
        #mais lógica aqui?
        self.pontos += pontos
        #self.fezPontos = True

    def setTurnoJogador(self):
        self.turno = True

    def definirVencedor(self):
        self.vencedor = True

    def obterFaltaJogador(self):
        return not self.jogadaValida

    def obterBolas(self):
        return self.bolas

    def passarTurno(self):
        self.fezPontos = False
        self.turno = False
        #Será que é True? Seria None?
        self.jogadaValida = True
        self.bolas = []
        self.vencedor = False
        self.bolaTocada = None
        self.bolaNumerada = False
        self.bolaVermelha = True

    def inverteBolaVermelha(self):
        if self.bolaVermelha == True:
            self.bolaVermelha = False
        else:
            self.bolaVermelha = True

    def inverteBolaNumerada(self):
        if self.bolaNumerada == True:
            self.bolaNumerada = False
        else:
            self.bolaNumerada = True

    def setBolaNumerada(self):
        self.bolaNumerada = True

    def salvarBolaTocadaJogador(self, bola):
        if (self.bolaTocada == None):
            self.bolaTocada = bola

    def obterBolaTocada(self):
        return self.bolaTocada

    def obterBolaVermelha(self):
        return self.bolaVermelha

    def obterBolaNumerada(self):
        return self.bolaNumerada