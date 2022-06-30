import numpy as np
import cv2
import time
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

#cap = cv2.VideoCapture('All over in 10 seconds.mp4')
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    static_image_mode=False,
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while True:
        success, image = cap.read()

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
    
    ''' start_point = (0, 0)
    end_point = (150, 150)
    color = (255, 0, 0)
    thickness = 2
    frame2 = cv2.rectangle(frame2, start_point, end_point, color, thickness)
    
    key = cv2.waitKey(1)          
    if key == ord('q'):
        break '''
        
    cap.release()

'''     cv2.imshow('frame', frame)
    cv2.imshow('frame2', frame2)
    

        
    cap.release()
    cv2.destroyAllWindows() '''