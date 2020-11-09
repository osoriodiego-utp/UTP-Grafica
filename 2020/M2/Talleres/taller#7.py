
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math
import pygame
from pygame.locals import *
import numpy as np

from color import *


pygame.init()
X, Y = 1000, 400
ventana = pygame.display.set_mode((X, Y)) 
pygame.display.set_caption("Taller de funciones primitivas gráficas ")

def draw_axes(color):
    draw_line_dda(color, (0, 200), (1000,200))
    draw_line_dda(color, (200, 0), (200,400))
    draw_line_dda(color, (400, 0), (400,400))
    draw_line_dda(color, (600, 0), (600,400))
    draw_line_dda(color, (800, 0), (800,400))


def draw_point(color, point):
    pygame.draw.circle(ventana, color, point, 1, 1)


def draw_line_dda(color, p_start, p_end):
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

    draw_point(color, [int(round(xi)), int(round(yi))])

    for i in range(steps):
        xi += x_increment
        yi += y_increment
        draw_point(color, [int(round(xi)), int(round(yi))])


def draw_rectangle(color, p_start, p_end):
    xi = p_start[0]
    yi = p_start[1]
    xf = p_end[0]
    yf = p_end[1]
    draw_line_dda(color, [xi,yi],[xf,yi])
    draw_line_dda(color, [xi, yf],[xf, yf])
    draw_line_dda(color, [xi, yi],[xi, yf])
    draw_line_dda(color, [xf, yi],[xf, yf])


def draw_rectangle_filled(color, p_start, p_end):
    for x in range(p_start[0], p_end[0]):
        for y in range(p_start[1], p_end[1]):
            draw_point(color, [x,y])


def draw_circle(xc, yc, x, y):
    draw_point((xc+x, yc+y))
    draw_point((xc-x, yc+y))
    draw_point((xc+x, yc-y))
    draw_point((xc-x, yc-y))
    draw_point((xc+y, yc+x))
    draw_point((xc-y, yc+x))
    draw_point((xc+y, yc-x))
    draw_point((xc-y, yc-x))


def draw_circle_bresenham(xc, yc, r):
    x = 0
    y = r
    d = 3-2*r
    draw_circle(xc, yc, x, y)
    while(y>=x):
        x=x+1
        if(d>0):
            y = y - 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        draw_circle(xc, yc, x ,y)


###################### F I G U R A S ######################
def fig_uno(color):
    draw_rectangle_filled(color, (25, 50), (100, 100))
    draw_rectangle(color, (100, 50), (175, 100))
    draw_rectangle(color, (25, 100), (100, 150))
    draw_rectangle_filled(color, (101, 101), (176, 151))

def fig_dos(color):
    draw_rectangle(color, (225, 25), (375, 175))
    draw_rectangle_filled(color, (225, 25), (275, 75))
    draw_rectangle_filled(color, (325, 25), (375, 75))
    draw_rectangle_filled(color, (275, 75), (325, 125))
    draw_rectangle_filled(color, (225, 125), (275, 175))
    draw_rectangle_filled(color, (325, 125), (375, 175))

def fig_tres(color):
    pass

def fig_cuatro(color):
    pass

def fig_cinco(color):
    pass

def fig_seis(color):
    pass

def fig_siete(color):
    pass

def fig_ocho(color):
    pass

def fig_nueve(color):
    pass

def fig_diez(color):
    pass


# ==== MAIN FUNCTION    ====
if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)

        draw_axes(color.blanco)
        fig_uno(color.azul)
        fig_dos(color.azul)
        fig_tres(color.azul)
        fig_cuatro(color.azul)
        fig_cinco(color.azul)
        fig_seis(color.azul)
        fig_siete(color.azul)
        fig_ocho(color.azul)
        fig_nueve(color.azul)
        fig_diez(color.azul)

        pygame.display.flip()
    pygame.quit()
