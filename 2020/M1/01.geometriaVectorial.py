
print(" == Unidad 1 . Geometria vectorial ==")

import math

# Definicion de funciones


def toDegree(ang):
    return(ang*math.pi/180)


def toRadians(ang):
    return(ang*180/math.pi)


def catOpuesto(size, ang):
    # return(size * math.sin(ang*math.pi/180))
    return(size * math.sin(toDegree(ang)))


def catAdyacente(size, ang):
    return(size * math.cos(toDegree(ang)))


def modulo(x, y):
    return(math.sqrt(pow(x, 2) + pow(y, 2)))


def angulo(x, y):
    # return (toDegree(math.atan(y/x)))
    return (math.atan(y/x)*180/math.pi)


def ejemplo():
    Ax = 5
    Ay = 2

    Bx = 4
    By = 6

    Cx = catAdyacente(4, 25)
    Cy = catOpuesto(4, 25)

    Dx = catAdyacente(6, 30)
    Dy = catOpuesto(6, -30)

    Sx = Ax+Bx+Cx+Dx
    Sy = Ay+By+Cy+Dy

    print("Sxy: ", Sx, Sy)


def coordenadas(vector):  # vector = (longitud, angulo)
    res = []
    Ax = vector[0]*math.cos(toDegree(vector[1]))
    Ay = vector[0]*math.sin(toDegree(vector[1]))
    res.append(round(Ax, 2))
    res.append(round(Ay, 2))
    return tuple(res)


def sumVectores(vector):    # [vector de tuplas]
    Sx = 0
    Sy = 0
    for i in vector:
        print(i)
        Sx = Sx + i[0]
        Sy = Sy + i[1]
    return tuple((round(Sx, 2), round(Sy, 2)))


print(sumVectores([(9.40, 3.42), (9.71, 7.05), (-6.93, 4.00), (-18.00, 0.0), (-10.5, -21.6)]))
