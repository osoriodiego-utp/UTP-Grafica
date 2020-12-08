#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from random import randint
from classes import projectile


class Invader(pygame.sprite.Sprite):
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
        self.shoot_range = 1
        self.speed = 1

        self.horizontal_move = True
        self.counter = 0
        self.down = self.rect.top + 40

        self.limit_right = pos_x + distance
        self.limit_left = pos_x - distance

        self.conquest = False



    def move(self, play_time):
        if(self.conquest == False):
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
            invader_projectile = projectile.Projectile(
                x, y, "assets/images/disparo_b.jpg", False)
            self.shoot_list.append(invader_projectile)

    def draw(self, surface):
        self.sprite_invader = self.sprite_list[self.sprite_selected]
        surface.blit(self.sprite_invader, self.rect)

