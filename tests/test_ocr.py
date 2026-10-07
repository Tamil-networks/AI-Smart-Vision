import cv2

from modules.camera import get_frame
from modules.ocr.ocr_reader import read_text

while True:

    frame = get_frame()

    if frame is None:
        continue

    results = read_text(frame)

    for item in results:

        pts = item["bbox"]

        x = int(pts[0][0])
        y = int(pts[0][1])

        cv2.putText(
            frame,
            item["text"],
            (x, y-5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )

        print(item["text"])

    cv2.imshow("OCR Test", frame)

    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()