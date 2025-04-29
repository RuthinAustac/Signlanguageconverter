import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1, 
    min_detection_confidence=0.85,  # Increased accuracy
    min_tracking_confidence=0.85
)
mp_draw = mp.solutions.drawing_utils

def detect_hands(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    return result

def draw_hands(frame, hand_landmarks):
    if hand_landmarks:
        for landmarks in hand_landmarks:
            mp_draw.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
