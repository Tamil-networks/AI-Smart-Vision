"""
==========================================
AI SMART VISION
Currency Voice Generator
==========================================

Converts detected currency
into natural voice sentences.

Author:
Hybotron
"""


NUMBER_TO_WORD = {

    "10": "ten",
    "20": "twenty",
    "50": "fifty",
    "100": "one hundred",
    "200": "two hundred",
    "500": "five hundred",
    "2000": "two thousand"

}


def number_to_words(note):

    """
    Convert note value to words.
    """

    note = str(note)

    return NUMBER_TO_WORD.get(note, note)


# ---------------------------------------------------


def build_sentence(note):

    """
    Build voice sentence.

    Example:

    Input:
        500

    Output:
        This is five hundred rupees.
    """

    words = number_to_words(note)

    return f"This is {words} rupees."


# ---------------------------------------------------


def build_not_found():

    """
    Voice when currency
    cannot be detected.
    """

    return "I cannot find any currency."


# ---------------------------------------------------


def build_multiple(notes):

    """
    Example:

    Input:
        ["500","100","20"]

    Output:

    I can see three currency notes.
    Five hundred rupees,
    One hundred rupees,
    Twenty rupees.
    """

    if len(notes) == 0:

        return build_not_found()

    if len(notes) == 1:

        return build_sentence(notes[0])

    message = f"I can see {len(notes)} currency notes. "

    for note in notes:

        message += f"{number_to_words(note)} rupees. "

    return message.strip()