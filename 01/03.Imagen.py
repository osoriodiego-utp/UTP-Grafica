#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
from random import randint


pygame.init()
width, height = 500, 500
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("IMAGEN")

#pygame.draw.circle(ventana, (50,150,200), (200,200), 50)
#pygame.draw.rect(ventana, color, (250,250,300,100))
#pygame.draw.polygon(ventana, color, ((200,90),(240,150),(550,200),(500,40),(570,100)))
imagen = pygame.image.load("img/marioPerfil.png")


while True:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit(0) 

	screen.blit(imagen, (width/2, height/2))
	pygame.display.flip()

pygame.quit()