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
pygame.draw.circle(ventana, color.blanco, (x_med, 50), 12, 1)
pygame.draw.rect(ventana, color.blanco, [195, 62, 10, 30], 1)
# Cabeza
pygame.draw.rect(ventana, color.blanco, [120, 92, 162, 87], 1)
# Cara
#Cuello
pygame.draw.rect(ventana, color.blanco, [150, 180, 100, 20], 1)
#Tronco
pygame.draw.rect(ventana, color.blanco, [90, 200, 220, 220], 1)
#Piernas
pygame.draw.rect(ventana, color.blanco, [125, 420, 40, 80], 1)
pygame.draw.rect(ventana, color.blanco, [230, 420, 40, 80], 1)




pygame.display.update()
time.sleep(2)
