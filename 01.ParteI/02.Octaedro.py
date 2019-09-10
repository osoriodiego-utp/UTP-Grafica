# -*- coding: utf-8 -*-
# TEMA: Rotación 3D  FECHA: ??

import sys, math, pygame
from operator import itemgetter

from color import *
from pygame.locals import *
import pygame.draw
import pygame.time
from math import sin, cos

ORIGINX = 0
ORIGINY = 0

def draw_3dline(surface, color, a, b):
	ax = a[0]+(a[2]*0.3)+ORIGINX
	ay = a[1]+(a[2]*0.3)+ORIGINY
	bx = b[0]+(b[2]*0.3)+ORIGINX
	by = b[1]+(b[2]*0.3)+ORIGINY
	pygame.draw.line(surface, color, (ax, ay), (bx, by))
	

def draw_octa(surface, color, octa):
	a, b, c, d, e, f = octa
	
	draw_3dline(surface, color, a, b)
	draw_3dline(surface, color, b, e)
	draw_3dline(surface, color, e, a)

	draw_3dline(surface, color, b, c)
	draw_3dline(surface, color, c, e)
	draw_3dline(surface, color, e, b)

	draw_3dline(surface, color, d, c)
	draw_3dline(surface, color, c, e)
	draw_3dline(surface, color, e, d)

	draw_3dline(surface, color, a, d)
	draw_3dline(surface, color, d, e)
	draw_3dline(surface, color, e, a)

	draw_3dline(surface, color, a, b)
	draw_3dline(surface, color, b, c)
	draw_3dline(surface, color, c, d)
	draw_3dline(surface, color, d, a)

	draw_3dline(surface, color, a, b)
	draw_3dline(surface, color, b, f)
	draw_3dline(surface, color, f, a)

	draw_3dline(surface, color, b, c)
	draw_3dline(surface, color, c, f)
	draw_3dline(surface, color, f, b)

	draw_3dline(surface, color, d, c)
	draw_3dline(surface, color, c, f)
	draw_3dline(surface, color, f, d)

	draw_3dline(surface, color, a, d)
	draw_3dline(surface, color, d, f)
	draw_3dline(surface, color, f, a)



def rotate_3dpoint(p, angle, axis):
	ret = [0, 0, 0]
	cosang = cos(angle)
	sinang = sin(angle)
	ret[0] += (cosang+(1-cosang)*axis[0]*axis[0])*p[0]
	ret[0] += ((1-cosang)*axis[0]*axis[1]-axis[2]*sinang)*p[1]
	ret[0] += ((1-cosang)*axis[0]*axis[2]+axis[1]*sinang)*p[2]
	ret[1] += ((1-cosang)*axis[0]*axis[1]+axis[2]*sinang)*p[0]
	ret[1] += (cosang+(1-cosang)*axis[1]*axis[1])*p[1]
	ret[1] += ((1-cosang)*axis[1]*axis[2]-axis[0]*sinang)*p[2]
	ret[2] += ((1-cosang)*axis[0]*axis[2]-axis[1]*sinang)*p[0]
	ret[2] += ((1-cosang)*axis[1]*axis[2]+axis[0]*sinang)*p[1]
	ret[2] += (cosang+(1-cosang)*axis[2]*axis[2])*p[2]
	return ret

def rotate_object(obj, angle, axis):
	for i in range(len(obj)):
		obj[i] = rotate_3dpoint(obj[i], angle, axis)
	


""" MAIN FUCTION """

if __name__ == "__main__":
	global ORIGINX, ORIGINY
	pygame.init()
	screen = pygame.display.set_mode((400,400))
	# Move origin to center of screen
	ORIGINX = screen.get_width()/2
	ORIGINY = screen.get_height()/2
	octa = [(-50,0,-50), (50,0,-50), (50,0,50), (-50,0,50), (0,100,0), (0,-100,0)]


	while 1:
		draw_octa(screen, 255, octa)
		event = pygame.event.poll()
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			break
		pygame.display.flip()
		pygame.time.delay(25)
		draw_octa(screen, 0, octa)
		rotate_object(octa, 0, (1,0,0))
		rotate_object(octa, 0.1, (0,1,0))
		rotate_object(octa, 0, (0,0,1))
