import cv2
from paddleocr import PaddleOCR

# Initialize once
ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en"
)

def read_text(frame, min_conf=0.5):

    if frame is None:
        return []

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = ocr.ocr(rgb, cls=True)

    texts = []

    if results is None:
        return texts

    for line in results:

        if line is None:
            continue

        for word in line:

            bbox = word[0]
            text = word[1][0]
            conf = word[1][1]

            if conf >= min_conf:

                texts.append({
                    "text": text,
                    "conf": float(conf),
                    "bbox": bbox
                })

    return texts


def read_text_strings(frame):

    results = read_text(frame)

    return [r["text"] for r in results]