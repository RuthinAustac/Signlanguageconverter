def is_c_sign(hand_landmarks):
    # Thumb and Pinky extended
    thumb_extended = hand_landmarks.landmark[4].y < hand_landmarks.landmark[3].y  # Thumb extended outward
    pinky_extended = hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y  # Pinky extended outward
    
    # Other fingers (index, middle, ring) curled
    index_curled = hand_landmarks.landmark[8].y > hand_landmarks.landmark[6].y  # Index curled inward
    middle_curled = hand_landmarks.landmark[12].y > hand_landmarks.landmark[10].y  # Middle curled inward
    ring_curled = hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y  # Ring curled inward

    # Thumb and Pinky extended, other fingers curled
    return thumb_extended and pinky_extended and index_curled and middle_curled and ring_curled


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
    # Thumb pointing vertically (tip above IP joint)
    thumb_vertical = hand_landmarks.landmark[4].y < hand_landmarks.landmark[3].y

    # Index pointing right (tip to the right of PIP joint)
    index_right = hand_landmarks.landmark[8].x > hand_landmarks.landmark[6].x

    # Other fingers curled (tips below their middle joints)
    others_curled = (
        hand_landmarks.landmark[12].y > hand_landmarks.landmark[10].y and
        hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y and
        hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y
    )

    return thumb_vertical and index_right and others_curled


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
    index_up = hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y
    middle_down = hand_landmarks.landmark[12].y > hand_landmarks.landmark[10].y
    ring_down = hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y
    pinky_down = hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y
    thumb_down = hand_landmarks.landmark[4].y > hand_landmarks.landmark[3].y

    return index_up and middle_down and ring_down and pinky_down and thumb_down

def is_three_fingers_up(hand_landmarks):
    return (
        hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y and  # Index finger up
        hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y and  # Middle finger up
        hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y and  # Ring finger up
        hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y  # Pinky down
    )

def is_scissors_gesture(hand_landmarks):
    index_tip = hand_landmarks.landmark[8]
    middle_tip = hand_landmarks.landmark[12]
    ring_tip = hand_landmarks.landmark[16]
    pinky_tip = hand_landmarks.landmark[20]
    ring_pip = hand_landmarks.landmark[14]
    pinky_pip = hand_landmarks.landmark[18]

    # Fingers extended
    index_up = index_tip.y < hand_landmarks.landmark[6].y
    middle_up = middle_tip.y < hand_landmarks.landmark[10].y

    # Fingers down
    ring_down = ring_tip.y > ring_pip.y
    pinky_down = pinky_tip.y > pinky_pip.y

    # Check if index and middle fingers are close together (gun shape)
    fingers_close = abs(index_tip.x - middle_tip.x) < 0.05  # adjust tolerance if needed

    return index_up and middle_up and fingers_close and ring_down and pinky_down


def is_ok_sign(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[4]
    index_tip = hand_landmarks.landmark[8]
    middle_tip = hand_landmarks.landmark[12]
    ring_tip = hand_landmarks.landmark[16]
    pinky_tip = hand_landmarks.landmark[20]

    # Circle detection (thumb and index touching)
    thumb_index_touching = (
        abs(thumb_tip.x - index_tip.x) < 0.05 and
        abs(thumb_tip.y - index_tip.y) < 0.05
    )

    # Other fingers extended upward (tips above lower joints)
    middle_up = middle_tip.y < hand_landmarks.landmark[10].y
    ring_up = ring_tip.y < hand_landmarks.landmark[14].y
    pinky_up = pinky_tip.y < hand_landmarks.landmark[18].y

    return thumb_index_touching and middle_up and ring_up and pinky_up


def is_all_fingers_closed_flat(hand_landmarks):
    # All finger tips below their middle joints (folded inward)
    fingers_closed = all(
        hand_landmarks.landmark[tip].y > hand_landmarks.landmark[tip - 2].y
        for tip in [8, 12, 16, 20]
    )

    # Thumb folded across palm
    thumb_closed = hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x

    return fingers_closed and thumb_closed

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
    # Only the pinky finger extended, all other fingers closed
    pinky_extended = hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y  # Pinky extended
    fingers_closed = all(
        hand_landmarks.landmark[tip].y > hand_landmarks.landmark[tip - 2].y
        for tip in [8, 12, 16]  # Ensure index, middle, and ring fingers are closed
    )
    thumb_hidden = hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x  # Thumb curled in

    return pinky_extended and fingers_closed and thumb_hidden

def is_scroll_down(hand_landmarks):
    # Pinky and index fingers extended, all other fingers closed
    pinky_extended = hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y  # Pinky extended
    index_extended = hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y  # Index extended
    fingers_closed = all(
        hand_landmarks.landmark[tip].y > hand_landmarks.landmark[tip - 2].y
        for tip in [12, 16]  # Ensure middle and ring fingers are closed
    )
    thumb_hidden = hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x  # Thumb curled in

    return pinky_extended and index_extended and fingers_closed and thumb_hidden
