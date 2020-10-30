
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math
import pygame
from pygame.locals import *
import numpy as np

from color import *


pygame.init()

X, Y = 700, 700
CX, CY = int(X/2), int(Y/2)

ventana = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Graficas primitivas")
center = [X/2, Y/2]

# ==== EJES X/Y         ====
def draw_axes():
    pygame.draw.line(ventana, color.blanco, (CX, 0), (CX, Y), 2)
    pygame.draw.line(ventana, color.blanco, (0, CY), (X, CY), 2)

# ==== (1.0) ROBOT      ====
def draw_robot():
    pass
# ==== (1.0) TORRE      ====
def draw_tower():
    pass

# ==== (1.5) CUADROS1   ====
def draw_squares_s():
    pass

# ==== (1.5) CUADROS2   ====
def draw_squares_c():
    pass

# ==== MAIN FUNCTION    ====
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
    
    draw_axes()

    draw_robot()
    draw_tower()
    draw_squares_c()
    draw_squares_s()


    pygame.display.flip()
pygame.quit()
