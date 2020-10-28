#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from color import *

x = y = 0
running = 1

screen = pygame.display.set_mode((600, 400))
cont = 0

while running:
    event = pygame.event.poll()
    if (event == pygame.QUIT):
        running = 0
    if (event == pygame.MOUSEMOTION):
        x, y = event.pos
    if (event == pygame.MOUSEBUTTONDOWN):
        if(cont<2):
            if(cont==0):
                p1 =list(event.pos)
                x1 = p1[0]
                y1 = p1[1]
                print(cont, x1, y1)
            if(cont==1):
                p2 =list(event.pos)
                x2 = p2[0]
                y2 = p2[1]
                print(cont, x2, y2)
        cont +=1
    
    screen.fill(color.negro)
    pygame.draw.line(screen, color.rojo, (x,0), (x,399))
    pygame.draw.line(screen, color.rojo, (0, y), (599,y))
    pygame.display.flip()
    
    
