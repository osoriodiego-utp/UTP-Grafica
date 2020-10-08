
#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Modulo 1 - Tratamiento de imágenes usando geometría vectorial")
print("\t Graficando funciones.")


import matplotlib.pyplot as plt
import numpy as np
import math


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2.1, 2.1, 3.2, 3.5, 4.1, 6.2, 5.2, 6.3, 7.1, 4.3]
plt.figure()
plt.plot(x, y)   # Gráfica con linea continua
plt.title("Graficar vectores")
plt.plot(x, y, 'o')  # Gráfica con linea punteada
plt.show()

# Vectores linspace
x = np.linspace(0, 3, 20)
y = np.linspace(0, 3, 20)
plt.figure()
plt.title("Graficar vectores usando matplotlib (arreglos 1D")
plt.plot(x, y)
plt.plot(x, y, 'o')
plt.show()


# Graficar una función ============================
xx = np.linspace(0, 2*math.pi, 100)
yy = np.sin(xx)
plt.figure()
plt.title("Graficar función Seno")
plt.plot(xx, yy)
plt.grid(True)
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()


# Nuestra propia función Seno ============================


def factorial(n):
    if n == 0 or n == 1:
        res = 1
    elif n > 1:
        res = n*factorial(n-1)
    else:
        return"NaN"
    return res


def seno(x):
    suma = 0
    termino = 0
    n = 0
    aportemin = 0.00001
    while(True):
        termino = ((-1)**n)/(factorial(2*n+1))*x**(2*n+1)
        suma = suma+termino
        n = n+1
        if(math.fabs(termino) < aportemin):
            break
    return suma


plt.figure()
plt.title("Nuestra propia función Seno")
plt.grid(True)
plt.xlabel("Eje x")
plt.ylabel("Eje y")
x = np.linspace(0, 2*math.pi, 100)
i = 0
while(i < 100):
    y = seno(x[i])
    plt.plot(x[i], y, '.')
    i = i+1
plt.show()
