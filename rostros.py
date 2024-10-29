# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:15:18 2024

@author: meera
"""

import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread('colombia.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=11, minSize=(30,30))

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (250,0,0),2)

cv2.imshow('ROSTROS DETECTADOS', img)

cv2.waitKey(0)
cv2.destroyAllWindows()