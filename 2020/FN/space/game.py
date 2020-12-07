#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
import time
import pygame
from pygame.locals import *
import numpy as np

# GLOBALES
X, Y = 900, 480


# CLASSES
class space_ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprite_nave = pygame.image.load("assets/nave.jpg")
        self.rect = self.sprite_nave.get_rect()
        self.rect.centerx = X/2
        self.rect.centery = Y-30
        self.alive = True
        self.speed = 20
        self.shoot_list = []

    def right_move(self):
        self.rect.right += self.speed
        self.move()

    def left_move(self):
        self.rect.left -= self.speed
        self.move()

    def move(self):
        if self.alive == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > X:
                self.rect.right = X

    def shoot(self, x, y):
        my_projectile = projectile(x, y)
        self.shoot_list.append(my_projectile)
        print("¡shoot!")

    def draw(self, surface):
        surface.blit(self.sprite_nave, self.rect)


class projectile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_projectile = pygame.image.load("assets/disparo_a.jpg")
        self.rect = self.sprite_projectile.get_rect()
        self.speed = 5
        self.rect.top = pos_y
        self.rect.left = pos_x

    def trajectory(self):
        self.rect.top = self.rect.top - self.speed

    def draw(self, surface):
        surface.blit(self.sprite_projectile, self.rect)


class invader(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_marciano_a = pygame.image.load("assets/marciano_a.jpg")
        self.rect = self.sprite_marciano_a.get_rect()
        self.rect.top = pos_y
        self.rect.left = pos_x
        self.speed = 20
        self.shoot_list = []

    def draw(self, surface):
        surface.blit(self.sprite_marciano_a, self.rect)


def space_invaders():
    pygame.init()
    screen = pygame.display.set_mode((X, Y))
    pygame.display.set_caption("Space Invaders")
    background = pygame.image.load("assets/fondo.jpg")

    player = space_ship()
    projectile_demo = projectile(X/2, Y-30)
    playing = True

    enemy = invader(100, 100)

    refresh = pygame.time.Clock()

    while True:
        refresh.tick(60)
        # player.move()

        projectile_demo.trajectory()

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
        player.draw(screen)
        enemy.draw(screen)

        if(len(player.shoot_list) > 0):
            for shoot in player.shoot_list:
                shoot.draw(screen)
                shoot.trajectory()

                if(shoot.rect.top < 0):
                    player.shoot_list.remove(shoot)

        pygame.display.update()


if __name__ == "__main__":
    space_invaders()
