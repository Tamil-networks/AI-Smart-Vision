import cv2
from config import LANGUAGE
from modules.camera import get_frame
from modules.object_detector import detect_objects
from modules.safety_logic import generate_instruction
from modules.translator import translate_text
from modules.voice_output import speak

last_spoken = ""

while True:
    frame = get_frame()
    if frame is None:
         continue
    objects = detect_objects(frame)
    if objects:
         #first=objects[0]
         obj=objects[0]

         instruction = generate_instruction(obj)

         translated = translate_text(instruction,LANGUAGE)

         if translated!= last_spoken:
               print("Output:",translated)
               speak(translated,LANGUAGE)
               last_spoken = translated
         #message = f"{first['name']} detected on your {first['side']}"
         #if message != last_spoken:
          #    print(message)
           #   speak(message, LANGUAGE)
            #  last_spoken = message

    cv2.imshow("AI Smart Vision Assistant Detection", frame)

    if cv2.waitKey(1) == 27:
              break 
        
cv2.destroyAllWindows()  