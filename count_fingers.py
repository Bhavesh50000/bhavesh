import cv2
import mediapipe as mp
cap = cv2.VideoCapture(0)
mp_hand=mp.solutions.hands
mp_drawing=mp.solutions.drawing_utils

hands = mp_hand.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5)

def drawHandLanmarks(image,handLandmark):
    if handLandmark:
        for landmark in handLandmark:
            mp_drawing.draw_landmark(image,landmark,mp_hand.HAND_CONNECTIONS)

while True:
    success, image = cap.read()

    image = cv2.flip(image,1)
    result = hands.process(image)
    handLandmark = result.multi_hand_landmarks
    drawHandLanmarks(image,handLandmark)
    
 # Get Hand Fingers Position    
    cv2.imshow("Media Controller", image)

    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()

