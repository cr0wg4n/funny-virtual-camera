import cv2
import numpy as np

class ImageManager():
    def __init__(self):
        pass

    def blur(self, img):
        return cv2.blur(img, (5, 5))

    def rescale(self, img, scale):
        props = self.props(img)
        return  cv2.resize(img, (int(props["width"] * scale / 100), int(props["height"] * scale / 100)))

    def props(self, img):
        return {
            "width": img.shape[1],
            "height": img.shape[0]
        }
    
    def insert_background_instead_green(self, img, background):
        hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        green_lower = np.array([25, 16, 72], np.uint8)
        green_upper = np.array([102, 255, 255], np.uint8)
        green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
        kernel = np.ones((5, 5), "uint8")
        green_mask = ~cv2.dilate(green_mask, kernel)
        green_mask = cv2.medianBlur(green_mask, 5)
        res_green = cv2.bitwise_and(img, img, mask=green_mask)
        cols, rows = res_green.shape[:2]
        background = background[0:cols, 0:rows]
        new_mask = cv2.cvtColor(green_mask, cv2.COLOR_GRAY2BGR)
        background_mask = cv2.bitwise_and(background, ~new_mask)
        result = background_mask + res_green
        return result

    def remove_green_background(self, img):
        hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        green_lower = np.array([25, 102, 72], np.uint8)
        green_upper = np.array([102, 255, 255], np.uint8)
        green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
        kernel = np.ones((5, 5), "uint8")
        green_mask = ~cv2.dilate(green_mask, kernel)
        green_mask = cv2.medianBlur(green_mask, 5)
        res_green = cv2.bitwise_and(img, img, mask=green_mask)
        new_mask = cv2.cvtColor(green_mask, cv2.COLOR_GRAY2BGR)
        return ~new_mask

    def load_files(self, images):
        for image in images:
            if image.video:
                frames = []
                cap = cv2.VideoCapture(image.path)
                while True:
                    _, frame = cap.read()
                    frame = cv2.resize(frame, (image.width, image.height))
                    mask = self.remove_green_background(frame)
                    frame = cv2.bitwise_and(frame, ~mask)
                    frames.append(frame)
                    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
                        break
                image.frame = frames
            else:
                image.frame = cv2.imread(image.path)
                image.frame = cv2.resize(image.frame, (image.width, image.height))
        return images
