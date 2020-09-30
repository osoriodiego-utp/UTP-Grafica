
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import math
print("\nTALLER#4 - Tratamiento de imágenes")

plt.rcParams['image.cmap'] = 'gray'  # Ver imágenes en escala de grises

# [:,:,N]  N = 0 => Red / N = 1 => Green / N = 2 => Blue
IMG_RGB = io.imread("rgb.jpg")
plt.subplot(221)
plt.title("Imagen RGB-Original")
plt.imshow(IMG_RGB, vmin=0, vmax=1)

# [:,:,N]  N = 0 => Cyan / N = 1 => Magenta / N = 2 => Yellow
IMG_CMYK = io.imread("cmyk.jpg")
plt.subplot(224)
plt.title("Imagen CMYK-Original")
plt.imshow(IMG_CMYK, vmin=0, vmax=1)
factor = 255
filas = IMG_CMYK.shape[0]
columnas = IMG_CMYK.shape[1]

plt.show()


cyan = [0, 1, 1]
magenta = [1, 0, 1]
yellow = [1, 1, 0]
white = [1, 1, 1]
grey = [1*0.5, 1*0.5, 1*0.5]
black = [0, 0, 0]
red = [1, 0, 0]
green = [0, 1, 0]
blue = [0, 0, 1]

# 1.Elaborar un procedimiento que diseñe la siguiente matriz.
# (ver imagen)

mat_col = np.ones((3, 3, 3))
# -columna CMY
mat_col[0, 0] = cyan
mat_col[1, 0] = magenta
mat_col[2, 0] = yellow
# -columna B/W
mat_col[0, 1] = white
mat_col[1, 1] = grey
mat_col[2, 1] = black
# -columna RGB
mat_col[0, 2] = red
mat_col[1, 2] = green
mat_col[2, 2] = blue

plt.title("Matriz de colores [3]X[3]")
plt.imshow(mat_col)
plt.show()

# 2.Realizar un procedimiento que diseñe la siguiente imagen a través de una matriz.
# (ver imagen)
fils = 6
cols = 11
capas = 3
colors = np.ones((fils, cols, capas))

for row in range(0, fils-2):
    for col in range(0, cols):
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

for row in range(4, fils):
    for col in range(0, cols):
        g = (10-col)/10
        colors[row, col] = [1*g, 1*g, 1*g]


plt.title("Colores y Grises")
plt.imshow(colors)
plt.show()

# 3.Elaborar una función que invierta los colores de una imagen.
plt.subplot(221)
plt.title("Imagen RGB-Original")
plt.imshow(IMG_RGB, vmin=0, vmax=1)

img_invert = 255 - IMG_RGB
plt.subplot(224)
plt.title("Imagen negativo")
plt.imshow(img_invert, vmin=0, vmax=1)
plt.show()

# 4.Elaborar una función a la que se le envie de una imagen retorne su capa Roja.
img_red = np.copy(IMG_RGB)
img_red[:, :, 1] = 0  # Green=0
img_red[:, :, 2] = 0  # Blue=0

plt.subplot(222)
plt.title("Imagen Rojo")
plt.imshow(img_red)
# plt.show()

# 5.Elaborar una función a la que se le envie de una imagen retorne su capa Verde
img_green = np.copy(IMG_RGB)
img_green[:, :, 0] = 0  # Red=0
img_green[:, :, 2] = 0  # Blue=0

plt.subplot(223)
plt.title("Imagen Verde")
plt.imshow(img_green)
# plt.show()

# 6.Elaborar una función a la que se le envie de una imagen retorne su capa Azul.
img_blue = np.copy(IMG_RGB)
img_blue[:, :, 0] = 0  # Red=0
img_blue[:, :, 1] = 0  # Green=0

plt.subplot(224)
plt.title("Imagen Blue")
plt.imshow(img_blue)
plt.show()

