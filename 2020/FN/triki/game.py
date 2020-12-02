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

matrix = np.matrix('"","","";"","","";"","",""')


def is_winner(m):
    # Columns
    if(m[0, 0] != "" and m[0, 0] == m[0, 1] == m[0, 2]):
        return True
    elif(m[1, 0] != "" and m[1, 0] == m[1, 1] == m[1, 2]):
        return True
    elif(m[2, 0] != "" and m[2, 0] == m[2, 1] == m[2, 2]):
        return True
    # Rows
    elif(m[0, 0] != "" and m[0, 0] == m[1, 0] == m[2, 0]):
        return True
    elif(m[0, 1] != "" and m[0, 1] == m[1, 1] == m[2, 1]):
        return True
    elif(m[0, 2] != "" and m[0, 2] == m[1, 2] == m[2, 2]):
        return True
    # Diagonals
    elif(m[0, 0] != "" and m[0, 0] == m[1, 1] == m[2, 2]):
        return True
    elif(m[0, 2] != "" and m[0, 2] == m[1, 1] == m[2, 0]):
        return True
    return False


def start():
    startBackground = pygame.image.load("assets/img/loading_bar.png")
    screen.blit(startBackground, (0, 0))
    pygame.display.update()
    time.sleep(1)


def restart():
    print("Matrix restarted")


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
                    help()
                if(x > 262 and x < 362 and y > 424 and y < 474):
                    print("ABOUT")
                    about()
                if(x > 378 and x < 478 and y > 424 and y < 474):
                    print("EXIT")
                    sys.exit(0)
    pygame.display.update()


def can_move(x, y):
    if(y > 35 and y < 176 and x > 45 and x < 178 and matrix[0, 0] == ""):
        return True
    elif(y > 35 and y < 176 and x > 178 and x < 308 and matrix[0, 1] == ""):
        return True
    elif(y > 35 and y < 176 and x > 308 and x < 456 and matrix[0, 2] == ""):
        return True
    elif(y > 176 and y < 295 and x > 45 and x < 178 and matrix[1, 0] == ""):
        return True
    elif(y > 176 and y < 295 and x > 178 and x < 308 and matrix[1, 1] == ""):
        return True
    elif(y > 176 and y < 295 and x > 308 and x < 456 and matrix[1, 2] == ""):
        return True
    elif(y > 295 and y < 395 and x > 45 and x < 178 and matrix[2, 0] == ""):
        return True
    elif(y > 295 and y < 395 and x > 178 and x < 308 and matrix[2, 1] == ""):
        return True
    elif(y > 295 and y < 395 and x > 308 and x < 456 and matrix[2, 2] == ""):
        return True
    return False


def move(player, x, y):
    if(player == "X"):
        figure = pygame.image.load("assets/img/cross.png")
    if(player == "O"):
        figure = pygame.image.load("assets/img/circle.png")

    if(y > 35 and y < 176):
        if(x > 45 and x < 178):
            screen.blit(figure, (45, 35))
            matrix[0, 0] = player
        if(x > 178 and x < 308):
            screen.blit(figure, (178, 35))
            matrix[0, 1] = player
        if(x > 308 and x < 456):
            screen.blit(figure, (308, 35))
            matrix[0, 2] = player
    if(y > 176 and y < 295):
        if(x > 45 and x < 178):
            screen.blit(figure, (45, 176))
            matrix[1, 0] = player
        if(x > 178 and x < 308):
            screen.blit(figure, (178, 176))
            matrix[1, 1] = player
        if(x > 308 and x < 456):
            screen.blit(figure, (308, 176))
            matrix[1, 2] = player
    if(y > 295 and y < 395):
        if(x > 45 and x < 178):
            screen.blit(figure, (45, 295))
            matrix[2, 0] = player
        if(x > 178 and x < 308):
            screen.blit(figure, (178, 295))
            matrix[2, 1] = player
        if(x > 308 and x < 456):
            screen.blit(figure, (308, 295))
            matrix[2, 2] = player
    pygame.display.update()
    print("==========")
    print(matrix)


def change_player(player):
    if(player == "X"):
        return "O"
    else:
        return "X"


def play():
    restart()
    gameBackground = pygame.image.load("assets/img/game.jpg")
    screen.blit(gameBackground, (0, 0))
    pygame.display.update()
    player = "X"
    player_win = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if (event.type == pygame.MOUSEBUTTONDOWN):
                x, y = event.pos
                # TIC-TAC-TOE
                if(x > 45 and x < 456 and y > 35 and y < 395):
                    if(can_move(x, y) and player_win == False):
                        move(player, x, y)
                        if(is_winner(matrix)):
                            player_win = True
                            print(f"WINNER: {player}")
                            winner(player)
                        player = change_player(player)
                # BUTTONS
                if(x > 24 and x < 124 and y > 424 and y < 474):
                    print("HOME")
                    menu()
                if(x > 142 and x < 242 and y > 424 and y < 474):
                    print("HELP")
                    help()
                if(x > 262 and x < 362 and y > 424 and y < 474):
                    print("ABOUT")
                    about()
                if(x > 378 and x < 478 and y > 424 and y < 474):
                    print("EXIT")
                    sys.exit(0)


def help():
    helpBackground = pygame.image.load("assets/img/help.png")
    screen.blit(helpBackground, (0, 0))
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
                    print("ABOUT")
                    about()
                if(x > 378 and x < 478 and y > 424 and y < 474):
                    print("EXIT")
                    sys.exit(0)
    pygame.display.update()


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
                    print("EXIT")
                    sys.exit(0)
    pygame.display.update()


def winner(player):
    if(player == "X"):
        figure = pygame.image.load("assets/img/cross.png")
    if(player == "O"):
        figure = pygame.image.load("assets/img/circle.png")
    
    winnerBackground = pygame.image.load("assets/img/winner.png")
    screen.blit(winnerBackground, (0, 0))
    pygame.display.update()
    screen.blit(figure, (200,200))
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
                    help()
                if(x > 262 and x < 362 and y > 424 and y < 474):
                    print("ABOUT")
                    about()
                if(x > 378 and x < 478 and y > 424 and y < 474):
                    print("EXIT")
                    sys.exit(0)
    pygame.display.update()


if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
        start()
        menu()

        pygame.display.flip()
    pygame.quit()
