
#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Modulo 1 - Tratamiento de imágenes usando geometría vectorial")
print("\t Lectura de imágenes")


from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import math


image = io.imread("/home/nano/UTP/Grafica/01/logoutp.png")/255.0
# image = io.imread("logoutp.png")/255.0
# https://carrerasuniversitarias.com.co/logos/original/logo-universidad-tecnologica-de-pereira.png
print("Dimensiones de la imagen: ", image.shape)
plt.imshow(image, vmin=0, vmax=1)
plt.show()

image_invertida = 0.255-image
print("Dimensiones imagen invertida: ", image_invertida.shape)
plt.imshow(image_invertida, vmin=0, vmax=1)
plt.show()
