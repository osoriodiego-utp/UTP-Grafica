
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from skimage import io
import matplotlib.pyplot as plt
import numpy as np
print("Clase 2020/09/17 - Imágen en grises")
plt.rcParams['image.cmap'] = 'gray'


# Original
img_orig = io.imread("rgb.jpg")/255

# Escala de grises - Promedio(average)
img_gray = np.copy(img_orig)

R = img_gray[:, :, 0]
G = img_gray[:, :, 1]
B = img_gray[:, :, 2]

img_gray = (0.2989*R) + (0.5870*G) + (0.1140*B)
plt.figure("Img escala de grises")
plt.imshow(img_gray, vmin=0, vmax=1)

# Histograma de la imagen(escala de grises)
histograma = np.trunc(np.around(img_gray*255, 0))
plt.figure("Histrograma")
plt.hist(histograma.ravel(), 256, [0, 256])


plt.show()
