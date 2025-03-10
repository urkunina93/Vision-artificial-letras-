import cv2
import numpy as np

  
img = cv2.imread('img.jpg',0)  # Leemos la imagen
img = cv2.resize(img,None,fx=0.8, fy=0.8, interpolation = cv2.INTER_CUBIC)
height, width = img.shape[:2]  # Obtenemos sus dimensiones

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img1 = np.zeros((height, width, 3), np.uint8)  # Creamos una imagen nueva


#  Limites para el recorte 
ix,iy=1187,259
fx,fy=1289,294

for i in range(iy, fy):
    for j in range(ix, fx):    	
    	img1[i, j] = img[i, j]

alto=fy-iy
ancho=fx-ix
translation = np.float32([[1, 0, -ix], [0, 1, -iy]]) # trasladamos imagen recortada
img1 = cv2.warpAffine(img1, translation, (ancho, alto))

ret, thr = cv2.threshold(img1, 130 , 255, cv2.THRESH_BINARY) # umbrlizacion

canny = cv2.Canny(thr, 10, 150) # deteccion de bordes 
contornos,_ = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Buscamos los contornos
cv2.drawContours(img1,contornos,-1,(0,0,255), 1) # Dibujamos los contornos


cv2.imshow('Canny', np.hstack([img1, thr]))  # Mostramos las imagenes
cv2.waitKey(0)
cv2.destroyAllWindows()

zoom = cv2.resize(img1,None,fx=3, fy=3, interpolation = cv2.INTER_CUBIC)
cv2.imshow('zoom',zoom)
cv2.waitKey(0)
cv2.destroyAllWindows()