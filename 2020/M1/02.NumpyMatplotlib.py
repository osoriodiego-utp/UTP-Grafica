
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

# ==========

b = np.array([0, 1, 2, 3])
print("B: ", b)
x = len(b)
print("El tamaño del vector B es: ", x)
print("El número de elementos de B es: ", b.size)

# === Tamaño del vector

bm = np.array([[2, 5, 1], [5, 6, 3, ], [8, 9, 2], [5, 6, 7]])
print(bm)
print("El tamaño del vector BM es: ", len(bm))
print("El número de elementos de BM es: ", bm.size)

# === Suma de los elementos de un vector
s = 0
for i in range(0, len(b)):
    s = s + b[i]
print("La suma de los elementos de B es: ", s)
print("La suma de elementos usando NUMPY es: ", np.sum(b))

# === Suma de vectores
a = np.array([9.4, 3.42])
b = np.array([9.71, 7.05])
c = np.array([-6.93, 4])
x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
plt.plot(x, y)
plt.plot(x, y, 'o')
plt.show()
a = np.array([2, 4, 0])
b = np.array([-2,-10,0])
p_punto = sum(np.multiply(a,b))
print("Producto punto 'np.multiply()' es: ", p_punto)
p_punto = np.dot(a, b)
print("Producto punto 'np.dot()' es: ", p_punto)

# === Producto cruz
p_cruz = np.cross(a, b)
print("Producto punto 'np.cross()' es: ", p_cruz)

# === Vector con valores aleatorios (0,1)
# np.random.rand(numero_elementos)
a = np.random.rand(5)
print(" Vector aleatorio (0,1): ", a)

# === Vector con valores aleatorios gaussianos
# np.random.randn(numero_elementos)
b = np.random.randn(5)
print(" Vector aleatorio gaussiano: ", b)

# === Vector de unos
# np.ones((numero_elementos))
a = np.ones((10))
print("vector de 1's: \n", a)

# === Matriz de unos
# np.ones((elementos_x, elementos_y))
am = np.ones((10,15))
print("Matriz de 1's: \n", am)

# === Vector de ceros

# === Matriz de ceros

# === Matriz de identidad

# === Matriz con elementos del vector en la diagonal
dm = np.diag(np.array([1,2,3,4]))
print("Matriz diagonal: \n", dm)

# === Arreglos según un número de puntos


# === Arreglos uniformemente espaciados

# === Gráfica de un vector - matplotlib
x = np.linspace(0, 3, 20)
y = np.linspace(0, 3, 20)
plt.plot(x, y)
plt.plot(x, y, 'o')
plt.show()

# === Gráfica matrices
image = np.random.rand(30, 30)
plt.imshow(image, cmap=plt.cm.hot)
plt.colorbar()
plt.show()
