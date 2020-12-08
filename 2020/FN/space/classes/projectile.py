#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame


class Projectile(pygame.sprite.Sprite):
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