import cv2
import time
from config import LANGUAGE
from modules.camera import get_frame
from modules.object_detector import detect_objects
from modules.path_planner import plan_path
from modules.safety_logic import generate_instruction
from modules.voice_output import speak
from modules.voice_query import listen_command, extract_object, describe_scene
from modules.currency_detector import CurrencyDetector
from modules.currency_memory import CurrencyMemory
from modules.currency_voice import build_sentence, build_not_found
from modules.currency_query import CurrencyQuery

# ---------------- MEMORY ----------------
spoken_memory = {}

# Cooldown for same alert
COOLDOWN = 5

announced_zones = {}
# Minimum gap between audio messages
GLOBAL_SPEAK_GAP = 3

# Path reminder interval
PATH_COOLDOWN = 8

# Last path spoken
last_path = ""
last_path_time = 0

# Last audio time
last_speak_time = 0

# ---------------- CURRENCY MODULE ----------------

currency_detector = CurrencyDetector()

currency_memory = CurrencyMemory()

currency_query = CurrencyQuery()

# ---------------- VOICE Q&A FUNCTION ----------------
def answer_query(command, objects, currencies):
    if command is None:
        return None

    command = command.lower()
    command = command.replace("colour", "color")

    # -------- Scene Description --------
    if "what is front of me" in command or "what is in front of me" in command:
        return describe_scene(objects)
    
    # ---------- Currency ----------

    if "currency" in command or \
      "note" in command or \
      "money" in command:

      if len(currencies) == 0:
         return "I cannot find any currency."

      note = currencies[0]["note"]

      return build_sentence(note)
    
    # -------- COLOR DETECTION --------
    if "color" in command:

      target = extract_object(command)

      if target:

        for obj in objects:

            if obj["name"].lower() == target:

                return f"The {target} is {obj['color']}."

        return f"I cannot find {target}."
    
    # -------- Object Location --------
    target = extract_object(command)

    if target:
        for obj in objects:
            if obj["name"].lower() == target:
                side = obj["side"]

                if side == "front":
                    return f"{target.capitalize()} is in front of you."
                else:
                    return f"{target.capitalize()} is on your {side}."

        return f"I cannot find {target}."

    return "I did not understand the question."

# ---------------- MAIN LOOP ----------------
while True:
    frame = get_frame()
    if frame is None:
        continue

    objects = detect_objects(frame)
    currency = currency_detector.detect_best(frame)

    currencies = []

    if currency:

      currencies.append({

         "note": currency["label"],

         "confidence": currency["confidence"],

         "bbox": currency["bbox"]

       })
      for note in currencies:

       x1, y1, x2, y2 = note["bbox"]

       cv2.rectangle(frame,
                  (x1, y1),
                  (x2, y2),
                  (0,255,0),
                  2)

       cv2.putText(frame,
                f"₹{note['note']}",
                (x1, y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,0),
                2)
    current_time = time.time()

    # ---------------- PATH PLANNING ----------------
    if objects:
        frame_width = frame.shape[1]
        path = plan_path(objects, frame_width)
        recommendation = path["recommendation"]

        if recommendation is not None:
          if recommendation != last_path:
            print("Path Recommendation:", recommendation)
            speak(recommendation, LANGUAGE)
            last_speak_time = time.time()
            last_path = recommendation
            last_path_time = current_time

          elif current_time - last_path_time >= PATH_COOLDOWN:
            print("Path Reminder:", recommendation)
            speak(recommendation, LANGUAGE)
            last_speak_time = time.time()
            last_path_time = current_time

            # Reminder after a few seconds
    
    # ---------------- DANGER ALERTS ----------------
    for obj in objects:
       instruction = generate_instruction(obj)

       # Ignore objects that should not generate alerts
       if instruction is None:
         continue

       # These variables MUST be inside the loop
       name = obj["name"].lower()
       side = obj["side"]
       d = obj["distance_m"]

       # Determine zone
       zone = None

       # Case-1
       if 0.31 <= d <= 0.50:
         zone = "case1_warning"
       elif 0.10 <= d <= 0.30:
         zone = "case1_critical"

       # Case-2
       elif 1.0 <= d <= 1.50:
         zone = "case2_warning"
       elif 0.60 <= d < 1.0:
         zone = "case2_critical"

       # Case-3
       elif 2.5 <= d <= 3.0:
         zone = "case3_warning"
       elif 1.5 <= d < 2.5:
         zone = "case3_critical"

       # Skip if outside all zones
       if zone is None:
         continue

       # Create unique key
       key = f"{name}_{side}_{zone}"

       # Speak only once per zone
       if key not in announced_zones:
          print("ALERT:", instruction)
          speak(instruction, LANGUAGE)
          announced_zones[key] = True



    # ---------------- DISPLAY CAMERA ----------------
    cv2.imshow("AI Smart Vision Assistant", frame)

    # ---------------- KEYBOARD INPUT ----------------
    key = cv2.waitKey(1) & 0xFF

    # Press V for Voice Q&A
    if key == ord('v') or key == ord('V'):

      print("Voice Q&A activated")

      command = listen_command()

      print("Command received:", command)
      reply = None

      if command:

          intent = currency_query.extract_query(command)

          if intent == "detect_currency":

            if len(currencies) == 0:

                reply = build_not_found()

            else:

                note = currencies[0]["note"]

                if currency_memory.should_speak(note):

                    reply = build_sentence(note)

          else:

            reply = answer_query(command, objects, currencies)

      print("Generated reply:", reply)

      if reply:

            print("Q&A:", reply)

            speak(reply, LANGUAGE)

    # Press ESC to exit
    elif key == 27:

      break

cv2.destroyAllWindows()