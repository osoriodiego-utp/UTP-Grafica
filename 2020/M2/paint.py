
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math
import pygame
from pygame.locals import *
import numpy as np

from color import *


pygame.init()

X, Y = 600, 400
ventana = pygame.display.set_mode((X, Y))
pygame.display.set_caption("PAINT")

def color_palette():
    pygame.draw.rect(ventana, color.amarillo, (550, 0, 600, 50))
    pygame.draw.rect(ventana, color.azul_pizarra_oscuro, (550, 50, 600, 100))
    pygame.draw.rect(ventana, color.rojo, (550, 100, 600, 150))
    pygame.draw.rect(ventana, color.verde, (550, 150, 600, 200))
    pygame.draw.rect(ventana, color.naranja_puro, (550, 200, 600, 250))
    pygame.draw.rect(ventana, color.violeta_oscuro, (550, 250, 600, 300))
    pygame.draw.rect(ventana, color.blanco, (550, 300, 600, 350))
    pygame.draw.rect(ventana, color.violeta_oscuro, (550, 350, 600, 400))



def draw_figure(figure, color_figure):
    if(color_figure=="amarillo"):
        pygame.draw.circle(ventana, color.amarillo, (x, y), 1, 1)
    if(color_figure=="verde"):
        pygame.draw.circle(ventana, color.verde, (x, y), 1, 1)



# ==== MAIN FUNCTION    ====

figura = "cuadro"
color_figura = "negro"

while True:

    color_palette()

    for event in pygame.event.get():

        if event.type == QUIT:
            sys.exit(0)

        x,y = pygame.mouse.get_pos()

        if(x<50):
            if event.type == MOUSEBUTTONDOWN:
                figura = "triangulo"
                print("figure must change")

        if(x>550):
            if event.type == MOUSEBUTTONDOWN:
                color_figura = "verde"
                print("color must change")

        if(x>550 and y<100):
            if event.type == MOUSEBUTTONDOWN:
                color_figura = "amarillo"
                print("color must change")

        if(x>50 and x<550):
            if event.type == MOUSEBUTTONDOWN:
                draw_figure(figura, color_figura)
                
        

    pygame.display.flip()
pygame.quit()
