import cv2

from modules.ocr.ocr_reader import read_text
from modules.bus.bus_parser import BusParser

IMAGE_PATH = "tests/bus_images/tamil/bus1.jpg"

frame = cv2.imread(IMAGE_PATH)

if frame is None:
    print("Image not found!")
    exit()

# OCR
ocr_results = read_text(frame)

print("\n========== OCR RESULTS ==========")

for r in ocr_results:
    print(r)

# Bus Parser
parser = BusParser()

bus_info = parser.parse(ocr_results)

print("\n========== BUS INFO ==========")

print("Bus Number :", bus_info.bus_number)
print("Destination:", bus_info.destination)
print("Language   :", bus_info.language)
print("Confidence :", bus_info.confidence)