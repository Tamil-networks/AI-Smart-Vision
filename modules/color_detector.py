import cv2
import numpy as np


# ---------------- COLOR RANGES (HSV) ----------------
COLOR_RANGES = {
    "red": [
        ((0, 80, 80), (10, 255, 255)),
        ((170, 80, 80), (180, 255, 255))
    ],
    "orange": [
        ((11, 80, 80), (20, 255, 255))
    ],
    "yellow": [
        ((21, 80, 80), (35, 255, 255))
    ],
    "green": [
        ((36, 50, 50), (85, 255, 255))
    ],
    "blue": [
        ((86, 80, 80), (130, 255, 255))
    ],
    "purple": [
        ((131, 50, 50), (160, 255, 255))
    ],
    "pink": [
        ((161, 50, 50), (169, 255, 255))
    ],
    "white": [
        ((0, 0, 200), (180, 30, 255))
    ],
    "gray": [
        ((0, 0, 80), (180, 30, 199))
    ],
    "black": [
        ((0, 0, 0), (180, 255, 79))
    ]
}


# ---------------- DETECT DOMINANT COLOR ----------------
def detect_color(frame, x1, y1, x2, y2):

    roi = frame[y1:y2, x1:x2]

    if roi.size == 0:
        return "unknown"

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    max_pixels = 0
    dominant_color = "unknown"

    for color_name, ranges in COLOR_RANGES.items():

        total = 0

        for lower, upper in ranges:

            lower = np.array(lower)
            upper = np.array(upper)

            mask = cv2.inRange(hsv, lower, upper)

            total += cv2.countNonZero(mask)

        if total > max_pixels:
            max_pixels = total
            dominant_color = color_name

    return dominant_color