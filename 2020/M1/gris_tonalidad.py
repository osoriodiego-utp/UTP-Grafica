
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from skimage import io
import matplotlib.pyplot as plt
import numpy as np
print("Clase 2020/09/17 - Imágen en grises")
plt.rcParams['image.cmap'] = 'gray'

# Original
img_orig = io.imread("lena.png")
plt.figure("Imagen original")
plt.imshow(img_orig, vmin=0, vmax=1)

# Escala de grises - Promedio(average)
img_gray = np.copy(img_orig)
R = img_gray[:, :, 0]
G = img_gray[:, :, 1]
B = img_gray[:, :, 2]

plt.show()