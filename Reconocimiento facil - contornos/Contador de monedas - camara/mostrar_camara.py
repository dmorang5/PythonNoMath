# Importaciones
import cv2 as cv

capturaVideo = cv.VideoCapture(1)

if not capturaVideo.isOpened():
    print("No se encontró una cámara")
    exit()

while True:
    _,Camara = capturaVideo.read()
    if not _ or Camara is None:
        print("No se pudo capturar el frame. Verifica la cámara.")
        break
    
    grises = cv.cvtColor(Camara, cv.COLOR_BGR2GRAY)    
    
    #cv.imshow("En vivo", Camara)
    cv.imshow("En vivo en grises", grises)
    if cv.waitKey(1) == ord("q"):
        break

capturaVideo.release() # detenemos
cv.destroyAllWindows() # destruimos
