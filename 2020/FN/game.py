#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
import time
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
    time.sleep(1)


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
                if(x > 24 and x < 124 and y > 424 and y < 474):
                    print("PLAY")
                    play()
                if(x > 142 and x < 242 and y > 424 and y < 474):
                    print("HELP")
                    # help()
                if(x > 262 and x < 362 and y > 424 and y < 474):
                    print("ABOUT")
                    about()
                if(x > 378 and x < 478 and y > 424 and y < 474):
                    print("BYE...")
                    sys.exit(0)
    pygame.display.update()

   
def move(player, x, y):
    if(player == "X"):
        print("load X")
        figure = pygame.image.load("assets/img/cross.png")
    if(player == "O"):
        print("load O")
        figure = pygame.image.load("assets/img/circle.png")

    if(y > 35 and y < 176):
        if(x > 45 and x < 178):
            print(f"{player} in C1")
            screen.blit(figure, (45,35))
        if(x > 178 and x < 308):
            print(f"{player} in C2")
            screen.blit(figure, (178,35))
        if(x > 308 and x < 456):
            print(f"{player} in C3")
            screen.blit(figure, (308,35))
    if(y > 176 and y < 295):
        if(x > 45 and x < 178):
            print(f"{player} in C4")
            screen.blit(figure, (45,176))
        if(x > 178 and x < 308):
            print(f"{player} in C5")
            screen.blit(figure, (178,176))
        if(x > 308 and x < 456):
            print(f"{player} in C6")
            screen.blit(figure, (308,176))
    if(y > 295 and y < 395):
        if(x > 45 and x < 178):
            print(f"{player} in C7")
            screen.blit(figure, (45,295))
        if(x > 178 and x < 308):
            print(f"{player} in C8")
            screen.blit(figure, (178,295))
        if(x > 308 and x < 456):
            print(f"{player} in C9")
            screen.blit(figure, (308,295))


def change(player):
    if(player == "X"):
        return "O"
    else:
        return "X"


def play():
    gameBackground = pygame.image.load("assets/img/game.png")
    screen.blit(gameBackground, (0, 0))
    pygame.display.update()
    player = "X"
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if (event.type == pygame.MOUSEBUTTONDOWN):
                x, y = event.pos
                # TIC-TAC-TOE
                if(x > 45 and x < 456 and y > 35 and y < 395):
                    move(player, x, y)
                    player = change(player)
                # BUTTONS
                if(x > 24 and x < 124 and y > 424 and y < 474):
                    print("HOME")
                    menu()
                if(x > 142 and x < 242 and y > 424 and y < 474):
                    print("HELP")
                    # help()
                if(x > 262 and x < 362 and y > 424 and y < 474):
                    print("ABOUT")
                    about()
                if(x > 378 and x < 478 and y > 424 and y < 474):
                    print("BYE...")
                    sys.exit(0)
                # print(f"Click on: {(x, y)}")


def help():
    print("Open help window")


def about():
    aboutBackground = pygame.image.load("assets/img/about.png")
    screen.blit(aboutBackground, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if (event.type == pygame.MOUSEBUTTONDOWN):
                x, y = event.pos
                if(x > 24 and x < 124 and y > 424 and y < 474):
                    print("BACK")
                    menu()
                if(x > 142 and x < 242 and y > 424 and y < 474):
                    print("PLAY")
                    play()
                if(x > 262 and x < 362 and y > 424 and y < 474):
                    print("HELP")
                    help()
                if(x > 378 and x < 478 and y > 424 and y < 474):
                    print("BYE...")
                    sys.exit(0)
    pygame.display.update()

    print("\tJuego creado para la clase de \n\tcomputación gráfica.")
    print("\tDiego Osorio López.")
    print("\tFacultad de Ingenierías. \n\tUTP 2020-2")


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
