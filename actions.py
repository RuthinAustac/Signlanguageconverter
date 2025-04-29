from pynput.keyboard import Controller, Key
from pynput.mouse import Controller as MouseController, Button
import pyautogui

keyboard = Controller()
mouse = MouseController()

def trigger_copy():
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)
    print("Ctrl+C Triggered")

def trigger_paste():
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)
    print("Ctrl+V Triggered")

def trigger_backspace():
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    print("Backspace Triggered")

def trigger_enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    print("Enter Triggered")

def trigger_alt_tab():
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt)
    print("Alt+Tab Triggered")

def increase_volume():
    keyboard.press(Key.media_volume_up)
    keyboard.release(Key.media_volume_up)
    print("Volume Up")

def decrease_volume():
    keyboard.press(Key.media_volume_down)
    keyboard.release(Key.media_volume_down)
    print("Volume Down")

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    print("Screenshot Taken")

def move_mouse(hand_landmarks):
    screen_width, screen_height = pyautogui.size()
    x = int(hand_landmarks.landmark[8].x * screen_width)
    y = int(hand_landmarks.landmark[8].y * screen_height)
    mouse.position = (x, y)
    print(f"Mouse moved to ({x}, {y})")

def trigger_undo():
    keyboard.press(Key.ctrl)
    keyboard.press('z')
    keyboard.release('z')
    keyboard.release(Key.ctrl)
    print("Ctrl+Z (Undo) Triggered")

def trigger_cut():
    keyboard.press(Key.ctrl)
    keyboard.press('x')
    keyboard.release('x')
    keyboard.release(Key.ctrl)
    print("Ctrl+X (Cut) Triggered")

def trigger_save():
    keyboard.press(Key.ctrl)
    keyboard.press('s')
    keyboard.release('s')
    keyboard.release(Key.ctrl)
    print("Ctrl+S (Save) Triggered")

def trigger_close_app():
    keyboard.press(Key.alt)
    keyboard.press(Key.f4)
    keyboard.release(Key.f4)
    keyboard.release(Key.alt)
    print("Alt+F4 (Close App) Triggered")
def trigger_mouse_left_click():
    mouse.press(Button.left)
    mouse.release(Button.left)
    print("Mouse Left Click Triggered")

def trigger_mouse_right_click():
    mouse.press(Button.right)
    mouse.release(Button.right)
    print("Mouse Right Click Triggered")
def trigger_select_all():
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.ctrl)
    print("Ctrl+A (Select All) Triggered")

def trigger_new_tab():
    keyboard.press(Key.ctrl)
    keyboard.press('t')
    keyboard.release('t')
    keyboard.release(Key.ctrl)
    print("Ctrl+T (New Tab) Triggered")

def trigger_scroll_up():
    mouse.scroll(0, 2)  # Scroll up
    print("Scroll Up Triggered")

def trigger_scroll_down():
    mouse.scroll(0, -2)  # Scroll down
    print("Scroll Down Triggered")
    
