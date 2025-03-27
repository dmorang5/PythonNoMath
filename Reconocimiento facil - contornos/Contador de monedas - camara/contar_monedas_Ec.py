""" import cv2 as cv
import numpy as np

def contar_monedas(imagen):
    grises = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(grises, (5, 5), 1)
    _, umbral = cv.threshold(blur, 100, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    contornos, _ = cv.findContours(umbral, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    # Definir los rangos de área para cada moneda
    valores_monedas = {
        "5 centavos": (79.0000, 80.1638),
        "10 centavos": (65.0000, 67.6913),
    }
    
    conteo = {key: 0 for key in valores_monedas}
    
    for contorno in contornos:
        area = cv.contourArea(contorno)
        print(f"Área detectada: {area}")  # Depuración
        
        M = cv.moments(contorno)
        if M["m00"] == 0:
            continue
        x = int(M["m10"] / M["m00"])
        y = int(M["m01"] / M["m00"])
        
        for moneda, (min_area, max_area) in valores_monedas.items():
            if min_area <= area <= max_area:
                conteo[moneda] += 1
                cv.putText(imagen, f"{moneda}", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                break
    
    # Sumar la cantidad total de monedas
    total_monedas = sum(conteo.values())
    print(f"Hay {total_monedas} monedas detectadas.")
    
    return imagen

# Captura de video
detector = cv.VideoCapture(1)
if not detector.isOpened():
    print("No se encontró una cámara")
    exit()

while True:
    _, frame = detector.read()
    if not _ or frame is None:
        print("No se pudo capturar el frame.")
        break
    
    resultado = contar_monedas(frame)
    cv.imshow("Deteccion de Monedas", resultado)
    
    if cv.waitKey(1) == ord('s'):
        break

detector.release()
cv.destroyAllWindows()
 """


""" import cv2
import numpy as np

# Variables para utilizar GaussianBlur. Deben ser valores impares
valorGauss = 3

# Variables para la matriz kernel
valorKernel = 3

# Parámetros de los umbrales de Canny (ajustarlos según el caso)
umbral_bajo = 50
umbral_alto = 150

# Captura de video desde la cámara (0 para la cámara predeterminada)
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: No se pudo acceder a la cámara.")
    exit()

while True:
    # Captura un frame de la cámara
    ret, frame = cap.read()
    if not ret:
        print("No se pudo capturar el frame.")
        break

    # Convertimos el frame a escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Suavizado para imágenes borrosas - Desenfoque gaussiano
    gauss = cv2.GaussianBlur(gris, (valorGauss, valorGauss), 0)

    # Canny: Eliminar ruidos
    canny = cv2.Canny(gauss, umbral_bajo, umbral_alto)

    # Definimos el kernel para las operaciones morfológicas
    kernel = np.ones((valorKernel, valorKernel), np.uint8)

    # Cierre de contornos (MORPH_CLOSE) - para rellenar huecos dentro de los contornos
    cierre = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

    # Apertura de contornos (MORPH_OPEN) - para eliminar ruido pequeño fuera del contorno
    apertura = cv2.morphologyEx(cierre, cv2.MORPH_OPEN, kernel)

    # Obtener contornos después de aplicar operaciones morfológicas
    contornos, _ = cv2.findContours(apertura.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filtrar contornos según su área (ajusta los valores según el tamaño de las monedas)
    contornos_filtrados = [c for c in contornos if 1000 < cv2.contourArea(c) < 15000]  # Filtrar según el área mínima y máxima

    # Dibujar los contornos en el frame original (solo los contornos de las monedas)
    cv2.drawContours(frame, contornos_filtrados, -1, (251, 60, 50), 3)

    # Contar el número de contornos (monedas) detectados
    num_monedas = len(contornos_filtrados)

    # Mostrar la cantidad de monedas detectadas en la pantalla
    cv2.putText(frame, f"Monedas detectadas: {num_monedas}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Mostrar los resultados en vivo
    cv2.imshow("Detección de Contornos en Vivo", frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar el recurso de la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows() """


import cv2

# Inicializa la cámara
cap = cv2.VideoCapture(1)

while True:
    # Captura fotograma por fotograma
    ret, frame = cap.read()

    # Si la captura fue exitosa
    if not ret:
        print("No se pudo acceder a la cámara")
        break

    # Convierte la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplica un desenfoque para reducir el ruido
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)

    # Detección de bordes con el operador Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Detecta los contornos
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filtra los contornos por área y dibuja los que tienen una forma aproximada de círculo
    count = 0
    for contour in contours:
        # Aproxima el contorno a un polígono
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Si el contorno es un círculo, cuenta la moneda
        if len(approx) > 8:  # Un círculo tiene más de 8 vértices
            count += 1
            cv2.drawContours(frame, [approx], -1, (0, 255, 0), 2)

    # Muestra el número de monedas detectadas
    cv2.putText(frame, f'Monedas: {count}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Muestra la imagen procesada
    cv2.imshow('Cámara', frame)

    # Rompe el bucle si presionas 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la cámara y cierra las ventanas
cap.release()
cv2.destroyAllWindows()
