import cv2
from modules.currency_detector import detect_currency

# Load test image
image = cv2.imread("test_images/100.jpg")

results = detect_currency(image)

if len(results) == 0:
    print("No currency detected")
else:
    print("\nDetected Currency:\n")

    for r in results:
        print(
            f"₹{r['currency']}   "
            f"Confidence : {r['confidence']:.2f}"
        )