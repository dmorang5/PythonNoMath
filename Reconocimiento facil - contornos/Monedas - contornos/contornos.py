# Para saber la version 
"""import cv2
print(cv2.__version__)
"""

import cv2

ruta_imagen = r"D:\UDEMY\Python para no matematicos De 0 hasta reconocimiento facial\Reconocimiento facil - contornos\Monedas - contornos\contorno.jpg"
imagen = cv2.imread(ruta_imagen)

if imagen is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta.")
else:
    # Pasamos a escala de gris la imagen
    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

_,umbral = cv2.threshold(grises, 100, 255, cv2.THRESH_BINARY)
# _ es para var ficticia

# Obtener contornos
contorno, jerarquía = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar nuestros contornos
cv2.drawContours(imagen, contorno, -1, (251, 60, 50), 3) #(1 es para poner que contorno, 2, es para dos contornos, -1 es para todos)

# Mostrar
cv2.imshow('Imagen original', imagen)
#cv2.imshow('Imagen en grises', grises)
#cv2.imshow('Imagen con umbral', umbral)
cv2.waitKey(0) #1 para videos o cámara y 0 para imagen
cv2.destroyAllWindows()

