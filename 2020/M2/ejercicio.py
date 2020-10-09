
# -*- coding: utf-8 -*-
# import pygame

import sys, math
import pygame
from pygame.locals import *
# import numpy as np

from color import *

pygame.init()

X, Y = 600, 600
CX, CY = X/2, Y/2
ventana = pygame.display.set_mode((X, Y))

pygame.display.set_caption("Recorrido automovilista")
center = [X/2, Y/2]

def to_cart(x, y):
    return tuple((round(CX+x), round(CY-y)))

def draw_punto(point):
    pygame.draw.circle(ventana, color.amarillo, point, 3, 3)

recorrido = [(9.40, 3.42), (9.71, 7.05), (-6.93, 4.00), (-18.00, 0.00), (-10.50, -21.26)]


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

    pygame.draw.line(ventana, color.blanco, (CX, 0), (CX, Y), 3)
    pygame.draw.line(ventana, color.blanco, (0, CY), (X, CY), 3)
    
    for pos in recorrido:
        draw_punto(to_cart(pos[0], pos[1]))
        print (pos) 

    
    pygame.display.flip()

pygame.quit()
