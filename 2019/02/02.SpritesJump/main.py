import pygame
import jugador

pygame.init()

widht = 600
height = 400

pantalla = pygame.display.set_mode((widht,height))
pygame.display.set_caption("Xena")
reloj = pygame.time.Clock()
game_over = False
jugador = jugador.xena((widht/2,height/2))

while game_over == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    jugador.evento(event)
    pantalla.fill(pygame.Color('white'))
    pantalla.blit(jugador.imagen, jugador.rect)

    pygame.display.flip()
    reloj.tick(25)
pygame.quit()
