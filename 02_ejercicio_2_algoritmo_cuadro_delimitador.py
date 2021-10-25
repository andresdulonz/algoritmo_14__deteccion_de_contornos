import cv2

img_1 = cv2.imread('imagen_1.png')

# Imagen, centro circunferencia, radio, color, ancho cicunferencia
cv2.circle(img_1, (710,100), 50, (255,255,255), -1)
cv2.circle(img_1, (300,276), 75, (255,255,255), -1)
cv2.circle(img_1, (150,220), 27, (255,255,255), -1)
cv2.circle(img_1, (620,425), 64, (255,255,255), -1)

gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)

# Detectar el contorno exterior, poca cantidad de puntos para el contorno
cnts, h = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Buscar las coordenadas de cada cuadro delimitador
for c in cnts:
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(img_1, (x,y), (x+w,y+h), (0,0,255), 2)

cv2.imwrite('imagen_cuadro_delimitado.png', img_1)
cv2.imshow('Imagen', img_1)
cv2.waitKey()