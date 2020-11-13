import math
#implementar una funcion para transladar un punto
def trans(t,p):
    xp = t[0] + p[0]
    yp = t[1] + p[1]
    pp = [xp,yp]
    return pp

#translacion en el plano cartesiano
def transcartesiano(c,p): #pasa de coordenadas cartesianas a pantalla
    xp = c[0] + p[0]
    yp = c[1] - p[1]
    pp = [xp,yp]
    return pp

def transpantalla(c,p): #pasa de coordenadas de pantalla a coordenadas cartesianas
    xp = p[0] - c[0]
    yp = c[1] - p[1]
    pp = [xp,yp]
    return pp

#transladar al centro
def transcentro(c,p):
    xp = c[0] - p[0]
    yp = c[1] - p[1]
    pp = [xp,yp]
    return pp

#transladar punto original
def transoriginal(c,p):
    xp = c[0] + p[0]
    yp = c[1] + p[1]
    pp = [xp,yp]
    return pp

#implementar una funcion para rotar un punto
def rotar(r,p): #rotacion antihoraria
    coseno = math.cos(math.radians(r))
    seno = math.sin(math.radians(r))
    xp = p[0]*coseno - p[1]*seno
    yp = p[0]*seno + p[1]*coseno
    pp = [xp,yp]
    return pp


def rotar2(r,p): #rotacion horaria
    coseno = math.cos(math.radians(r))
    seno = math.sin(math.radians(r))
    xp = p[0]*coseno + p[1]*seno
    yp = p[1]*coseno - p[0]*seno
    pp = [xp,yp]
    return pp

#implementar una funcion para escalar un punto
def escalar(p,e):
    xp = p[0]*e[0]
    yp = p[1]*e[1]
    pp = [xp,yp]
    return pp

def polar(cartesiana): #pasa de coordenadas [x,y] cartesianas a polares [angulo,r]
    r = math.sqrt(math.pow(cartesiana[0],2) + math.pow(cartesiana[1],2))
    a = math.degrees(math.asin(cartesiana[1]/r))
    pp = [a,r]
    return pp

def cartesiana(polar): #pasa de coordenadas polares [angulo,r] a cartesianas [x,y]
    x = polar[1] * math.cos(math.radians(polar[0]))
    y = polar[1] * math.sin(math.radians(polar[0]))
    pp = [x,y]
    return pp
