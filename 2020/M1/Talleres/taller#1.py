
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

# 1) Cree el siguiente vector A= [2, 3,5, 1, 4 ,7 9, 8, 6, 10]
a = np.array([2, 3, 5, 1, 4, 7, 9, 8, 6, 10])
print("01. ", a)

# 2) Cree un vector B que contenga los elementos desde el 11 hasta el 20 (utilice subscripts)
b = np.arange(11, 21, 1)
print("02. ", b)

# 3) Componer un vector C formado por los vectores A y B en la misma fila respectivamente
# c = np.array([a, b])
c = np.arange(2, 21, 1)
print("03. ", c)

# 4) encuentre el valor mínimo en el vector C haciendo uso de la función propia de Numpy
minimo = np.amin(c)
print("04. ", minimo)

# 5) encuentre el valor máximo en el vector C haciendo uso de la función propia de Numpy
maximo = np.amax(c)
print("05. ", maximo)

# 6) encuentre la longitud en el vector C haciendo uso de la función propia de Numpy
longitud = np.size(c)
print("06. ", longitud)

# 7) encuentre la suma de los elementos el vector C haciendo uso de la función propia de Numpy
sumatoria = np.sum(c)
print("07. ", sumatoria)

# 8) Encuentre el promedio de los elementos en el vector C haciendo uso de las operaciones elementales suma y división


def prom(vector):
    suma = 0
    for i in vector:
        suma = suma + i
    return (suma/len(vector))


print("08. ", prom(c))

# 9) Encuentre el promedio en el vector C haciendo uso de la función propia de Numpy
promedio = np.average(c)
print("09. ", promedio)

# 10) Encuentre la media en el vector C haciendo uso de la función propia de Numpy
media = np.median(c)
print("10. ", media)

# 11) Encuentre la suma en el vector C haciendo uso de la función propia de Numpy
suma = np.sum(c)
print("11. ", suma)

# 12) Cree un vector D a partir del vector C con los elementos mayores que 5
vector_cinco = []
for i in c:
    if(i > 5):
        vector_cinco.append(i)
print("12. ", vector_cinco)

# 13) Cree un vector E a partir del vector C con los elementos mayores que 5 y menores que 15
vector_cinco_quince = []
for i in c:
    if(i > 5 and i < 15):
        vector_cinco_quince.append(i)
print("13. ", vector_cinco_quince)

# 14) Cambie los elementos 5 y 15 elemento del vector C por ‘7’
vector_siete = []
for i in range(0, len(c)):
    if(i == 5 or i == 15):
        vector_siete.append(7)
    else:
        vector_siete.append(c[i])
print("14. ", vector_siete)

# 15) Determine la moda del vector C
moda = np.bincount(a)
print("15. ", np.argmax(moda))

# 16) Ordene el Vector C de menor a mayor
vector_ordenado = sorted(c)
vector_ordenado_invertido = sorted(c, reverse=True)
print("16. ", vector_ordenado)

# 17) Multiplique el vector C por 10
vector_diez = []
for i in range(0, len(c)):
    vector_diez.append(c[i]*10)
print("17. ", vector_diez)

# 18) Cambie los elementos del 6 al 8 de la matriz C por 60, 70 y 80 respectivamente
vector_seis_ocho = []
for i in range(0, len(c)):
    if(c[i] >= 6 and c[i] <= 8):
        vector_seis_ocho.append(c[i]*10)
    else:
        vector_seis_ocho.append(c[i])
print("18. ", vector_seis_ocho)

# 19) Cambie los elementos del 14 al 16 de la matriz C por 140, 150 y 160 respectivamente
vector_catorce = []
for i in range(0, len(c)):
    if(c[i] >= 14 and c[i] <= 16):
        vector_catorce.append(c[i]*10)
    else:
        vector_catorce.append(c[i])
print("19. ", vector_catorce)
