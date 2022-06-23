import numpy as np
import cv2
import time

cap = cv2.VideoCapture('All over in 10 seconds.mp4')
#cap = cv2.VideoCapture(0)

# used to record the time when we processed last frame
prev_frame_time = 0

# used to record the time at which we processed current frame
new_frame_time = 0
    
while (True):
    ret, frame = cap.read()
    
    gray = frame     
    
    # font which we will be using to display FPS
    font = cv2.FONT_HERSHEY_SIMPLEX
    # time when we finish processing for this frame
    new_frame_time = time.time()
    
    # Calculating the fps
 
    # fps will be number of frame processed in given time frame
    # since their will be most of time error of 0.001 second
    # we will be subtracting it to get more accurate result
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
 
    # converting the fps into integer
    fps = int(fps)
 
    # converting the fps to string so that we can display it on frame
    # by using putText function
    fps = str(fps)
 
    # putting the FPS count on the frame
    cv2.putText(gray, fps, (7, 70), font, 3, (255, 0, 0), 1, cv2.LINE_AA)

    
    cv2.imshow('frame', gray)
    
    k = cv2.waitKey(30)                                                         #detectar cada 30 seg si se presiona una tecla
    if k == 27:                                                             #27 es el ascii para escape
        break     
    
cap.release()
cv2.destroyAllWindows()