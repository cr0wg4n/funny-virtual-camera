import pyvirtualcam
import cv2
from models.ImageManager import ImageManager
from models.Frame import Frame
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
    # background = cv2.imread('./backgrounds/pycon.png')
    frames = [
        Frame(id='pycon', path='./backgrounds/pycon.png', width=width, height=height),
        Frame(id='moon', path='./backgrounds/moon.jpg', width=width, height=height),
        Frame(id='time', path='./backgrounds/its_time_to_stop.mp4', width=width, height=height, video=True)
    ]
    image_manager = ImageManager()
    frames = image_manager.load_files(frames)
    listener = keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+a': hot_key_a,
        '<ctrl>+<alt>+s': hot_key_s,
        '<ctrl>+<alt>+d': hot_key_d,
        '<ctrl>+<alt>+f': hot_key_f,
    })
    listener.start()
    print('data loaded!')
    with pyvirtualcam.Camera(width=width, height=height, fps=fps, delay=1) as cam:
        count = 0
        lenght = 0
        while True:
            if key == 'a':
                _, image_frame = webcam.read()
                background = Frame().get_frame_by_id(frames, 'pycon')
                if background:
                    result = image_manager.insert_background_instead_green(image_frame, background.frame)
                    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGBA)
                    cam.send(result)
            elif key == 's':
                _, image_frame = webcam.read()
                background = Frame().get_frame_by_id(frames, 'moon')
                if background:
                    result = image_manager.insert_background_instead_green(image_frame, background.frame)
                    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGBA)
                    cam.send(result)
            elif key == 'd':
                video = Frame().get_frame_by_id(frames, 'time')
                if video:
                    result = video.frame[count]
                    count += 1
                    lenght = len(video.frame)
                    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGBA)
                    cam.send(result)
                    cam.sleep_until_next_frame()
            elif key == 'f':
                _, image_frame = webcam.read()
                result = cv2.cvtColor(image_frame, cv2.COLOR_BGR2RGBA)
                cam.send(result)

            if count >= lenght:
                count=0
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