
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math
import pygame
from pygame.locals import *
import numpy as np

from color import *


pygame.init()

X, Y = 700, 700
ventana = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Función linea - Algoritmo Bresenham")

# ==== OTHER FN         ====
def draw_point(point):
    pygame.draw.circle(ventana, color.amarillo, point, 1, 1)

# ==== BRESENHAM FN     ====
def draw_line_bres(p_start, p_end):
    xo = p_start[0]
    yo = p_start[1]
    xi = p_end[0]
    yi = p_end[1]

    dx = xi-xo
    dy = yi-yo

    stepX = -1 if dx <0 else 1
    dx = math.fabs(dx)

    stepY = -1 if dy <0 else 1
    dy = math.fabs(dy)

    if (dx>dy):
        p = 2*dy-dx
        incE = 2*dy
        incNE = 2*(dy-dx)
        x = xo
        y = yo
        xEnd = xi
        stepX = 1
        draw_point((x,y))
        while (x != xEnd):
            x += stepX
            if (p<0):
                p += incE
            else:
                p += incNE
                y += stepY
            draw_point((x,y))
    else:
        p = 2*dx-dy
        incE = 2*dx
        incNE = 2*(dx-dy)
        x = xo
        y = yo
        yEnd = yi
        stepY = 1
        draw_point((x,y))
        while(y!= yEnd):
            y += stepY
            if(p<0):
                p += incE
            else:
                p += incNE
                x += stepX
            draw_point((x,y))


# ==== MAIN FUNCTION    ====
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

    draw_line_bres((100,100), (200,200))
    draw_line_bres((200,200), (300,300))

    draw_line_bres((200,100), (300,100))


    pygame.display.flip()
pygame.quit()
