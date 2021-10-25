import cv2

img_1 = cv2.imread('imagen_1.png')

# Imagen, centro circunferencia, radio, color, ancho cicunferencia
cv2.circle(img_1, (500,100), 50, (255,255,255), -1)
cv2.circle(img_1, (300,300), 50, (255,255,255), -1)

# Imagen, posicion x, posicion y, ancho, alto, color, grosor de linea
cv2.rectangle(img_1, (75,85), (175,150), (255,255,255), -1)
cv2.rectangle(img_1, (125,425), (500,475), (255,255,255), -1)
cv2.rectangle(img_1, (560,222), (734,425), (255,255,255), -1)

gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)

# Detectar el contorno exterior, poca cantidad de puntos para el contorno
cnts, h = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img_1, cnts, -1, (0,255,0), 3)

cv2.imwrite('imagen_deteccion_contorno.png', img_1)
cv2.imshow('Imagen', img_1)
cv2.waitKey()