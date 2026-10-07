from gtts import gTTS
from playsound import playsound
import os
import time

is_speaking = False

def speak(text, lang="en"):
    global is_speaking

    # Ignore if already speaking
    if is_speaking:
        return

    try:
        is_speaking = True
        filename = "temp_voice.mp3"

        # Generate speech
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)

        # Play audio
        playsound(filename)

        # Small delay before cleanup
        time.sleep(0.1)

        # Remove temporary file
        if os.path.exists(filename):
            os.remove(filename)

    finally:
        is_speaking = False

