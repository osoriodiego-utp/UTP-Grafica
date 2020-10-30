
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
import pygame
from pygame.locals import *
import numpy as np

from color import *

# Elaborar un gratificador básico usando la librería pygame y el material visto en clase

pygame.init()


def draw_point(color, point):
    pygame.draw.circle(ventana, color, point, 1, 1)


def draw_rectangle_filled(color, p_start, p_end):
    for x in range(p_start[0], p_end[0]):
        for y in range(p_start[1], p_end[1]):
            draw_point(color, [x, y])


X, Y = 800, 600
ventana = pygame.display.set_mode((X, Y))
pygame.display.set_caption("PAINT")
ventana.fill(color.blanco)


def figure_palette():
    draw_rectangle_filled(color.gris, (0, 0), (75, 600))
    draw_rectangle_filled(color.blanco, (10, 10), (65, 65))
    draw_rectangle_filled(color.blanco, (10, 75), (65, 130))
    draw_rectangle_filled(color.blanco, (10, 140), (65, 195))
    draw_rectangle_filled(color.blanco, (10, 205), (65, 260))
    draw_rectangle_filled(color.blanco, (10, 270), (65, 325))
    draw_rectangle_filled(color.blanco, (10, 335), (65, 390))
    draw_rectangle_filled(color.blanco, (10, 400), (65, 455))
    draw_rectangle_filled(color.blanco, (10, 465), (65, 520))


def color_palette():
    pygame.draw.rect(ventana, color.gris, (725, 0, 800, 600))
    draw_rectangle_filled(color.amarillo, (735, 10), (790, 65))
    draw_rectangle_filled(color.azul, (735, 75), (790, 130))
    draw_rectangle_filled(color.rojo, (735, 140), (790, 195))
    draw_rectangle_filled(color.verde, (735, 205), (790, 260))
    draw_rectangle_filled(color.naranja_puro, (735, 270), (790, 325))
    draw_rectangle_filled(color.violeta_oscuro, (735, 335), (790, 390))
    draw_rectangle_filled(color.blanco, (735, 400), (790, 455))
    draw_rectangle_filled(color.negro, (735, 465), (790, 520))


def draw_figure(figure, color_figure):
    if(color_figure == "amarillo"):
        pygame.draw.circle(ventana, color.amarillo, (x, y), 4, 4)
    if(color_figure == "azul"):
        pygame.draw.circle(ventana, color.azul, (x, y), 4, 4)
    if(color_figure == "rojo"):
        pygame.draw.circle(ventana, color.rojo, (x, y), 4, 4)
    if(color_figure == "verde"):
        pygame.draw.circle(ventana, color.verde, (x, y), 4, 4)
    if(color_figure == "blanco"):
        pygame.draw.circle(ventana, color.blanco, (x, y), 4, 4)
        

# ==== MAIN FUNCTION    ====
figura = "cuadro"
color_figura = "blanco"

while True:

    figure_palette()
    color_palette()

    for event in pygame.event.get():

        if event.type == QUIT:
            sys.exit(0)

        x, y = pygame.mouse.get_pos()

        if(x < 75):  # figure_palette
            if event.type == MOUSEBUTTONDOWN:
                figura = "triangulo"
                print("figure must change")

        if(x > 725):  # color_palette
            
            if(y>10 and y<65):
                if event.type == MOUSEBUTTONDOWN:
                    color_figura = "amarillo"
                    print("changed to \'amarillo\'")
            
            if(y>75 and y<130):
                if event.type == MOUSEBUTTONDOWN:
                    color_figura = "azul"
                    print("changed to \'azul\'")

            if(y>140 and y<195):
                if event.type == MOUSEBUTTONDOWN:
                    color_figura = "rojo"
                    print("changed to \'rojo\'")



        if(x > 75 and x < 725):  # draw_area
            if event.type == MOUSEBUTTONDOWN:
                draw_figure(figura, color_figura)

    pygame.display.flip()
pygame.quit()
