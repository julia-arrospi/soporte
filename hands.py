import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
#https://omes-va.com/mediapipe-hands-python/
#https://google.github.io/mediapipe/solutions/hands#python-solution-api
#https://techtutorialsx.com/2021/04/10/python-hand-landmark-estimation/

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    height, width, _ = image.shape
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

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
        ''' print("hand landmark")
        print(hand_landmarks) '''
        
        for point in mp_hands.HandLandmark: 	
          normalizedLandmark = hand_landmarks.landmark[point]
              
        
        x1 = int(normalizedLandmark.x * width)
        y1 = int(normalizedLandmark.y * height)
        if(x1 <= 150):
          cv2.putText(image, "Adentro", (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 1, cv2.LINE_AA)

    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()