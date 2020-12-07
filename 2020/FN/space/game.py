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


# CLASSES
class space_ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_nave = pygame.image.load("assets/images/nave.jpg")
        self.shoot_sound = pygame.mixer.Sound("assets/sounds/shoot.ogg")

        self.rect = self.sprite_nave.get_rect()
        self.rect.centerx = int(X/2)
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
        self.shoot_sound.play()
        ship_projectile = projectile(x, y, "assets/images/disparo_a.jpg", True)
        self.shoot_list.append(ship_projectile)

    def draw(self, surface):
        surface.blit(self.sprite_nave, self.rect)


class projectile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, sprite_path, character):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_projectile = pygame.image.load(sprite_path)
        self.rect = self.sprite_projectile.get_rect()
        self.speed = 5
        self.rect.top = pos_y
        self.rect.left = pos_x
        self.shooter = character

    def trajectory(self):
        if(self.shooter == True):
            self.rect.top = self.rect.top - self.speed
        else:
            self.rect.top = self.rect.top + self.speed

    def draw(self, surface):
        surface.blit(self.sprite_projectile, self.rect)


class invader(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, distance, img_1, img_2):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_marciano_a = pygame.image.load(img_1)
        self.sprite_marciano_b = pygame.image.load(img_2)

        self.sprite_list = [self.sprite_marciano_a, self.sprite_marciano_b]
        self.sprite_selected = 0
        self.sprite_invader = self.sprite_list[self.sprite_selected]
        self.time_to_change = 1

        self.rect = self.sprite_invader.get_rect()
        self.rect.top = pos_y
        self.rect.left = pos_x

        self.shoot_list = []
        self.shoot_range = 5
        self.speed = 10

        self.horizontal_move = True
        self.counter = 0
        self.down = self.rect.top + 40

        self.limit_right = pos_x + distance
        self.limit_left = pos_x - distance

    def move(self, play_time):
        # Disparar
        self.shoot()
        # Animación
        if (play_time == self.time_to_change):
            self.sprite_selected += 1
            self.time_to_change += 1
            if self.sprite_selected > len(self.sprite_list)-1:
                self.sprite_selected = 0
        if(self.counter < 2):
            # Movimiento horizontal
            if(self.horizontal_move == True):
                self.rect.left = self.rect.left + self.speed
                if(self.rect.left > self.limit_right):
                    self.horizontal_move = False
                    self.counter += 1
            else:
                self.rect.left = self.rect.left - self.speed
                if(self.rect.left < self.limit_left):
                    self.horizontal_move = True
        else:
            # movimiento descendente
            if(self.down == self.rect.top):
                self.counter = 0
                self.down = self.rect.top + 40
            else:
                self.rect.top += 1

    def shoot(self):
        if(randint(0, 100) < self.shoot_range):
            x, y = self.rect.center
            invader_projectile = projectile(
                x, y, "assets/images/disparo_b.jpg", False)
            self.shoot_list.append(invader_projectile)

    def draw(self, surface):
        self.sprite_invader = self.sprite_list[self.sprite_selected]
        surface.blit(self.sprite_invader, self.rect)


def load_enemies():
    posx = 100
    for i in range(1, 5):
        enemy_1 = invader(posx, 100, 40, "assets/images/marciano_1a.jpg", "assets/images/marciano_1b.jpg")
        enemy_list.append(enemy_1)
        posx = posx +200

    posx = 100
    for i in range(1, 5):
        enemy_2 = invader(posx, 0, 40, "assets/images/marciano_2a.jpg", "assets/images/marciano_2b.jpg")
        enemy_list.append(enemy_2)
        posx = posx +200

    posx = 100
    for i in range(1, 5):
        enemy_3 = invader(posx, -100, 40, "assets/images/marciano_3a.jpg", "assets/images/marciano_3b.jpg")
        enemy_list.append(enemy_3)
        posx = posx +200
        

def space_invaders():
    pygame.init()
    screen = pygame.display.set_mode((X, Y))
    pygame.display.set_caption("Space Invaders")
    background = pygame.image.load("assets/images/fondo.jpg")

    pygame.mixer.music.load("assets/sounds/spaceship.ogg")
    pygame.mixer.music.play()

    player = space_ship()
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
