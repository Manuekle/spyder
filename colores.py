# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:01:13 2024

@author: meera
"""

import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('coloresimg.jpg')

# Convertir a HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Definir rangos de colores en HSV
color_ranges = {
    'amarillo': ((20, 100, 100), (30, 255, 255)),
    'rojo': ((0, 100, 100), (10, 255, 255)),
    'azul': ((100, 150, 0), (140, 255, 255)),
    'verde': ((40, 100, 100), (70, 255, 255))
}

# Detectar cada color y mostrar el resultado
for color, (lower, upper) in color_ranges.items():
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow(f'Deteccion de {color}', result)

cv2.waitKey(0)
cv2.destroyAllWindows()

