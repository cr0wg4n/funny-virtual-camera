import pyvirtualcam
import cv2
from models.Filterizer import Filterizer
from pynput import keyboard
from multiprocessing import Process
import time 

tecla = ''
def main():
    width=640
    height=480
    fps = 4
    webcam = cv2.VideoCapture(0)
    background = cv2.imread('./backgrounds/pycon.png')
    filterer = Filterizer()
    # proc = Process(target=launch_keyboard_listener, args=(key,))
    # proc.start()
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    with pyvirtualcam.Camera(width=width, height=height, fps=fps, delay=1) as cam:
        while True:
            _, image_frame = webcam.read()
            result = filterer.insert_background_instead_green(image_frame, background)
            result = cv2.cvtColor(result, cv2.COLOR_BGR2RGBA)
            cam.send(result)
            print(tecla)

def on_press(key):
    global tecla
    tecla = key

if __name__ == "__main__":
    main()