# 7.Elaborar una función a la que se le envie de una imagen y retorne la imagen
# en Magenta.
img_magenta = np.copy(IMG_CMYK)
img_magenta[:, :, 0] = np.ones((filas, columnas))*factor
img_magenta[:, :, 2] = np.ones((filas, columnas))*factor
plt.subplot(222)
plt.title("Imagen Magenta")
plt.imshow(img_magenta)
# plt.show()

# 8.Elaborar una función a la que se le envie de una imagen y retorne la imagen
# en Cyan.
img_cyan = np.copy(IMG_CMYK)
img_cyan[:, :, 1] = np.ones((filas, columnas))*factor
img_cyan[:, :, 2] = np.ones((filas, columnas))*factor
plt.subplot(223)
plt.title("Imagen Cyan")
plt.imshow(img_cyan)
# plt.show()

# 9.Elaborar una función a la que se le envie de una imagen y retorne la imagen
# en Amarillo.
img_yellow = np.copy(IMG_CMYK)
img_yellow[:, :, 0] = np.ones((filas, columnas))*factor
img_yellow[:, :, 1] = np.ones((filas, columnas))*factor
plt.subplot(224)
plt.title("Imagen Amarillo")
plt.imshow(img_yellow)
plt.show()

# 10.Elaborar una función en  la que le envie por separado las capas RGB y con base
# en ellas reconstruya la imagen en colores(R,G,B) = ORIGINAL

# 11.Elaborar una función a la que se le envie 2 imágenes y que me retorne la fusión
# de las dos imágenes sin ecualizar.
image1 = io.imread("cactus.jpg")/255.0
factor1 = 0.5
image2 = io.imread("desierto.jpg")/255.0
factor2 = 0.25

plt.subplot(221)
plt.imshow(image1)
plt.title("Img 1")

plt.subplot(222)
plt.imshow(image2)
plt.title("Img2")

image3 = image1*factor1 + image2*factor2
plt.subplot(224)
plt.imshow(image3)
plt.title("Imagenes fusionadas")

plt.show()

# 12.Elaborar una función a la que se le envie 2 imágenes y que me retorne la
# fusión de las dos imágenes ecualizadas.

# 13.Elaborar una función a la que se le envie una imagen y un factor y retorne la
# imagen ecualizada según el factor.

# 14.Elaborar una función a la que se le envie una imagen y que retorne la imagen
# con la Técnica de promedio(Average).

# 15.Elaborar una función a la que se le envie una imagen y que retorne la imagen
# en escala de grises con la técnica de promedio(Average).
img_gray_average = np.copy(IMG_RGB)/255
R = img_gray_average[:, :, 0]
G = img_gray_average[:, :, 1]
B = img_gray_average[:, :, 2]

img_gray_average = ((R+G+B)/3)

plt.subplot(222)
plt.title("Imagen gris - average")
plt.imshow(img_gray_average)

# plt.show()

# 16.Elaborar una función a la que se le envie una imagen y que retorne la imagen
# en escala de grises con latécnica de Luminosidad(Luminosity).
img_gray_luminosity = np.copy(IMG_RGB)/255
R = img_gray_luminosity[:, :, 0]
G = img_gray_luminosity[:, :, 1]
B = img_gray_luminosity[:, :, 2]

img_gray_luminosity = (0.2989*R) + (0.5870*G) + (0.1140*B)

plt.subplot(223)
plt.title("Imagen gris - luminosity")
plt.imshow(img_gray_luminosity, vmin=0, vmax=1)

# plt.show()

# 17.Elaborar una función a la que se le envie una imagen y que retorne la imagen
# en escala de grisescon latécnica de La tonalidad(Midgray).
img_gray_midgray = np.copy(IMG_RGB)/255
R = img_gray_midgray[:, :, 0]
G = img_gray_midgray[:, :, 1]
B = img_gray_midgray[:, :, 2]

for x in range(filas):
    for y in range(columnas):
        img_gray_midgray[x, y] = max(
            R[x, y], G[x, y], B[x, y])+min((R[x, y], G[x, y], B[x, y]))/2

plt.subplot(224)
plt.title("Imagen gris - midgray")
plt.imshow(img_gray_luminosity, vmin=0, vmax=1)

plt.show()
