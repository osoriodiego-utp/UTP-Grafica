
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt
print("Taller #3 - Graficando funciones...sen(x), cos(x), tan(X) y transformadas.")

# 0. Preliminares


def factorial(n):
    if n == 0 or n == 1:
        res = 1
    elif n > 1:
        res = n*factorial(n-1)
    else:
        return"NaN"
    return res


# 1.Cree las funciones trigonométricas(misin, micos, mitan), exponencial y
# logarítmica a partir de la función dada. (ver imagen)


def misin(x):
    sumatoria = 0
    termino = 0
    n = 0
    aportemin = 0.00001
    while(True):
        termino = ((-1)**n)/(factorial(2*n+1))*x**(2*n+1)
        sumatoria = sumatoria+termino
        n = n+1
        if(math.fabs(termino) < aportemin):
            break
    return sumatoria


# Grafica función seno(x)
plt.figure()
plt.title("Función: misin(x)")
plt.grid(True)
plt.xlabel("Eje x")
plt.ylabel("Eje y")
x = np.linspace(0, 2*math.pi, 100)
i = 0
while(i < 100):
    y = misin(x[i])
    plt.plot(x[i], y, '.')
    i = i+1
# # plt.show()


def micos(x):
    sumatoria = 0
    termino = 0
    n = 0
    aportemin = 0.00001
    while(True):
        termino = ((-1)**n/factorial(2*n)) * (x**(2*n))
        sumatoria = sumatoria+termino
        n = n+1
        if(math.fabs(termino) < aportemin):
            break
    return sumatoria


# Grafica función coseno(x)
plt.figure()
plt.title("Función: micos(x)")
plt.grid(True)
plt.xlabel("Eje x")
plt.ylabel("Eje y")
x = np.linspace(0, 2*math.pi, 100)
i = 0
while(i < 100):
    y = micos(x[i])
    plt.plot(x[i], y, '.')
    i = i+1
# # plt.show()


def mitan(x):
    return (misin(x)/micos(x))


# Gráfica función tangente(x)
puntos = 50
plt.figure()
plt.title("Función: micos(x)")
plt.grid(True)
plt.xlabel("Eje x")
plt.ylabel("Eje y")
x = np.linspace(0, 3, puntos)
i = 0
while(i < puntos):
    y = mitan(x[i])
    plt.plot(x[i], y, '.')
    i = i+1
# # plt.show()


# 2. Sean las series de Fourier para las funciones donde T es el periodo.
# Programe el algoritmo en Matlab que permita generar la función haciendo
# uso de las funciones a partir de las series del punto anteior.
# Grafique usando subplot permitiendo ver para algunos armónicos del aporte.
# -Cuadrada(micuadrada())
# -Diente de Sierra(misierra())
# -Triangular(mitriangular())


def micuadrada(t):
    T = 10
    n = 1
    pi = 3.141592653589793
    sumatoria = 0
    termino = 0
    aportemin = 0.00001
    while(True):
        termino = ((1/n) * (math.sin(2*pi*n*t/T)))
        sumatoria = sumatoria+termino
        n = n+1
        if(math.fabs(termino) < aportemin):
            break
        return ((4/pi)*sumatoria)


puntos = 50
plt.figure()
plt.title("Función: micuadrada(x)")
plt.grid(True)
plt.xlabel("Eje x")
plt.ylabel("Eje y")
x = np.linspace(0, 10, puntos)
i = 1
while(i < (puntos-1)):
    y = (micuadrada(x[i]))
    plt.plot(x[i], y, '.')
    i = i+1
# plt.show()


def misierra(t):
    T = 10
    n = 1
    pi = 3.141592653589793
    sumatoria = 0
    termino = 0
    aportemin = 0.00001
    while(True):
        termino = ((1/n) * (math.sin(2*pi*n*t/T)))
        sumatoria = sumatoria+termino
        n = n+1
        if(math.fabs(termino) < aportemin):
            break
        return ((1/2) - (1/pi*sumatoria))


puntos = 50
plt.figure()
plt.title("Función: misierra(x)")
plt.grid(True)
plt.xlabel("Eje x")
plt.ylabel("Eje y")
x = np.linspace(0, 10, puntos)
i = 1
while(i < (puntos-1)):
    y = (misierra(x[i]))
    plt.plot(x[i], y, '.')
    i = i+1
# plt.show()


def mitriangular(t):
    T = 10
    n = 1
    pi = 3.141592653589793
    sumatoria = 0
    termino = 0
    aportemin = 0.00001
    while(True):
        termino = ((((-1)**((n-1)/2)) / n) * math.sin(2*pi*n*t/T))
        sumatoria = sumatoria+termino
        n = n+2
        if(math.fabs(termino) < aportemin):
            break
        return (8/(pi**2)*sumatoria)


puntos = 50
plt.figure()
plt.title("Función: mitriangular(x)")
plt.grid(True)
plt.xlabel("Eje x")
plt.ylabel("Eje y")
x = np.linspace(0, 10, puntos)
i = 1
while(i < (puntos-1)):
    y = (mitriangular(x[i]))
    plt.plot(x[i], y, '.')
    i = i+1
# plt.show()


plt.show()
