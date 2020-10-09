import pygame
import math
import time
import numpy as np
from color import *

windows = pygame
Width, Height = 600, 600
center = [int(Width/2), int(Height/2)]

# FUNCIONES


def punto(screen, color, point):
    pygame.draw.line(screen, color, point, point, 2)


def draw_line_dda(screen, color, p_start, p_end):
    xo = p_start[0]
    yo = p_start[1]
    xi = p_end[0]
    yi = p_end[1]

    dx = xi-xo
    dy = yi-yo

    if(abs(dx) > abs(dy)):
        steps = dx
    else:
        steps = dy

    x_increment = float(dx)/float(steps)
    y_increment = float(dy)/float(steps)

    # punto(screen, color, [xo, yo])

    for i in range(steps):
        xo += x_increment
        yo += y_increment
        punto(screen, color, [int(round(xo)), int(round(yo))])
        # print(xo, yo)


# PROGRAMA PRINCIPAL
pygame.init()
window = pygame.display.set_mode((Width, Height))

punto(window, color.azul_celeste, (200, 200))

puntos = [[300, 100], [500, 100], [500, 300], [500, 500],
          [300, 500], [100, 500], [100, 300], [100, 100]]


for point in puntos:
    print(center, point)
    draw_line_dda(window, color.rojo_fuego, center, point)

# draw_line_dda(window, color.rojo_fuego, center, [800, 300])

pygame.display.update()
time.sleep(3)
