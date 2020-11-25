#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math, time
import pygame
from pygame.locals import *
import numpy as np
from assets.color import *

pygame.init()
X, Y = 500, 500
ventana = pygame.display.set_mode((X, Y))
pygame.display.set_caption("GAME.PY")
screen = pygame.display.set_mode((X, Y))


def start():
    startBackground = pygame.image.load("assets/img/loading_bar.png")
    screen.blit(startBackground, (0, 0))
    pygame.display.update()
    time.sleep(2)


def menu():
    menuBackground = pygame.image.load("assets/img/home.png")
    screen.blit(menuBackground, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if (event.type == pygame.MOUSEBUTTONDOWN):
                x, y = event.pos
                if(x>24 and x <124 and y>424 and y<474):
                    print("Open game screen")
                    play()
                if(x>142 and x <242 and y>424 and y<474):
                    print("Open help view")
                    # help()
                if(x>262 and x <362 and y>424 and y<474):
                    print("Open about view")
                    # play()
                if(x>378 and x <478 and y>424 and y<474):
                    print("Bye")
                    sys.exit(0)
    screen.blit(menuBackground, (0, 0))
    pygame.display.update()


def play():
    gameBackground = pygame.image.load("assets/img/game.png")
    screen.blit(gameBackground, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if (event.type == pygame.MOUSEBUTTONDOWN):
                x, y = event.pos
                if(x>24 and x <124 and y>424 and y<474):
                    print("Open home screen")
                    menu()
                if(x>142 and x <242 and y>424 and y<474):
                    print("Open help view")
                    # help()
                if(x>262 and x <362 and y>424 and y<474):
                    print("Open about view")
                    # play()
                if(x>378 and x <478 and y>424 and y<474):
                    print("Bye")
                    sys.exit(0)
                print(f"Click on: {(x, y)}")


def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
        start()
        menu()

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
