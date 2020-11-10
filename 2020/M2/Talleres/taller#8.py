
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
X, Y = 800, 600
ventana = pygame.display.set_mode((X, Y))
pygame.display.set_caption("PAINT")
ventana.fill(color.blanco)

# === Primitivas === ===

def distance(p1, p2):
    value = math.sqrt((math.pow((p2[0]-p1[0]), 2)) + (math.pow((p2[1]-p1[1]), 2)))
    return int(round(value))

def draw_point(color, point):
    pygame.draw.circle(ventana, color, point, 1, 1)

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
        draw_point(color, [x,y])
        while (x != xEnd):
            x += stepX
            if (p<0):
                p += incE
            else:
                p += incNE
                y += stepY
            draw_point(color, [x,y])
    else:
        p = 2*dx-dy
        incE = 2*dx
        incNE = 2*(dx-dy)
        x = xo
        y = yo
        yEnd = yi
        stepY = 1
        draw_point(color, [x,y])
        while(y!= yEnd):
            y += stepY
            if(p<0):
                p += incE
            else:
                p += incNE
                x += stepX
            draw_point(color, [x,y])

def draw_rectangle(color, p_start, p_end):
    xi = p_start[0]
    yi = p_start[1]
    xf = p_end[0]
    yf = p_end[1]
    draw_line_bres(color, [xi, yi], [xf,yi])
    draw_line_bres(color, [xi, yf], [xf, yf])
    draw_line_bres(color, [xi, yi], [xi, yf])
    draw_line_bres(color, [xf, yi], [xf, yf])

def draw_rectangle_filled(color, p_start, p_end):
    for x in range(p_start[0], p_end[0]):
        for y in range(p_start[1], p_end[1]):
            draw_point(color, [x, y])

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


# === Paletas paint  ===
def figure_palette():
    draw_rectangle_filled(color.gris, (0, 0), (75, 600))

    draw_rectangle_filled(color.blanco, (10, 10), (65, 65))
    draw_line_bres(color.plata, (20,20), (55,55))
    
    draw_rectangle_filled(color.blanco, (10, 75), (65, 130))
    draw_rectangle(color.plata, (20,85), (55,120))
    
    draw_rectangle_filled(color.blanco, (10, 140), (65, 195))
    draw_rectangle_filled(color.plata, (20,150), (55, 185))
    
    draw_rectangle_filled(color.blanco, (10, 205), (65, 260))
    draw_circle_bresenham(color.plata, 37, 232, 18)
    
    draw_rectangle_filled(color.blanco, (10, 270), (65, 325))
    #draw_right_triangle

    draw_rectangle_filled(color.blanco, (10, 335), (65, 390))
    #draw_equilateral_triangle
    
    draw_rectangle_filled(color.blanco, (10, 400), (65, 455))
    #draw_pentagon

    # draw_rectangle_filled(color.blanco, (10, 465), (65, 520))

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


# === Funciones  === ===
def draw_figure(figure, color_figure, p_start, p_end):
    if(figure == "line"):
        draw_line_bres(color_figure, p_start, p_end)
    if(figure == "rectangle"):
        draw_rectangle(color_figure, p_start, p_end)
    if(figure == "filled_rectangle"):
        draw_rectangle_filled(color_figure, p_start, p_end)
    if(figure == "circle"):
        pygame.draw.circle(ventana, color_figure, (p_start), distance(p_start, p_end), 4)
    if(figure == "right_triangle"):
        pygame.draw.circle(ventana, color.blanco, (x, y), 4, 4)
    if(figure == "equilateral_triangle"):
        pygame.draw.circle(ventana, color.blanco, (x, y), 4, 4)
    if(figure == "pentagon"):
        pygame.draw.circle(ventana, color.blanco, (x, y), 4, 4)

def color_select(x, y):
    if(y > 10 and y < 65):
        value = color.amarillo
    if(y > 75 and y < 130):
        value = color.azul
    if(y > 140 and y < 195):
        value = color.rojo
    if(y > 205 and y < 260):
        value = color.verde
    if(y > 270 and y < 325):
        value = color.naranja_puro
    if(y > 335 and y < 390):
        value = color.violeta_oscuro
    if(y > 400 and y < 455):
        value = color.blanco
    if(y > 465 and y < 520):
        value = color.negro
    if(y > 520):
        return
    return value

def figure_select(x, y):
    if(y > 10 and y < 65):
        value = "line"
    if(y > 75 and y < 130):
        value = "rectangle"
    if(y > 140 and y < 195):
        value = "filled_rectangle"
    if(y > 205 and y < 260):
        value = "circle"
    if(y > 270 and y < 325):
        value = "right_triangle"
    if(y > 335 and y < 390):
        value = "equilateral_triangle"
    if(y > 400 and y < 455):
        value = "pentagon"
    if(y > 450):
        return
    return value


# ==== MAIN FUNCTION    ====
figura = "cuadro"
color_figura = "blanco"


def main():
    figure_palette()
    color_palette()

    fig = "line"
    col = color.negro
    cont = 0
    p1 = ()
    p2 = ()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)

            if event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                
                if(x < 75):  # figure_palette
                    fig = figure_select(x,y)
                    print(f"Figure changed to {fig}")
                    cont = 0

                if(x>75 and x<725): #draw_area
                    if(cont < 2):
                        if(cont == 0):
                            p1 = (x,y)
                            # print(f"DIBUJO desde {p1}")
                        if(cont == 1):
                            p2 = pygame.mouse.get_pos()
                            print(f"Draw {fig} from {p1} to {p2}")
                            draw_figure(fig, col, p1, p2)
                        cont +=1
                        if(cont == 2):
                            cont = 0

                if(x>725): #Color_area
                    col = color_select(x,y)
                    print(f"Color changed")
                    cont = 0


        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
