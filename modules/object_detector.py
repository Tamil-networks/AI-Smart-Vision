from turtle import color

from ultralytics import YOLO
from config import MODEL_PATH
from modules.color_detector import detect_color


# Load YOLO model
model = YOLO(MODEL_PATH)

def detect_objects(frame):
    results = model(frame)
    names = results[0].names
    detected = []

    for box in results[0].boxes:
        cls = int(box.cls[0])
        label = names[cls]

        # ---------------- BOUNDING BOX ----------------
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        color = detect_color(frame, x1, y1, x2, y2)
        width = x2 - x1
        height = y2 - y1

        # ---------------- DISTANCE ESTIMATION ----------------
        # Approximate distance using bounding-box width
        if width > 400:
            distance_m = 0.2
        elif width > 300:
            distance_m = 0.4
        elif width > 220:
            distance_m = 0.8
        elif width > 160:
            distance_m = 1.5
        elif width > 100:
            distance_m = 2.5
        else:
            distance_m = 4.0

        # ---------------- HUMAN READABLE DISTANCE ----------------
        if distance_m <= 0.3:
            distance = "critical"
        elif distance_m <= 1.0:
            distance = "close"
        elif distance_m <= 3.0:
            distance = "warning"
        else:
            distance = "far"

        # ---------------- POSITION DETECTION ----------------
        center_x = (x1 + x2) / 2
        if center_x < frame.shape[1] / 3:
            side = "left"
        elif center_x > frame.shape[1] * 2 / 3:
            side = "right"
        else:
            side = "front"

        # ---------------- SAVE OBJECT DATA ----------------
        detected.append({
            "name": label,
            "color": color,
            "distance": distance,
            "distance_m": distance_m,
            "side": side,
            "x": x1,
            "y": y1,
            "width": width,
            "height": height
        })

    return detected


