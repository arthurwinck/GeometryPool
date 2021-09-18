import pygame as py
import pymunk

MULTIPLICADOR_FORCA = 1800

class Taco():
    def __init__(self):
        self.forca_taco = 0

        taco_img = py.image.load('assets/taco.png')
        self.taco_img = py.transform.scale(taco_img, (700, 350))

    def getForca(self, vec_x, vec_y):
        return (
            vec_x * self.forca_taco * MULTIPLICADOR_FORCA,
            vec_y * self.forca_taco * MULTIPLICADOR_FORCA,
        )

    def reset(self):
        self.forca_taco = 0

    def aumentarForca(self):
        self.forca_taco += 1
