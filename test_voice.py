from config import LANGUAGE
from modules.voice_output import speak
#speak("உங்கள் இடது பக்கத்தில் கார் மிக அருகில் உள்ளது. வலப்புறம் நகர்ந்து பாதுகாப்பாக செல்லுங்கள்.", "ta")
message = "Car is very close on your left. Move right and go safely."
speak(message, LANGUAGE)