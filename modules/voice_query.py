import speech_recognition as sr

recognizer = sr.Recognizer()


# ---------------- LISTEN TO USER ----------------
def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)
            command = recognizer.recognize_google(audio)
            command = command.lower().strip()
            print("You said:", command)
            return command

        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None
        except sr.WaitTimeoutError:
            return None


def extract_object(command):

    if not command:
        return None

    command = command.lower().strip()

    prefixes = [

        "where is the ",
        "where is ",

        "what is the colour of the ",
        "what is the color of the ",

        "what colour is the ",
        "what color is the ",

        "colour of the ",
        "color of the ",

        "find the ",
        "find "
    ]

    for p in prefixes:
        if command.startswith(p):
            command = command[len(p):]
            break

    command = command.strip()

    return command if command else None


# ---------------- SCENE DESCRIPTION ----------------
def describe_scene(objects):
    left = []
    center = []
    right = []

    for obj in objects:
        name = obj["name"].lower()
        side = obj["side"]

        if side == "left":
            left.append(name)
        elif side == "right":
            right.append(name)
        else:
            center.append(name)

    parts = []

    if left:
        parts.append(f"{left[0].capitalize()} is on your left")

    if center:
        parts.append(f"{center[0].capitalize()} is in the center")

    if right:
        parts.append(f"{right[0].capitalize()} is on your right")

    if not parts:
        return "No important objects detected around you."

    if len(parts) == 1:
        return parts[0] + "."
    elif len(parts) == 2:
        return parts[0] + " and " + parts[1] + "."
    else:
        return parts[0] + ", " + parts[1] + ", and " + parts[2] + "."
    
def is_currency_question(command):
    if command is None:
        return False

    command = command.lower()

    keywords = [
        "how much is this",
        "how much money",
        "currency",
        "money",
        "rupees",
        "note",
        "identify money",
        "identify currency"
    ]

    return any(k in command for k in keywords)


def is_bus_question(command):
    if command is None:
        return False

    command = command.lower()

    keywords = [
        "bus number",
        "which bus",
        "read bus",
        "bus"
    ]

    return any(k in command for k in keywords)


def is_sign_question(command):
    if command is None:
        return False

    command = command.lower()

    keywords = [
        "read board",
        "read sign",
        "what is written",
        "read text"
    ]

    return any(k in command for k in keywords)