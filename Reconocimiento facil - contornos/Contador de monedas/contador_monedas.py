# Importaciones de lib
import cv2
import numpy as np

# Variables para utilizar GaussianBlur. Deben ser valores impares
valorGauss = 3

# Variables para la matriz kernel
valorKernel = 3

# Ruta imagen
ruta_imagen = r"D:\UDEMY\Python para no matematicos De 0 hasta reconocimiento facial\Reconocimiento facil - contornos\Contador de monedas\monedas-2.jpg"

# Leemos la imagen
original = cv2.imread(ruta_imagen)

if original is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta.")
else:
    # Pasamos a escala de gris la imagen
    gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

# Suavizado para imagenes borrosas - Desenfoque gausiano
gauss = cv2.GaussianBlur(gris, (valorGauss, valorGauss), 0)

# canny: Eliminar ruidos
canny = cv2.Canny(gauss, 60, 100)

# Numpy
# Decir que contornos me interesa
kernel = np.ones((valorKernel, valorKernel), np.uint8)

#Cierre de contornos
cierre = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel) # MORPH_CLOSE es para dentro del contorno, MORPH_OPEN es para fuera del contorno 

# Obtener contornos
contornos, jerarquía = cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#print("Monedas encontradas: {}".format(len(contornos)))

# Dibujar los contornos
cv2.drawContours(original, contornos, -1,  (251, 60, 50), 3)

# Mostrar resultados
cv2.imshow("Imagen", original)
#cv2.imshow("Grises", gris)
#cv2.imshow("Gauss", gauss)
#cv2.imshow("Canny", canny)
#cv2.imshow("Cierre", cierre)

cv2.waitKey(0)
