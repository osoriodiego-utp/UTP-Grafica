
# -*- coding: utf-8 -*-
# import pygame

import sys, math
import pygame
from pygame.locals import *
import numpy as np

from color import *

pygame.init()

X, Y = 600, 600
CX, CY = int(X/2), int(Y/2)
ventana = pygame.display.set_mode((X, Y))

pygame.display.set_caption("Recorrido automovislita")
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
recorrido = [(90.40, 30.42), (90.71, 70.05), (-60.93, 40.00), (-180.00, 00.00), (-100.50, -210.26)]

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

    # Ejes x/y
    pygame.draw.line(ventana, color.blanco, (CX, 0), (CX, Y), 2)
    pygame.draw.line(ventana, color.blanco, (0, CY), (X, CY), 2)


    pos_i = (0.0, 0.0)
    for i in range(0, len(recorrido)):
        pos_f = (pos_i[0]+recorrido[i][0], pos_i[1] + recorrido[i][1])
        pygame.draw.line(ventana, color.amarillo, to_cart(pos_i), to_cart(pos_f), 1)
        pos_i = pos_f
        new_pos = ()

    # Vector resultado
    pygame.draw.line(ventana, color.rojo, to_cart((0,0)), to_cart((-160.30, -70.13)), 1)
    
    pygame.display.flip()

pygame.quit()
