import cv2 as cv
import os
import imutils

modelo = 'FotosDenn'
ruta1 = r'D:\UDEMY\Python para no matematicos De 0 hasta reconocimiento facial\Reconocimiento facial\Data'
rutacompleta = os.path.join(ruta1, modelo)

if not os.path.exists(rutacompleta):
    os.makedirs(rutacompleta)

# Cargar el clasificador
ruidos = cv.CascadeClassifier(r'D:\UDEMY\Python para no matematicos De 0 hasta reconocimiento facial\Reconocimiento facial\Data\haarcascade_frontalface_default.xml')

if ruidos.empty():
    print("Error: No se pudo cargar el clasificador de rostros")
    exit()

# Inicializar cámara
camara = cv.VideoCapture(1)
camara.set(cv.CAP_PROP_FRAME_WIDTH, 640)
camara.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

id = 0

while True:
    respuesta, captura = camara.read()

    if not respuesta or captura is None:
        print("No se pudo capturar imagen")
        break

    captura = imutils.resize(captura, width=640)
    grises = cv.cvtColor(captura, cv.COLOR_BGR2GRAY)
    idcaptura = captura.copy()

    cara = ruidos.detectMultiScale(grises, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))

    for (x, y, e1, e2) in cara:
        cv.rectangle(captura, (x, y), (x + e1, y + e2), (0, 255, 0), 2)
        rostrocapturado = idcaptura[y:y + e2, x:x + e1]
        rostrocapturado = cv.resize(rostrocapturado, (160, 160), interpolation=cv.INTER_CUBIC)
        cv.imwrite(os.path.join(rutacompleta, f'imagen_{id}.jpg'), rostrocapturado)
        id += 1

    cv.imshow("Resultado rostro", captura)

    if cv.waitKey(1) & 0xFF == 27 or id == 350:  # Presiona ESC para salir
        break

camara.release()
cv.destroyAllWindows()
