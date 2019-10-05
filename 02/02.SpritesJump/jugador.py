import pygame


class xena(pygame.sprite.Sprite):
    def __init__(self, posicion):
        self.hoja = pygame.image.load("trump.png")
        self.hoja.set_clip(pygame.Rect(0, 0, 100, 100))
        self.imagen = self.hoja.subsurface(self.hoja.get_clip())
        self.rect = self.imagen.get_rect()
        self.rect.topleft = posicion
        self.figura = 0
        self.estados_izq = {
            0: (0, 300, 100, 400),
            1: (200, 300, 300, 400),
            2: (400, 300, 500, 400),
        }
        self.estados_der = {
            0: (0, 100, 100, 200),
            1: (200, 100, 300, 200),
            2: (400, 100, 500, 200),
        }
        self.estados_arriba = {
            0: (0, 200, 100, 300),
            1: (200, 200, 300, 300),
            2: (400, 200, 500, 300),
        }
        self.estados_abajo = {
            0: (0, 0, 100, 100),
            1: (200, 0, 300, 100),
            2: (400, 0, 500, 100),
        }

    def get_figura(self, estados):
        self.figura += 1
        if self.figura > (len(estados) - 1):
            self.figura = 0
        return estados[self.figura]

    def corte(self, rect_cortado):
        if type(rect_cortado) is dict:
            self.hoja.set_clip(pygame.Rect(self.get_figura(rect_cortado)))
        else:
            self.hoja.set_clip(pygame.Rect(rect_cortado))
        return rect_cortado

    def actualizacion(self, direccion):
        if direccion == "izq":
            self.corte(self.estados_izq)
            self.rect.x -= 5
        if direccion == "der":
            self.corte(self.estados_der)
            self.rect.x += 5
        if direccion == "arriba":
            self.corte(self.estados_arriba)
            self.rect.y -= 5
        if direccion == "abajo":
            self.corte(self.estados_abajo)
            self.rect.y += 5

        if direccion == "quieto_izq":
            self.corte(self.estados_izq[0])
        if direccion == "quieto_der":
            self.corte(self.estados_der[0])
        if direccion == "quieto_arriba":
            self.corte(self.estados_arriba[0])
        if direccion == "quieto_abajo":
            self.corte(self.estados_abajo[0])

        self.imagen = self.hoja.subsurface(self.hoja.get_clip())

    def evento(self, event):
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.actualizacion("izq")
            if event.key == pygame.K_RIGHT:
                self.actualizacion("der")
            if event.key == pygame.K_UP:
                self.actualizacion("arriba")
            if event.key == pygame.K_DOWN:
                self.actualizacion("abajo")

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.actualizacion("quieto_izq")
            if event.key == pygame.K_RIGHT:
                self.actualizacion("quieto_der")
            if event.key == pygame.K_UP:
                self.actualizacion("quieto_arriba")
            if event.key == pygame.K_DOWN:
                self.actualizacion("quieto_abajo")

