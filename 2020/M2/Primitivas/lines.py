import pygame
import math
import time

color = (50, 100, 150)
color2 = (100, 100, 100)
ini = (100, 200)
fin = (200, 100)

# pygame.init()
window = pygame.display.set_mode((800, 600))
# pygame.draw.rect(wondows)
pygame.draw.line(window, (255, 255, 0), (400, 50), (400, 550), 1)
pygame.draw.line(window, (255, 255, 0), (50, 300), (750, 300), 1)

# Arco
pygame.draw.arc(window, color, [50, 10, 300, 300], 0, math.radians(180))

# Cuadrado
pygame.draw.rect(window, color2, [150, 50, 400, 400], 0)


# Circulo
pygame.draw.circle(window, color, (30, 40), 80, 1)
pygame.draw.circle(window, color, (60, 70), 80, 1)
pygame.draw.circle(window, color, (90, 100), 80, 1)
pygame.draw.circle(window, color, (120, 130), 80, 1)

pygame.display.update()
time.sleep(2)
