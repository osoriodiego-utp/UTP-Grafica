
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math
import pygame
from pygame.locals import *
import numpy as np

from color import *

pygame.init()

X, Y = 600, 600
CX, CY = X/2, Y/2
ventana = pygame.display.set_mode((X, Y))
print("\nTALLER#8 - Graficador")


# Elaborar un graficador básico usando la librería pygame y el material visto en clase