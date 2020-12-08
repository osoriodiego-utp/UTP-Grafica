#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
import time
import pygame
from pygame.locals import *
import numpy as np
from random import randint

# GLOBALES
X, Y = 900, 480
enemy_list = []

# CLASES
from classes import ship
from classes import invader
# from classes import invader as invader


def load_enemies():
    posx = 100
    for i in range(1, 5):
        enemy_1 = invader.Invader(posx, 100, 40, "assets/images/marciano_1a.jpg", "assets/images/marciano_1b.jpg")
        enemy_list.append(enemy_1)
        posx = posx +200

    posx = 100
    for i in range(1, 5):
        enemy_2 = invader.Invader(posx, 0, 40, "assets/images/marciano_2a.jpg", "assets/images/marciano_2b.jpg")
        enemy_list.append(enemy_2)
        posx = posx +200

    posx = 100
    for i in range(1, 5):
        enemy_3 = invader.Invader(posx, -100, 40, "assets/images/marciano_3a.jpg", "assets/images/marciano_3b.jpg")
        enemy_list.append(enemy_3)
        posx = posx +200
        

def space_invaders():
    pygame.init()
    screen = pygame.display.set_mode((X, Y))
    pygame.display.set_caption("Space Invaders")
    background = pygame.image.load("assets/images/fondo.jpg")

    pygame.mixer.music.load("assets/sounds/spaceship.ogg")
    pygame.mixer.music.play()

    player = ship.Space_ship(X, Y)
    # enemy_list = invader(100, 50)
    load_enemies()

    refresh = pygame.time.Clock()
    playing = True

    while playing:
        refresh.tick(60)
        play_time = round(pygame.time.get_ticks()/1000)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if (playing == True):
                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT:
                        player.left_move()
                    elif event.key == K_RIGHT:
                        player.right_move()
                    elif event.key == K_s:
                        x, y = player.rect.center
                        player.shoot(x, y)

        screen.blit(background, (0, 0))
        # enemy_list.move(play_time)
        player.draw(screen)
        # enemy_list.draw(screen)

        if(len(player.shoot_list) > 0):
            for shoot in player.shoot_list:
                shoot.draw(screen)
                shoot.trajectory()

                if(shoot.rect.top < -10):
                    player.shoot_list.remove(shoot)
                else:
                    for enemy in enemy_list:
                        if(shoot.rect.colliderect(enemy.rect)):
                            enemy_list.remove(enemy)
                            player.shoot_list.remove(shoot)

        if(len(enemy_list)>0):
            for enemy in enemy_list:
                enemy.move(play_time)
                enemy.draw(screen)

                if enemy.rect.colliderect(player.rect):
                    pass

                if(len(enemy.shoot_list) > 0):
                    for e_shoot in enemy.shoot_list:
                        e_shoot.draw(screen)
                        e_shoot.trajectory()
                        if(e_shoot.rect.colliderect(player.rect)):
                            pass
                        if(e_shoot.rect.top > 900):
                            enemy.shoot_list.remove(e_shoot)
                        else:
                            #Eliminar proyectiles que chocan
                            for p_shoot in player.shoot_list:
                                if (e_shoot.rect.colliderect(p_shoot.rect)):
                                    player.shoot_list.remove(p_shoot)
                                    enemy.shoot_list.remove(e_shoot)

        pygame.display.update()


if __name__ == "__main__":
    space_invaders()
