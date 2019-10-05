import sys, pygame
from pygame.locals import *

from random import randint

#costantes
Width = 600
Height = 400
color = (255,0,0)
color2 = pygame.Color(255,255,255)
pygame.init()

ventana = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Hola mundo")

#pygame.draw.circle(ventana, (50,150,200), (200,200), 50)
#pygame.draw.rect(ventana, color, (250,250,300,100))
#pygame.draw.polygon(ventana, color, ((200,90),(240,150),(550,200),(500,40),(570,100)))



#posX = randint(10,(Width-300))
#posY = randint(10, (Height-300))
posX, posY = 100, 70
velocidad = 5
bandera = True
imagen = pygame.image.load("img/link2.png")
rectan2 = imagen.get_rect()
rectan3 = pygame.Rect(100, 70, 256, 256)
rectan = pygame.Rect(0,0,100,50)


while True:
    ventana.fill(color2)
    #pygame.draw.line(ventana,color,(0,0),(120,200),5)
   # ventana.blit(imagen,(posX,posY))
    #pygame.draw.rect(ventana,color,rectan2)
    ventana.blit(imagen,(posX,posY))
    pygame.draw.rect(ventana,color,rectan)
    rectan.left, rectan.top = pygame.mouse.get_pos()
    
    if rectan. colliderect(rectan3):
        velocidad = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        """
        posX, posY = pygame.mouse.get_pos()
        posX = posX -150
        posY = posY -150
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                posX -= velocidad
            elif event.key == K_RIGHT:
                posX += velocidad
                """
    if bandera == True:
        if posX < 500:
            posX += velocidad
            rectan3.left = posX 
        else:
            bandera = False
    else:
        if posX > 1:
            posX -= velocidad
            rectan3.left =posX 
        else:
            bandera = True
    pygame.display.update()

