# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:02:04 2024

@author: meera
"""
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# Cargar la imagen
image = cv2.imread('rostro.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectar rostros
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Dibujar rectángulos alrededor de los rostros y agregar nombres
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.putText(image, 'Andrea', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

cv2.imshow('Rostro detectado', image)
cv2.waitKey(0)
cv2.destroyAllWindows()