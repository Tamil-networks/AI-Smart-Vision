"""
====================================================
AI Smart Vision Assistant
Bus Voice Generator

Author : Hybotron
====================================================
"""

from .bus_language import detect_language


# -------------------------------------------------
# Voice Templates
# -------------------------------------------------

VOICE_TEMPLATES = {

    "en": {
        "full":
            "Bus number {number} is going to {destination}.",
        "number":
            "Bus number {number} detected.",
        "destination":
            "Bus going to {destination} detected.",
        "unknown":
            "Bus detected."
    },

    "ta": {
        "full":
            "பேருந்து எண் {number} {destination} செல்கிறது.",
        "number":
            "பேருந்து எண் {number}.",
        "destination":
            "{destination} செல்லும் பேருந்து.",
        "unknown":
            "பேருந்து கண்டறியப்பட்டது."
    },

    "hi": {
        "full":
            "बस संख्या {number} {destination} जा रही है।",
        "number":
            "बस संख्या {number}.",
        "destination":
            "{destination} जाने वाली बस।",
        "unknown":
            "बस मिली।"
    },

    "te": {
        "full":
            "{destination} కు వెళ్తున్న బస్సు సంఖ్య {number}.",
        "number":
            "బస్సు సంఖ్య {number}.",
        "destination":
            "{destination} వెళ్తున్న బస్సు.",
        "unknown":
            "బస్సు గుర్తించబడింది."
    },

    "kn": {
        "full":
            "{destination} ಗೆ ಹೋಗುವ ಬಸ್ ಸಂಖ್ಯೆ {number}.",
        "number":
            "ಬಸ್ ಸಂಖ್ಯೆ {number}.",
        "destination":
            "{destination} ಗೆ ಹೋಗುವ ಬಸ್.",
        "unknown":
            "ಬಸ್ ಪತ್ತೆಯಾಗಿದೆ."
    },

    "ml": {
        "full":
            "{destination} പോകുന്ന ബസ് നമ്പർ {number}.",
        "number":
            "ബസ് നമ്പർ {number}.",
        "destination":
            "{destination} പോകുന്ന ബസ്.",
        "unknown":
            "ബസ് കണ്ടെത്തി."
    }

}


# -------------------------------------------------
# Helper
# -------------------------------------------------

def get_template(language):

    return VOICE_TEMPLATES.get(
        language,
        VOICE_TEMPLATES["en"]
    )


# -------------------------------------------------
# Main
# -------------------------------------------------

def build_sentence(
    bus_number=None,
    destination=None,
    operator=None,
    language=None
):
    """
    Returns a spoken sentence.

    Example

    Bus number 21G is going to Madurai.
    """

    # Detect language if not supplied
    if language is None:

        samples = []

        if destination:
            samples.append(destination)

        if operator:
            samples.append(operator)

        language = detect_language(samples)

    template = get_template(language)

    # -----------------------------

    if bus_number and destination:

        return template["full"].format(

            number=bus_number,

            destination=destination

        )

    # -----------------------------

    if bus_number:

        return template["number"].format(

            number=bus_number

        )

    # -----------------------------

    if destination:

        return template["destination"].format(

            destination=destination

        )

    # -----------------------------

    return template["unknown"]


# -------------------------------------------------
# Detailed Voice
# -------------------------------------------------

def build_detailed_sentence(info):
    """
    info = BusInfo object
    """

    return build_sentence(

        bus_number=info.bus_number,

        destination=info.destination,

        operator=info.operator,

        language=info.language

    )


# -------------------------------------------------
# Debug
# -------------------------------------------------

if __name__ == "__main__":

    print(

        build_sentence(

            bus_number="21G",

            destination="MADURAI"

        )

    )

    print(

        build_sentence(

            bus_number="4",

            destination="நத்தம்"

        )

    )

    print(

        build_sentence(

            bus_number="15A",

            destination="ಬೆಂಗಳೂರು"

        )

    )