# -*- coding: utf-8 -*-
# TEMA: Transfomaciones  FECHA: Agosto/30

import sys
import math
import time
from math import sin, cos
from operator import itemgetter
from random import randint

import pygame
from pygame.locals import *

from color import *

Width, Height = 400, 600
center = (Width/2, Height/2)
x_med = int(Width/2)  # 200
y_med = int(Height/2)  # 300


ventana = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("ROBOT")

# Cuadrado
#pygame.draw.rect(ventana, color.blanco, [x, y, lx, ly], 1)

# Antena
pygame.draw.circle(ventana, color.blanco, (200, 38), 12, 1)
pygame.draw.rect(ventana, color.blanco, [195, 50, 10, 25], 1)
# Cabeza
pygame.draw.rect(ventana, color.blanco, [125, 75, 150, 100], 1)
# Cara-ojos
pygame.draw.circle(ventana, color.blanco, (162, 112), 12, 1)
pygame.draw.circle(ventana, color.blanco, (237, 112), 12, 1)
# Cara-boca
pygame.draw.rect(ventana, color.blanco, [162, 137, 75, 25], 1)
pygame.draw.line(ventana, color.blanco, (182, 137), (182, 162), 1)
pygame.draw.line(ventana, color.blanco, (200, 137), (200, 162), 1)
pygame.draw.line(ventana, color.blanco, (218, 137), (218, 162), 1)


# Cuello
pygame.draw.rect(ventana, color.blanco, [150, 175, 100, 25], 1)
# Tronco
pygame.draw.rect(ventana, color.blanco, [100, 200, 200, 225], 1)
pygame.draw.rect(ventana, color.blanco, [112, 225, 175, 62], 1)
# Triangulos
pygame.draw.polygon(ventana, color.blanco, [
                    (147, 250), (123, 275), (153, 275)])
pygame.draw.polygon(ventana, color.blanco, [
                    (182, 250), (164, 275), (194, 275)])
pygame.draw.polygon(ventana, color.blanco, [
                    (217, 250), (205, 275), (235, 275)])
pygame.draw.polygon(ventana, color.blanco, [
                    (252, 250), (246, 275), (276, 275)])

# Circulos
pygame.draw.circle(ventana, color.blanco, (150, 375), 12, 1)
pygame.draw.circle(ventana, color.blanco, (200, 375), 12, 1)
pygame.draw.circle(ventana, color.blanco, (250, 375), 12, 1)

# PiernaIzq
pygame.draw.rect(ventana, color.blanco, [125, 425, 37, 75], 1)
pygame.draw.line(ventana, color.blanco, (125, 500), (125, 512), 1)
pygame.draw.polygon(ventana, color.blanco, [(162, 500), (162, 536), (75, 536)])
# PiernaDer
pygame.draw.rect(ventana, color.blanco, [238, 425, 37, 75], 1)
pygame.draw.line(ventana, color.blanco, (275, 500), (275, 512), 1)
pygame.draw.polygon(ventana, color.blanco, [
                    (238, 500), (238, 536), (325, 535)])


pygame.display.update()
time.sleep(10)
