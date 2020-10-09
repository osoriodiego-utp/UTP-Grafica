
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

def to_cart(punto):
    return tuple((round(CX+punto[0]), round(CY-punto[1])))

def draw_punto(point):
    pygame.draw.circle(ventana, color.amarillo, point, 3, 3)

def draw_line_dda(p_start, p_end):
    xo = p_start[0]
    yo = p_start[1]
    xi = p_end[0]
    yi = p_end[1]

    dx = xi-xo
    dy = yi-yo

    if(abs(dx) > abs(dy)):
        steps = dx
    else:
        steps = dy

    x_increment = float(dx)/float(steps)
    y_increment = float(dy)/float(steps)

    # punto(screen, color, [xo, yo])

    for i in range(steps):
        xo += x_increment
        yo += y_increment
        punto(ventana, color.amarillo, [int(round(xo)), int(round(yo))])


# recorrido = [(9.40, 3.42), (9.71, 7.05), (-6.93, 4.00), (-18.00, 0.00), (-10.50, -21.26)]
recorrido = [(00.00, 00.00), (90.40, 30.42), (90.71, 70.05), (-60.93, 40.00), (-180.00, 00.00), (-100.50, -210.26)]


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

    # Ejes x/y
    pygame.draw.line(ventana, color.blanco, (CX, 0), (CX, Y), 2)
    pygame.draw.line(ventana, color.blanco, (0, CY), (X, CY), 2)
    
    # for pos in recorrido:
        # draw_punto(to_cart(pos))
    #     print (pos) 

    for i in range(0, len(recorrido)-1):
        pygame.draw.line(ventana, color.amarillo, to_cart(recorrido[i]), to_cart(recorrido[i+1]), 1)
        draw_punto(to_cart(recorrido[i+1]))
        print(recorrido[i])
    
    pygame.display.flip()

pygame.quit()
