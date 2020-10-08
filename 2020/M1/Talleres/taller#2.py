
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt
print("\nTALLER #2 - Trabajando con matrices.")

# 1. Crear una matriz de numero reales 2x4:
# M=  |0 2 4 6|
#     |0 3 5 7|

matrix_string = '0 2 4 5; 0 3 5 7'
matrix = np.matrix(matrix_string)


# Guardar la variable M en el fichero matriz.mat, a continuación limpiar el
# espacio de trabajo y volver a cargar el fichero, comprobando que la variable
# está en memoria.

archivo = open('matriz.mat', 'w')   # <== escritura
archivo.write(matrix_string)
archivo = open('matriz.mat', 'r')   # <== lectura
matrix2 = np.matrix(archivo.readline())
print("\nMatriz leida desde \'matriz.mat\ '\n", matrix2)


# Por ultimo selecciona la segunda fila, la cuarta columna y las submatriz
# formada por las dos primeras filas y las dos primeras columnas.


print("\nElemento en [2][4]: \n", matrix2[[1], [3]])
print("\nSubmatriz: \n", matrix2[0:2, 0:2])


# 2. Definir las siguientes matrices en Matlab:
# A=  |1 3 5 8|   B=  | 1  9  5  8|   C=  | 1  9|
#     |2 6 5 3|       |12  5  5  9|       |10  2|
#     |4 1 9 7|       | 4  2  9 74|
#     |1 8 0 2|       | 0  6  0  3|

A = np.matrix('1 3 5 8; 2 6 5 3; 4 1 9 7; 1 8 0 2')
print("\nMatriz A: \n", A)
B = np.matrix('1  9  5  8;12  5  5  9; 4  2  9 74; 0  6  0  3')
print("\nMatriz B: \n", B)
C = np.matrix('1 9; 10 2')
print("\nMatriz C: \n", C)


# Y realizar los diguientes cálculos básicos con estas matrices:
# > 3·A,
print("\nMultiplicación 3·A: \n", 3*A)

# > A-7,
print("\nResta A-7: \n", A-7)

# > A·B,
print("\nMultiplicación A·B: \n", A*B)

# > A^-1,
print("\nInversa A^1: \n", np.linalg.inv(A))

# > B^⁻1
print("\nInversa B^1: \n", np.linalg.inv(B))
