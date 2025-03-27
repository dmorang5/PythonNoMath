import cv2

cam = cv2.VideoCapture(1)

while True:
    ret, frame = cam.read()
    if not ret:
        print("No se pudo capturar imagen")
        break

    cv2.imshow("Prueba de cámara", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Presiona ESC para salir
        break

cam.release()
cv2.destroyAllWindows()
