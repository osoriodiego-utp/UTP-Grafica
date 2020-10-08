
#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Modulo 1 - Tratamiento de imágenes usando geometría vectorial")
print("\t Graficando matrices.")


import math
import numpy as np
import matplotlib.pyplot as plt


# configuración necesaria para ver las imágenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

size = (50, 50)

imagen_negra = np.zeros(size)
# visualizar la matriz
# plt.figure()
plt.imshow(imagen_negra, vmin=0, vmax=1)
plt.show()

imagen_blanca = np.ones(size)
# visualizar la matriz
plt.figure()
plt.imshow(imagen_blanca, vmin=0, vmax=1)
plt.show()

imagen_gris = np.ones(size)*0.5
plt.figure()
plt.imshow(imagen_gris, vmin=0, vmax=1)
plt.show()

imagen_aleatoria = np.random.rand(size[0], size[1])
plt.figure()
plt.imshow(imagen_aleatoria, vmin=0, vmax=1)
plt.show()

