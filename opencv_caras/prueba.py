import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #Ubicacion de la hardcascade

cap = cv2.VideoCapture(0)                                                   #Obtener referencia a la webcam o video

while True:                                                                 #Bucle infinito para leer fotograma x fotograma
    _, img = cap.read()                                                     #Leer cada uno de los fotogramas
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                            #Convertir a escala de grises para que opencv detecte bien
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)                     #almacenar caras, (escala de grises, y parametros para detectar las caras)
    for(x, y, w, h) in faces:                                                   #Generar el cuadrado en las caras, son los vertices del cuadrado
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('img', img)                                                  #mostrar con el cuadrado y la cara detectada
    k = cv2.waitKey(30)                                                         #detectar cada 30 seg si se presiona una tecla
    if k == 27:                                                             #27 es el ascii para escape
        break                                                               #cortar con escape
    
cap.release()                                                               #liberar la webcam
