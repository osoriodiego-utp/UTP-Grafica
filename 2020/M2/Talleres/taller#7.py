
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


def draw_line_bres(color, p_start, p_end):
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
        draw_point(color, (x,y))
        while (x != xEnd):
            x += stepX
            if (p<0):
                p += incE
            else:
                p += incNE
                y += stepY
            draw_point(color, (x,y))
    else:
        p = 2*dx-dy
        incE = 2*dx
        incNE = 2*(dx-dy)
        x = xo
        y = yo
        yEnd = yi
        stepY = 1
        draw_point(color, (x,y))
        while(y!= yEnd):
            y += stepY
            if(p<0):
                p += incE
            else:
                p += incNE
                x += stepX
            draw_point(color, (x,y))


def draw_rectangle(color, p_start, p_end):
    xi = p_start[0]
    yi = p_start[1]
    xf = p_end[0]
    yf = p_end[1]
    draw_line_dda(color, [xi, yi],[xf, yi])
    draw_line_dda(color, [xi, yf],[xf, yf])
    draw_line_dda(color, [xi, yi],[xi, yf])
    draw_line_dda(color, [xf, yi],[xf, yf])


def draw_rectangle_filled(color, p_start, p_end):
    for x in range(p_start[0], p_end[0]):
        for y in range(p_start[1], p_end[1]):
            draw_point(color, [x,y])


def draw_circle(color, xc, yc, x, y):
    draw_point(color, (xc+x, yc+y))
    draw_point(color, (xc-x, yc+y))
    draw_point(color, (xc+x, yc-y))
    draw_point(color, (xc-x, yc-y))
    draw_point(color, (xc+y, yc+x))
    draw_point(color, (xc-y, yc+x))
    draw_point(color, (xc+y, yc-x))
    draw_point(color, (xc-y, yc-x))


def draw_circle_bresenham(color, xc, yc, r):
    x = 0
    y = r
    d = 3-2*r
    draw_circle(color, xc, yc, x, y)
    while(y>=x):
        x=x+1
        if(d>0):
            y = y - 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        draw_circle(color, xc, yc, x ,y)


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
    draw_rectangle(color, (425, 25), (575, 175))
    draw_rectangle_filled(color, (475, 25), (525, 75))
    draw_rectangle_filled(color, (425, 75), (475, 125))
    draw_rectangle_filled(color, (475, 75), (525, 125))
    draw_rectangle_filled(color, (525, 75), (575, 125))
    draw_rectangle_filled(color, (475, 125), (525, 175))

def fig_cuatro(color):
    draw_rectangle_filled(color, (625,50), (675, 75))
    draw_rectangle_filled(color, (625,75), (700, 100))
    draw_rectangle_filled(color, (625,100), (725, 125))
    draw_rectangle_filled(color, (625,125), (750, 150))
    draw_rectangle_filled(color, (625,150), (775, 175))

def fig_cinco(color):
    draw_rectangle_filled(color, (888, 25), (913, 50))
    draw_rectangle_filled(color, (875, 50), (925, 75))
    draw_rectangle_filled(color, (863, 75), (937, 100))
    draw_rectangle_filled(color, (850, 100), (950, 125))
    draw_rectangle_filled(color, (837, 125), (962, 150))
    draw_rectangle_filled(color, (825, 150), (975, 175))

def fig_seis(color):
    draw_line_dda(color, (50, 250), (150,350))
    draw_line_dda(color, (50, 250), (50,350))
    draw_line_dda(color, (50, 350), (150,350))

def fig_siete(color):
    draw_line_dda(color, (300, 250), (375,375))
    draw_line_dda(color, (225, 375), (375,375))
    draw_line_dda(color, (300, 250), (225,375))

def fig_ocho(color):
    draw_line_dda(color, (450, 250), (550, 250))
    draw_line_dda(color, (450, 250), (425, 350))
    draw_line_dda(color, (550, 250), (575, 350))
    draw_line_dda(color, (425, 350), (575, 350))

def fig_nueve(color):
    draw_line_dda(color, (700, 225), (775, 275))
    draw_line_dda(color, (775, 275), (750, 350))
    # draw_line_dda(color, (750, 350), (650, 350))
    draw_line_dda(color, (650, 350), (750, 350))
    # draw_line_dda(color, (650, 350), (625, 275))
    draw_line_dda(color, (625, 275), (650, 350))
    draw_line_dda(color, (625, 275), (700, 225))

def fig_diez(color):
    draw_circle_bresenham(color, 900, 300, 75)


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
