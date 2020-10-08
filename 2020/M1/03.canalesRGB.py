
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
print("Modulo 1 - Tratamiento de imágenes usando geometría vectorial")
print("\t Canales RGB")


# === === === CANALES RGB === === ===
# === === === === === === === === ===

plt.rcParams['image.cmap'] = 'gray'

image_rgb = io.imread("lena.png")/255.0

plt.subplot(221)
plt.imshow(image_rgb)
plt.title("Imagen Original")

plt.subplot(222)
plt.imshow(image_rgb[:, :, 0])
plt.title("Imagen Rojo")

plt.subplot(223)
plt.imshow(image_rgb[:, :, 1])
plt.title("Imagen Verde")

plt.subplot(224)
plt.imshow(image_rgb[:, :, 2])
plt.title("Imagen Azul")

plt.show()

print("Dimensiones de la imagen: ", image_rgb.shape)


# === === === DESCOMPSOSICIÓN RGB === === ===
# === === === === === === === === === === ===

image_rgb = io.imread("lena.png")/255.0
print("Dimensiones de la imagen: ", image_rgb.shape)

#Image_rgb[:,:,N] = 0   >> se está igualando a cero(para RGB) la capa N // 0:red 1:green 2:blue
#Image_rgb[:,:,N] = 0   >> se está igualando a uno(para RGB) la capa N // 0:red 1:green 2:blue

image_red = np.copy(image_rgb)
image_red[:, :, 1] = 1
image_red[:, :, 2] = 1
print(image_red)
plt.figure()
plt.subplot(221)
plt.title("Imagen canal rojo")
plt.imshow(image_red)

image_green = np.copy(image_rgb)
image_green[:, :, 0] = 1
image_green[:, :, 2] = 1
# print(image_green)
# plt.figure()
plt.subplot(222)
plt.title("Imagen canal verde")
plt.imshow(image_green)

image_blue = np.copy(image_rgb)
image_blue[:, :, 0] = 1
image_blue[:, :, 1] = 1
# print(image_blue)
# plt.figure()
plt.subplot(223)
plt.title("Imagen canal azul")
plt.imshow(image_blue)

image_not_blue = np.copy(image_rgb)
image_not_blue[:,:,2]=0
plt.subplot(224)
plt.title("Imagen sin canal azul")
plt.imshow(image_not_blue)


plt.show()