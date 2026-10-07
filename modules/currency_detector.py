"""
==========================================
AI SMART VISION
Currency Detector
==========================================

Detects Indian currency using YOLOv8.

Model:
    models/currency_best.pt

Returns:
    Currency label
    Confidence
    Bounding box

Author:
Hybotron
"""

from ultralytics import YOLO


class CurrencyDetector:

    def __init__(self,
                 model_path="models/currency_best.pt",
                 confidence=0.60):

        self.model = YOLO(model_path)

        self.confidence = confidence

    # --------------------------------------------------

    def detect(self, frame):

        """
        Detect currency from image/frame.

        Returns:

        [
            {
                "label": "100",
                "confidence": 0.98,
                "bbox": [x1,y1,x2,y2]
            }
        ]
        """

        results = self.model.predict(
            source=frame,
            conf=self.confidence,
            verbose=False
        )

        detections = []

        for result in results:

            boxes = result.boxes

            for box in boxes:

                cls = int(box.cls[0])

                label = result.names[cls]

                conf = float(box.conf[0])

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                detections.append({

                    "label": label,

                    "confidence": round(conf, 2),

                    "bbox": [x1, y1, x2, y2]

                })

        return detections

    # --------------------------------------------------

    def detect_best(self, frame):

        """
        Return highest confidence detection.

        Returns:

        {
            "label":"100",
            "confidence":0.98,
            "bbox":[...]
        }

        or None
        """

        detections = self.detect(frame)

        if not detections:
            return None

        detections.sort(
            key=lambda x: x["confidence"],
            reverse=True
        )

        return detections[0]