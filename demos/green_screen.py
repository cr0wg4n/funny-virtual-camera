import numpy as np
import cv2

webcam = cv2.VideoCapture(0)
background = cv2.imread('./backgrounds/pycon.png')
while(1):
    _, image_frame = webcam.read()
    hsvFrame = cv2.cvtColor(image_frame, cv2.COLOR_BGR2HSV)

    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
    kernel = np.ones((5, 5), "uint8")

    green_mask = ~cv2.dilate(green_mask, kernel)
    green_mask = cv2.medianBlur(green_mask, 9)
    res_green = cv2.bitwise_and(image_frame, image_frame,
                                mask=green_mask)
    cols, rows = res_green.shape[:2]
    print(cols, rows)
    background = background[0:cols, 0:rows]
    new_mask = cv2.cvtColor(green_mask, cv2.COLOR_GRAY2BGR)
    background_mask = cv2.bitwise_and(background, ~new_mask)
    result = background_mask + res_green
    cv2.imshow("result", result)

    # cv2.imshow("green-mask", green_mask)
    # cv2.imshow('new_mask', new_mask)
    # cv2.imshow('substract',cv2.subtract(~new_mask, background))
    # cv2.imshow('res_green', res_green)
    # cv2.imshow('background', background)


    # Creating contour to track green color
    # contours, hierarchy = cv2.findContours(green_mask,
    #                                        cv2.RETR_TREE,
    #                                        cv2.CHAIN_APPROX_SIMPLE)

    # for pic, contour in enumerate(contours):
    #     area = cv2.contourArea(contour)
    #     if(area > 300):
    #         x, y, w, h = cv2.boundingRect(contour)
    #         image_frame = cv2.rectangle(image_frame, (x, y),
    #                                    (x + w, y + h),
    #                                    (0, 255, 0), 2)

    #         cv2.putText(image_frame, "Green Colour", (x, y),
    #                                 cv2.FONT_HERSHEY_SIMPLEX,
    #                                 1.0, (0, 255, 0))

    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
