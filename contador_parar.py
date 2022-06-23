import numpy as np
import cv2
import time

#cap = cv2.VideoCapture('All over in 10 seconds.mp4')
cap = cv2.VideoCapture(0)

mostrar = True
gray = ''
contador = 0
    
while (True):
    if(mostrar):
        contador += 1
        ret, frame = cap.read()
        
        gray = frame     
        
        # font which we will be using to display FPS
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        key = cv2.waitKey(1)          
        if key == ord('q'):
            break
        #detectar cada 30 seg si se presiona una tecla
        if key == ord('p'):
            #cv2.waitKey(-1) #wait until any key is pressed
            mostrar = False
        
        # putting the FPS count on the frame
        cv2.putText(gray, str(contador), (7, 70), font, 3, (255, 0, 0), 1, cv2.LINE_AA)

    key = cv2.waitKey(1)          
    if key == ord('q'):
        break
    #detectar cada 30 seg si se presiona una tecla
    if key == ord('r'):
        #cv2.waitKey(-1) #wait until any key is pressed
        mostrar = True
    cv2.imshow('frame', gray)
    
 
    
cap.release()
cv2.destroyAllWindows()