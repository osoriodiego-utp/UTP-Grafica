#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import pygame
import transformaciones as trans
from color import *

X, Y = 600, 600


if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode([X, Y])
    a = [150, 100]
    b = [400, 100]
    
    #Ejes cartesianos
    pygame.draw.line(pantalla, color.blanco, [(X/2), 0], [X/2, Y])
    pygame.draw.line(pantalla, color.blanco, [0, Y/2], [X, Y/2])

    pygame.display.flip()
    reloj = pygame.time.Clock()
    cont = 0
    # e = [2,2]
    fin = False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if(cont<3):
                    if  (cont==0):
                        p1 = list(event.pos)
                        q1 = trans.rotar2(90, p1)
                        s1 = trans.transcartesiano(([300,300]), q1)
                        print(p1, q1)
                        cont +=1
                    elif (cont==1):
                        p2 = list(event.pos)
                        q2 = trans.rotar2(90, p2)
                        s2 =  trans.transcartesiano([300, 300], q2)
                        print(p2, q2)
                        cont +=1
                    elif (cont==2):
                        p3 = list(event.pos)
                        q3 = trans.rotar2(90, p3)
                        s3 =  trans.transcartesiano([300, 300], q3)
                        print(p3, q3)
                        cont +=1
                if(cont==3):
                    #Original
                    pygame.draw.line(pantalla, color.verde, p1, p2)
                    pygame.draw.line(pantalla, color.verde, p2, p3)
                    pygame.draw.line(pantalla, color.verde, p3, p1)
                    #Escalado
                    pygame.draw.line(pantalla, color.rojo, s1, s2)
                    pygame.draw.line(pantalla, color.rojo, s2, s3)
                    pygame.draw.line(pantalla, color.rojo, s3, s1)
                    cont = 0

                pygame.display.flip()
        reloj.tick(5)

