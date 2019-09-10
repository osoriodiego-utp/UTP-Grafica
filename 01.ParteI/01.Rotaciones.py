# -*- coding: utf-8 -*-
# TEMA: Transfomaciones  FECHA: Agosto/30

import sys, math
from math import sin, cos
from operator import itemgetter
from random import randint

import pygame
from pygame.locals import *

from color import *

Width,Height = 500, 500
center = (Width/2, Height/2)


ventana = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("ROTACIONES")

def rotatePoint(p, angle):
	rot = [0,0]
	rot[0] = (cos(angle)*p[0] - sin(angle)*p[1])
	rot[1] = (sin(angle)*p[0] + cos(angle)*p[1])
	return rot

def rotateLine(l, angle):
	for i in range(len(l)):
		l[i] = rotatePoint(l[i], angle)

	

if __name__ == "__main__":
	initial = (100,100)
	while True:
		pygame.draw.line(ventana, color.rojo, (center), (initial), 2)
		event = pygame.event.poll()
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			break
		pygame.display.flip()
		pygame.draw.line(ventana, color.negro, (center), (initial), 2)
		pygame.time.delay(500)
		pygame.draw.line(ventana, color.rojo, (center), (rotatePoint(initial, 10)), 2)
		#pygame.display.update()
