import cv2
from modules.camera import get_frame
from modules.object_detector import detect_objects

while True:
    frame = get_frame()
    if frame is None:
         continue
    objects = detect_objects(frame)
    for obj in objects:
         print(obj)

    cv2.imshow("Test Detection", frame)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()