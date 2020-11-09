
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math
import pygame
from pygame.locals import *
import numpy as np

from color import *


pygame.init()

X, Y = 800, 800
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
    #Axes
    pygame.draw.line(ventana, color.gris, (200, 400), (200, 800), 1)
    pygame.draw.line(ventana, color.gris, (0, 600), (400, 600), 1)
    #R1
    pygame.draw.line(ventana, color.gris, (100, 400), (200, 500), 1)
    pygame.draw.line(ventana, color.gris, (200, 500), (100, 600), 1)
    pygame.draw.line(ventana, color.gris, (100, 600), (0, 500), 1)
    pygame.draw.line(ventana, color.gris, (0, 500), (100, 400), 1)
    pygame.draw.rect(ventana, color.gris, [50, 450, 100, 100], 1)
    pygame.draw.line(ventana, color.gris, (100, 450), (150, 500), 1)
    pygame.draw.line(ventana, color.gris, (150, 500), (100, 550), 1)
    pygame.draw.line(ventana, color.gris, (100, 550), (50, 500), 1)
    pygame.draw.line(ventana, color.gris, (50, 500), (100, 450), 1)
    pygame.draw.line(ventana, color.gris, (75, 475), (125, 525), 1) 
    pygame.draw.line(ventana, color.gris, (125, 475), (75, 525), 1) 

    #R2
    pygame.draw.line(ventana, color.gris, (100+200, 400), (200+200, 500), 1)
    pygame.draw.line(ventana, color.gris, (200+200, 500), (100+200, 600), 1)
    pygame.draw.line(ventana, color.gris, (100+200, 600), (0+200, 500), 1)
    pygame.draw.line(ventana, color.gris, (0+200, 500), (100+200, 400), 1)
    pygame.draw.rect(ventana, color.gris, [50+200, 450, 100, 100], 1)
    pygame.draw.line(ventana, color.gris, (100+200, 450), (150+200, 500), 1)
    pygame.draw.line(ventana, color.gris, (150+200, 500), (100+200, 550), 1)
    pygame.draw.line(ventana, color.gris, (100+200, 550), (50+200, 500), 1)
    pygame.draw.line(ventana, color.gris, (50+200, 500), (100+200, 450), 1)
    pygame.draw.line(ventana, color.gris, (75+200, 475), (125+200, 525), 1) 
    pygame.draw.line(ventana, color.gris, (125+200, 475), (75+200, 525), 1) 

    #R3
    pygame.draw.line(ventana, color.gris, (100, 400+200), (200, 500+200), 1)
    pygame.draw.line(ventana, color.gris, (200, 500+200), (100, 600+200), 1)
    pygame.draw.line(ventana, color.gris, (100, 600+200), (0, 500+200), 1)
    pygame.draw.line(ventana, color.gris, (0, 500+200), (100, 400+200), 1)
    pygame.draw.rect(ventana, color.gris, [50, 450+200, 100, 100+200], 1)
    pygame.draw.line(ventana, color.gris, (100, 450+200), (150, 500+200), 1)
    pygame.draw.line(ventana, color.gris, (150, 500+200), (100, 550+200), 1)
    pygame.draw.line(ventana, color.gris, (100, 550+200), (50, 500+200), 1)
    pygame.draw.line(ventana, color.gris, (50, 500+200), (100, 450+200), 1)
    pygame.draw.line(ventana, color.gris, (75, 475+200), (125, 525+200), 1) 
    pygame.draw.line(ventana, color.gris, (125, 475+200), (75, 525+200), 1)
    
    #R4
    pygame.draw.line(ventana, color.gris, (100+200, 400+200), (200+200, 500+200), 1)
    pygame.draw.line(ventana, color.gris, (200+200, 500+200), (100+200, 600+200), 1)
    pygame.draw.line(ventana, color.gris, (100+200, 600+200), (0+200, 500+200), 1)
    pygame.draw.line(ventana, color.gris, (0+200, 500+200), (100+200, 400+200), 1)
    pygame.draw.rect(ventana, color.gris, [50+200, 450+200, 100, 100], 1)
    pygame.draw.line(ventana, color.gris, (100+200, 450+200), (150+200, 500+200), 1)
    pygame.draw.line(ventana, color.gris, (150+200, 500+200), (100+200, 550+200), 1)
    pygame.draw.line(ventana, color.gris, (100+200, 550+200), (50+200, 500+200), 1)
    pygame.draw.line(ventana, color.gris, (50+200, 500+200), (100+200, 450+200), 1)
    pygame.draw.line(ventana, color.gris, (75+200, 475+200), (125+200, 525+200), 1) 
    pygame.draw.line(ventana, color.gris, (125+200, 475+200), (75+200, 525+200), 1) 


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
