
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
pygame.display.set_caption("Taller de funciones primitivas gráficas ")


def draw_point(point):
    pygame.draw.circle(ventana, color.rojo, point, 1, 1)


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


def draw_rectangle(p_start, p_end):
    xi = p_start[0]
    yi = p_start[1]
    xf = p_end[0]
    yf = p_end[1]
    draw_line_dda([xi,yi],[xf,yi])
    draw_line_dda([xi, yf],[xf, yf])
    draw_line_dda([xi, yi],[xi, yf])
    draw_line_dda([xf, yi],[xf, yf])


def draw_rectangle_filled(p_start, p_end):
    for x in range(p_start[0], p_end[0]):
        for y in range(p_start[1], p_end[1]):
            draw_point([x,y])


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
def fig_uno(p_start, p_end):
    x = p_end[0]-p_start[0]
    y = p_end[1]-p_start[1]
    draw_rectangle(p_start, p_end)
    draw_rectangle_filled(p_start, (p_end[0], p_end[y]))
    # draw_rectangle_filled((p_start[0]+x, p_end+y), p_end)



# ==== MAIN FUNCTION    ====
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

    center = (int(X/2), int(Y/2))
    
    # draw_line_dda(center, (400,400))
    # draw_rectangle((100,200), (300, 400))
    # draw_rectangle_filled((100,200), (300, 400))
    # draw_circle(100, 200, 300, 400)
    # draw_circle_bresenham(center[0], center[1], 100)
    fig_uno((100,100), (400,200))

    pygame.display.flip()
pygame.quit()
