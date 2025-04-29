import cv2
from hand_detection import detect_hands, draw_hands
from gesture_recognition import (
    is_open_hand, is_fist, is_paste_gesture, is_thumbs_up, is_victory_sign, is_l_sign,
    is_three_fingers_up, is_scissors_gesture, is_four_fingers_up,
    is_volume_up, is_volume_down, is_screenshot, is_mouse_control, is_fist_thumb_sideways,
    is_select_all, is_new_tab, is_scroll_up, is_scroll_down  
)
from actions import (
    trigger_copy, trigger_paste, trigger_backspace, trigger_enter, trigger_alt_tab,
    trigger_undo, trigger_cut, trigger_save, trigger_close_app,
    increase_volume, decrease_volume, take_screenshot, move_mouse, trigger_select_all, trigger_new_tab, trigger_scroll_up, trigger_scroll_down  # Added new actions
)


# Initialize Camera
cap = cv2.VideoCapture(0)
gesture_count = {}  # Stores consecutive detections

def detect_gesture(gesture_name, hand_landmarks, detection_function, action_function):
    if gesture_name not in gesture_count:
        gesture_count[gesture_name] = 0

    if detection_function(hand_landmarks):  # Use the detection function to check the gesture
        gesture_count[gesture_name] += 1
    else:
        gesture_count[gesture_name] = 0  # Reset if not detected

    if gesture_count[gesture_name] > 5:  # Gesture must be stable for 5 frames
        if action_function == move_mouse:
            action_function(hand_landmarks)  # Pass hand_landmarks to move_mouse
        else:
            action_function()  # Trigger other action functions without arguments
        gesture_count[gesture_name] = 0  # Reset after execution

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect hands
    result = detect_hands(frame)

    if result.multi_hand_landmarks:
        draw_hands(frame, result.multi_hand_landmarks)
        for hand_landmarks in result.multi_hand_landmarks:
            
            detect_gesture("open_hand", hand_landmarks, is_open_hand, trigger_copy)
            detect_gesture("fist", hand_landmarks, is_fist, trigger_backspace)
            detect_gesture("thumbs_up", hand_landmarks, is_thumbs_up, trigger_enter)
            detect_gesture("paste_gesture", hand_landmarks, is_paste_gesture, trigger_paste)  # Updated Paste Gesture
            detect_gesture("l_sign", hand_landmarks, is_l_sign, trigger_alt_tab)
            detect_gesture("three_fingers_up", hand_landmarks, is_three_fingers_up, trigger_undo)
            detect_gesture("scissors_gesture", hand_landmarks, is_scissors_gesture, trigger_cut)
            detect_gesture("fist_thumb_sideways", hand_landmarks, is_fist_thumb_sideways, trigger_save)
            detect_gesture("four_fingers_up", hand_landmarks, is_four_fingers_up, trigger_close_app)
           
          
            detect_gesture("mouse_control", hand_landmarks, is_mouse_control, move_mouse)
            detect_gesture("victory_sign", hand_landmarks, is_victory_sign, trigger_paste)  # Example action
            
            detect_gesture("select_all", hand_landmarks, is_select_all, trigger_select_all)  # New Gesture
            detect_gesture("new_tab", hand_landmarks, is_new_tab, trigger_new_tab)  # New Gesture
            detect_gesture("scroll_up", hand_landmarks, is_scroll_up, trigger_scroll_up)  # New Gesture
            detect_gesture("scroll_down", hand_landmarks, is_scroll_down, trigger_scroll_down)  # New Gesture

    # Display the frame
    cv2.imshow("Gesture Control", frame)

    # Exit with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
