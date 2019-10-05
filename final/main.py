import pygame

import jugador

import pytmx
tmxdata = pytmx.TiledMap("maps/map1.tmx")
#--
from pytmx import load_pygame
tmxdata = load_pygame("maps/map1.tmx")
#--
image = tmx_data.get_tile_image(x, y, layer)
screen.blit(image, position)



pygame.init()

widht = 640
height = 640

pantalla = pygame.display.set_mode((widht, height))
pygame.display.set_caption("Maps")
reloj = pygame.time.Clock()
game_over = False
jugador = jugador.xena((widht / 2, height / 2))

imagen = pygame.image.load("img/map1.png")

while game_over == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    jugador.evento(event)
    pantalla.blit(imagen, (0, 0))
    pantalla.blit(jugador.imagen, jugador.rect)

    pygame.display.flip()
    reloj.tick(15)
pygame.quit()
