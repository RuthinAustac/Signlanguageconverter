def is_open_hand(hand_landmarks):
    tips = [8, 12, 16, 20]  # Fingertip landmarks
    base = [5, 9, 13, 17]  # Corresponding base joints

    for tip, b in zip(tips, base):
        if abs(hand_landmarks.landmark[tip].y - hand_landmarks.landmark[b].y) < 0.1:
            return False  # Ensures fingers are fully extended
    return True

def is_fist(hand_landmarks):
    tips = [8, 12, 16, 20]
    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[0].y:
            return False
    return True

def is_thumbs_up(hand_landmarks):
    return (
        hand_landmarks.landmark[4].y < hand_landmarks.landmark[3].y and
        all(hand_landmarks.landmark[i].y > hand_landmarks.landmark[0].y for i in [8, 12, 16, 20])
    )

def is_victory_sign(hand_landmarks):
    return (
        hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y and
        hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y and
        hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y and
        hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y
    )

def is_l_sign(hand_landmarks):
    return (
        hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x and
        hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y and
        all(hand_landmarks.landmark[i].y > hand_landmarks.landmark[0].y for i in [12, 16, 20])
    )

def is_volume_up(hand_landmarks):
    return hand_landmarks.landmark[4].y < hand_landmarks.landmark[8].y  # Thumb above index

def is_volume_down(hand_landmarks):
    return hand_landmarks.landmark[4].y > hand_landmarks.landmark[8].y  # Thumb below index

def is_screenshot(hand_landmarks):
    return (
        hand_landmarks.landmark[8].x < hand_landmarks.landmark[4].x and
        hand_landmarks.landmark[12].x < hand_landmarks.landmark[4].x
    )

def is_mouse_control(hand_landmarks):
    return hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y and hand_landmarks.landmark[4].y > hand_landmarks.landmark[3].y

def is_three_fingers_up(hand_landmarks):
    return (
        hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y and  # Index finger up
        hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y and  # Middle finger up
        hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y and  # Ring finger up
        hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y  # Pinky down
    )

def is_scissors_gesture(hand_landmarks):
    return (
        hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y and  # Index finger up
        hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y and  # Middle finger up
        hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y and  # Ring finger down
        hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y  # Pinky down
    )

def is_fist_thumb_sideways(hand_landmarks):
    return (
        all(hand_landmarks.landmark[i].y > hand_landmarks.landmark[0].y for i in [8, 12, 16, 20]) and
        hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x  # Thumb is extended sideways
    )

def is_four_fingers_up(hand_landmarks):
    return (
        all(hand_landmarks.landmark[i].y < hand_landmarks.landmark[i - 2].y for i in [8, 12, 16, 20]) and
        hand_landmarks.landmark[4].y > hand_landmarks.landmark[3].y  # Thumb is down
    )
def is_paste_gesture(hand_landmarks):
    # Thumb and index finger touch
    thumb_tip = hand_landmarks.landmark[4]
    index_tip = hand_landmarks.landmark[8]
    distance = ((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2) ** 0.5

    # Other fingers extended
    middle_extended = hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y
    ring_extended = hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y
    pinky_extended = hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y

    # Check if thumb and index finger are close and other fingers are extended
    return distance < 0.05 and middle_extended and ring_extended and pinky_extended
def is_select_all(hand_landmarks):
    # Thumb and pinky finger touch, others extended
    thumb_tip = hand_landmarks.landmark[4]
    pinky_tip = hand_landmarks.landmark[20]
    distance = ((thumb_tip.x - pinky_tip.x) ** 2 + (thumb_tip.y - pinky_tip.y) ** 2) ** 0.5

    # Other fingers extended
    index_extended = hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y
    middle_extended = hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y
    ring_extended = hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y

    return distance < 0.05 and index_extended and middle_extended and ring_extended

def is_new_tab(hand_landmarks):
    # Thumb and ring finger touch, others extended
    thumb_tip = hand_landmarks.landmark[4]
    ring_tip = hand_landmarks.landmark[16]
    distance = ((thumb_tip.x - ring_tip.x) ** 2 + (thumb_tip.y - ring_tip.y) ** 2) ** 0.5

    # Other fingers extended
    index_extended = hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y
    middle_extended = hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y
    pinky_extended = hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y

    return distance < 0.05 and index_extended and middle_extended and pinky_extended

def is_scroll_up(hand_landmarks):
    # Index finger pointing upward, others curled
    index_extended = hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y
    middle_curled = hand_landmarks.landmark[12].y > hand_landmarks.landmark[10].y
    ring_curled = hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y
    pinky_curled = hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y

    return index_extended and middle_curled and ring_curled and pinky_curled

def is_scroll_down(hand_landmarks):
    # Index finger pointing downward, others curled
    index_curled = hand_landmarks.landmark[8].y > hand_landmarks.landmark[6].y
    middle_curled = hand_landmarks.landmark[12].y > hand_landmarks.landmark[10].y
    ring_curled = hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y
    pinky_curled = hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y

    return index_curled and middle_curled and ring_curled and pinky_curled
