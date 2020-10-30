
# -*- coding: utf-8 -*-
# import pygame

import sys, math
import pygame
from pygame.locals import *
import numpy as np

from color import *

pygame.init()

# traslación de un punto P
def trans(t,p):
    xp = t[0]+p[0]
    yp = t[1]+p[1]
    pp = [xp, yp]
    return pp

# de coordenadas cartesianas a pantalla
def cart_to_pant(c,p):
    xp = c[0]+p[0]
    yp = c[1]-p[1]
    pp = [xp, yp]
    return pp


# de coordenadas de pantalla a cartesianas
def pant_to_cart(c,p):
    xp = p[0]-c[0]
    yp = c[1]-p[1]
    pp = [xp, yp]
    return pp

# trasladat al centro
def trans_to_centro(c,p):
    xp = c[0]-p[0]
    yp = c[1]-p[1]
    pp = [xp, yp]
    return pp

# transladar punto ogiginal
def transoriginal(c,p)



# MAIN FUNCTION
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

    #BODY MAIN-FUNCTION
    
    pygame.display.flip()
pygame.quit()
