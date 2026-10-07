import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

for i, voice in enumerate(voices):
    print("=" * 50)
    print("Index :", i)
    print("Name  :", voice.name)
    print("ID    :", voice.id)