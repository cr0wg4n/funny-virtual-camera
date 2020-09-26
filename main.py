import pyvirtualcam
import cv2
from models.Filterizer import Filterizer
from pynput import keyboard
import time 

key = ''

def main():
    width=640
    height=360
    fps = 6
    webcam = cv2.VideoCapture(0)
    webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
    background = cv2.imread('./backgrounds/pycon.png')
    filterer = Filterizer()
    # listener = keyboard.Listener(on_press=on_press)
    # listener.start()
    listener = keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+a': hot_key_a,
        '<ctrl>+<alt>+s': hot_key_s,
        '<ctrl>+<alt>+d': hot_key_d,
        '<ctrl>+<alt>+f': hot_key_f,
    })
    listener.start()
    with pyvirtualcam.Camera(width=width, height=height, fps=fps, delay=1) as cam:
        while True:
            if key == 'a':
                _, image_frame = webcam.read()
                result = filterer.insert_background_instead_green(image_frame, background)
                # cv2.imshow("res", result)
                result = cv2.cvtColor(result, cv2.COLOR_BGR2RGBA)
                cam.send(result)
                # cv2.waitKey(1)
            elif key == 's':
                pass
            elif key == 'd':
                pass
            elif key == 'f':
                _, image_frame = webcam.read()
                result = cv2.cvtColor(image_frame, cv2.COLOR_BGR2RGBA)
                cam.send(result)

def hot_key_a():
    global key
    key = 'a'

def hot_key_s():
    global key
    key = 's'

def hot_key_d():
    global key
    key = 'd'

def hot_key_f():
    global key
    key = 'f'

if __name__ == "__main__":
    main()