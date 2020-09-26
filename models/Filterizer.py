import cv2
import numpy as np

class Filterizer():
    def __init__(self):
        pass

    def blur(self, img):
        return cv2.blur(img, (5, 5))

    def resize(self, img, scale):
        props = self.props(img)
        return  cv2.resize(img, (int(props["width"] * scale / 100), int(props["height"] * scale / 100)))

    def props(self, img):
        return {
            "width": img.shape[1],
            "height": img.shape[0]
        }
    
    def insert_background_instead_green(self, img, background):
        hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        green_lower = np.array([25, 52, 72], np.uint8)
        green_upper = np.array([102, 255, 255], np.uint8)
        green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
        kernel = np.ones((5, 5), "uint8")
        green_mask = ~cv2.dilate(green_mask, kernel)
        green_mask = cv2.medianBlur(green_mask, 9)
        res_green = cv2.bitwise_and(img, img, mask=green_mask)
        cols, rows = res_green.shape[:2]
        background = background[0:cols, 0:rows]
        new_mask = cv2.cvtColor(green_mask, cv2.COLOR_GRAY2BGR)
        background_mask = cv2.bitwise_and(background, ~new_mask)
        result = background_mask + res_green
        return result