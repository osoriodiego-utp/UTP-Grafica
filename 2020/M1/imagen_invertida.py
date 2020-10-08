
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import math
print("Clase 2020/09/17 - Imágen invertida")


img_orig = io.imread("lena.png")
plt.figure("Imagen original")
plt.imshow(img_orig, vmin=0, vmax=1)

img_invert = 255 - img_orig
plt.figure("Imagen invertida")
plt.imshow(img_invert, vmin=0, vmax=1)

plt.show()