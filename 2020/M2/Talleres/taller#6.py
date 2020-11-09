
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
    #Head
    pygame.draw.circle(ventana, color.gris, (200, 37), 10, 1)
    pygame.draw.rect(ventana, color.gris, [195, 45, 12, 30], 1)
    pygame.draw.rect(ventana, color.gris, [150, 75, 100, 50], 1)
    pygame.draw.rect(ventana, color.gris, [175, 125, 50, 14], 1)
    #Trunk
    pygame.draw.rect(ventana, color.gris, [150, 162, 100, 38], 1)
    pygame.draw.rect(ventana, color.gris, [125, 138, 150, 138], 1)
    pygame.draw.circle(ventana, color.gris, (175, 250), 6, 1)
    pygame.draw.circle(ventana, color.gris, (200, 250), 6, 1)
    pygame.draw.circle(ventana, color.gris, (225, 250), 6, 1)
    #Arms
    pygame.draw.rect(ventana, color.gris, [75, 175, 25, 75], 1)
    pygame.draw.rect(ventana, color.gris, [300, 175, 25, 75], 1)
    #Legs
    pygame.draw.rect(ventana, color.gris, [150, 275, 25, 75], 1)
    pygame.draw.line(ventana, color.gris, (175, 350), (175, 375), 1)
    pygame.draw.line(ventana, color.gris, (175, 375), (125, 375), 1)
    pygame.draw.line(ventana, color.gris, (125, 375), (175, 350), 1)
    pygame.draw.rect(ventana, color.gris, [225, 275, 25, 75], 1)
    pygame.draw.line(ventana, color.gris, (225, 350), (275, 375), 1)
    pygame.draw.line(ventana, color.gris, (275, 375), (225, 375), 1)
    pygame.draw.line(ventana, color.gris, (225, 375), (225, 350), 1)



# ==== (1.0) TORRE      ====
def draw_tower():
    #Base
    pygame.draw.line(ventana, color.gris, (450, 375), (750, 375), 1)

    #Tower (techo)
    pygame.draw.line(ventana, color.gris, (575, 125), (650, 50), 1)
    pygame.draw.line(ventana, color.gris, (650, 50), (725, 125), 1)
    pygame.draw.line(ventana, color.gris, (575, 125), (650, 100), 1)
    pygame.draw.line(ventana, color.gris, (650, 100), (725, 125), 1)
    pygame.draw.line(ventana, color.gris, (575, 125), (600, 150), 1)
    pygame.draw.line(ventana, color.gris, (600, 150), (650, 125), 1)
    pygame.draw.line(ventana, color.gris, (650, 125), (700, 150), 1)
    pygame.draw.line(ventana, color.gris, (650, 50), (650, 125), 1)
    pygame.draw.line(ventana, color.gris, (700, 150), (725, 125), 1)
    #Tower (cajón)
    pygame.draw.line(ventana, color.gris, (600, 150), (587, 250), 1)
    pygame.draw.line(ventana, color.gris, (650, 125), (650, 375), 1)
    pygame.draw.line(ventana, color.gris, (700, 150), (725, 375), 1)
    #V1
    #V2
    pygame.draw.line(ventana, color.gris, (665, 150), (680, 155), 1)
    pygame.draw.line(ventana, color.gris, (680, 155), (685, 185), 1)
    pygame.draw.line(ventana, color.gris, (685, 185), (665, 180), 1)
    pygame.draw.line(ventana, color.gris, (665, 180), (665, 150), 1)
    #V3
    #V4
    pygame.draw.line(ventana, color.gris, (665, 200), (685, 205), 1)
    pygame.draw.line(ventana, color.gris, (685, 205), (690, 255), 1)
    pygame.draw.line(ventana, color.gris, (690, 255), (665, 250), 1)
    pygame.draw.line(ventana, color.gris, (665, 250), (665, 200), 1)
    #V5
    #V6
    pygame.draw.line(ventana, color.gris, (665, 275), (690, 280), 1)
    pygame.draw.line(ventana, color.gris, (690, 280), (695, 335), 1)
    pygame.draw.line(ventana, color.gris, (695, 335), (665, 330), 1)
    pygame.draw.line(ventana, color.gris, (665, 330), (665, 275), 1)

    #House (techo)
    pygame.draw.line(ventana, color.gris, (475, 250), (600, 250), 1)
    pygame.draw.line(ventana, color.gris, (475, 250), (450, 300), 1)
    pygame.draw.line(ventana, color.gris, (475, 250), (500, 300), 1)
    pygame.draw.line(ventana, color.gris, (600, 250), (625, 300), 1)
    pygame.draw.line(ventana, color.gris, (450, 300), (625, 300), 1)
    #House (cajón)
    pygame.draw.line(ventana, color.gris, (450, 300), (450, 375), 1)
    pygame.draw.line(ventana, color.gris, (500, 300), (500, 375), 1)
    pygame.draw.line(ventana, color.gris, (625, 300), (625, 375), 1)


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
    #Axes
    pygame.draw.line(ventana, color.gris, (500, 400), (500, 800), 1)
    pygame.draw.line(ventana, color.gris, (600, 400), (600, 800), 1)
    pygame.draw.line(ventana, color.gris, (700, 400), (700, 800), 1)
    pygame.draw.line(ventana, color.gris, (400, 500), (800, 500), 1)
    pygame.draw.line(ventana, color.gris, (400, 600), (800, 600), 1)
    pygame.draw.line(ventana, color.gris, (400, 700), (800, 700), 1)

    #R1
    pygame.draw.line(ventana, color.gris, (416, 400), (400, 416), 1)
    pygame.draw.line(ventana, color.gris, (432, 400), (400, 433), 1)
    pygame.draw.line(ventana, color.gris, (448, 400), (400, 448), 1)
    pygame.draw.line(ventana, color.gris, (464, 400), (400, 464), 1)
    pygame.draw.line(ventana, color.gris, (480, 400), (400, 480), 1)
    pygame.draw.line(ventana, color.gris, (500, 400), (600, 500), 3)
    pygame.draw.line(ventana, color.gris, (600, 500), (500, 600), 3)
    pygame.draw.line(ventana, color.gris, (500, 600), (400, 500), 3)
    pygame.draw.line(ventana, color.gris, (400, 500), (500, 400), 3)


    #R2
    #R3
    #R4

# ==== MAIN FUNCTION    ====
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
    

    draw_robot()
    draw_tower()
    draw_squares_c()
    draw_squares_s()

    draw_axes()

    pygame.display.flip()
pygame.quit()
