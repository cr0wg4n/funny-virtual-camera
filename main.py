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
        Frame(id='thunder', path='./backgrounds/thunder.jpg', width=width, height=height),
        Frame(id='pycon', path='./backgrounds/pycon.png', width=width, height=height),
        Frame(id='moon', path='./backgrounds/moon.jpg', width=width, height=height),
        Frame(id='time', path='./backgrounds/its_time_to_stop.mp4', width=width, height=height, video=True),
        Frame(id='error', path='./backgrounds/exp_error.mp4', width=width, height=height, video=True),
        Frame(id='macizo', path='./backgrounds/macizo.jpg', width=width, height=height),
        Frame(id='rev', path='./backgrounds/revolucion.jpg', width=width, height=height),
        Frame(id='hacked', path='./backgrounds/hacked.mp4', width=width, height=height, video=True)
    ]
    image_manager = ImageManager()
    frames = image_manager.load_files(frames)
    listener = keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+a': hot_key_a,
        '<ctrl>+<alt>+s': hot_key_s,
        '<ctrl>+<alt>+d': hot_key_d,
        '<ctrl>+<alt>+n': hot_key_n,
        '<ctrl>+<alt>+t': hot_key_t,
        '<ctrl>+<alt>+e': hot_key_e,
        '<ctrl>+<alt>+r': hot_key_r,
        '<ctrl>+<alt>+m': hot_key_m,
        '<ctrl>+<alt>+h': hot_key_h,
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
            elif key == 't':
                _, image_frame = webcam.read()
                background = Frame().get_frame_by_id(frames, 'thunder')
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
            elif key == 'e':
                video = Frame().get_frame_by_id(frames, 'error')
                if video:
                    result = video.frame[count]
                    count += 1
                    lenght = len(video.frame)
                    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGBA)
                    cam.send(result)
                    cam.sleep_until_next_frame()
            elif key == 'h':
                video = Frame().get_frame_by_id(frames, 'hacked')
                if video:
                    result = video.frame[count]
                    count += 1
                    lenght = len(video.frame)
                    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGBA)
                    cam.send(result)
                    cam.sleep_until_next_frame()
            elif key == 'm':
                _, image_frame = webcam.read()
                background = Frame().get_frame_by_id(frames, 'macizo')
                if background:
                    result = cv2.cvtColor(background.frame, cv2.COLOR_BGR2RGBA)
                    cam.send(result)
            elif key == 'r':
                _, image_frame = webcam.read()
                background = Frame().get_frame_by_id(frames, 'rev')
                if background:
                    result = image_manager.insert_background_instead_green(image_frame, background.frame)
                    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGBA)
                    cam.send(result)
            elif key == 'n':
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

def hot_key_n():
    global key
    key = 'n'
    
def hot_key_t():
    global key
    key = 't'

def hot_key_e():
    global key
    key = 'e'

def hot_key_m():
    global key
    key = 'm'

def hot_key_r():
    global key
    key = 'r'

def hot_key_h():
    global key
    key = 'h'
if __name__ == "__main__":
    main()