
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
print("Modulo 1 - Tratamiento de imágenes usando geometría vectorial")
print("\t Canales RGB")


# === === === CANALES CMYK === === ===
# === === === === === === === === ===


image_cmyk = io.imread("lena.png")/255.0
factor = 255

print("Dimensiones de la imagen: ", image_cmyk.shape)
filas = image_cmyk.shape[0]
columnas = image_cmyk.shape[1]
print("Filas: ", filas, "Columnas: ", columnas)
# print("Cols: ", columnas)

plt.show()
