import base64
import json
#import gzip
 
import pygame
from pygame import *
 
import sys
 
tileWidth = 0
tileHeigh = 0
 
def uploadMap(name):
    global mapWidth, mapHeight, tileHeight, tileWidth, matrizMapa
 
    aux = open(name + ".json", "r")
    data = json.load(aux)
    aux.close()
 
    tileWidth = data["tilewidth"]
    tileHeight = data["tileheight"]
 
    mapWidth = data["widht"]
    mapHeight =data["height"]
 
    #obtener mapa
    for item in data["layers"]:
        mapa = item["data"]
 
 
    #mapa = base64.decodestring(mapa)
 
    #Char to integer
    #salida = []
    #for i in 
 
    print(mapa)
 
# = = = = = = = = = = = = = = = = = =
 
def arrayTileset(img):
    pass 
 
def cut(img, rectangel):
    pass
 
def main():
    pygame.init()
    screen =pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Mapa")
    clock = pygame.time.Clock()
 
    img = pygame.image.load("./tileset.png")
    uploadMap("map1")
    while True:
        time = clock.tick(60)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
 
 
main()
