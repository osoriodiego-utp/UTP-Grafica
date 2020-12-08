#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from classes import projectile

class Space_ship(pygame.sprite.Sprite):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

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
            elif self.rect.right > self.X:
                self.rect.right = self.X

    def shoot(self, x, y):
        self.shoot_sound.play()
        ship_projectile = projectile.Projectile(x, y, "assets/images/disparo_a.jpg", True)
        self.shoot_list.append(ship_projectile)

    def draw(self, surface):
        surface.blit(self.sprite_nave, self.rect)

