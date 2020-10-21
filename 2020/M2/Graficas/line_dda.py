
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
pygame.display.set_caption("Función linea - Algoritmo DDA")

# ==== OTHER FN    ====
def draw_point(point):
    pygame.draw.circle(ventana, color.rojo, point, 1, 1)

# ==== DDA FN      ====
def draw_line_dda(p_start, p_end):
    xi = p_start[0]
    yi = p_start[1]
    xf = p_end[0]
    yf = p_end[1]

    dx = xf-xi
    dy = yf-yi

    if(abs(dx) > abs(dy)):
        steps = dx
    else:
        steps = dy

    x_increment = float(dx)/float(steps)
    y_increment = float(dy)/float(steps)
    draw_point([int(round(xi)), int(round(yi))])
    for i in range(steps):
        xi += x_increment
        yi += y_increment
        draw_point([int(round(xi)), int(round(yi))])


# ==== MAIN FUNCTION    ====
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

    center = (int(X/2), int(Y/2))
    puntos = [[300, 100], [500, 100], [500, 300], [500, 500],
            [300, 500], [100, 500], [100, 300], [100, 100]]
    
    for point in puntos:
        draw_line_dda(center, point)

    pygame.display.flip()
pygame.quit()
