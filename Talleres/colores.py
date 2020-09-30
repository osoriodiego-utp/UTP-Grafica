
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import math
print("\nTALLER#4 - Tratamiento de imágenes")

plt.rcParams['image.cmap'] = 'gray'  # Ver imágenes en escala de grises

# 1.Elaborar un procedimiento que diseñe la siguiente matriz.
# (ver imagen)

filas = 6
columnas = 11
capas = 3

colors = np.ones((filas, columnas, capas))
cyan = [0, 1, 1]
magenta = [1, 0, 1]
yellow = [1, 1, 0]
white = [1, 1, 1]
grey = [1*0.5, 1*0.5, 1*0.5]
black = [0, 0, 0]
red = [1, 0, 0]
green = [0, 1, 0]
blue = [0, 0, 1]


for row in range(0, filas-2):
    for col in range(0, columnas):
        if(col == 0):
            colors[row, col] = yellow
        if((col == 1) or (col == 2)):
            colors[row, col] = cyan
        if((col == 3) or (col == 4)):
            colors[row, col] = green
        if((col == 5) or (col == 6)):
            colors[row, col] = magenta
        if((col == 7) or (col == 8)):
            colors[row, col] = red
        if((col == 9) or (col == 10)):
            colors[row, col] = blue

for row in range(4, filas):
    for col in range(0, columnas):
        g = (10-col)/10
        colors[row, col] = [1*g, 1*g, 1*g]


plt.title("Matriz de colores")
plt.imshow(colors)
plt.show()
