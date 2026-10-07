import cv2
from config import CAMERA_INDEX

cap = cv2.VideoCapture(CAMERA_INDEX)
def get_frame():
    ret, frame= cap.read()
    if ret:
        return frame
    return None