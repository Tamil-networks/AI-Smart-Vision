"""
====================================================
AI Smart Vision Assistant
Bus Language Detection

Author : Hybotron
====================================================
"""

import re

from langdetect import detect
from langdetect import DetectorFactory

DetectorFactory.seed = 0


# ---------------------------------------------------
# Unicode Script Detection
# ---------------------------------------------------

TAMIL = re.compile(r'[\u0B80-\u0BFF]')
HINDI = re.compile(r'[\u0900-\u097F]')
TELUGU = re.compile(r'[\u0C00-\u0C7F]')
KANNADA = re.compile(r'[\u0C80-\u0CFF]')
MALAYALAM = re.compile(r'[\u0D00-\u0D7F]')
GUJARATI = re.compile(r'[\u0A80-\u0AFF]')
BENGALI = re.compile(r'[\u0980-\u09FF]')
PUNJABI = re.compile(r'[\u0A00-\u0A7F]')
ORIYA = re.compile(r'[\u0B00-\u0B7F]')
URDU = re.compile(r'[\u0600-\u06FF]')
CHINESE = re.compile(r'[\u4E00-\u9FFF]')
JAPANESE = re.compile(r'[\u3040-\u30FF]')
KOREAN = re.compile(r'[\uAC00-\uD7AF]')
THAI = re.compile(r'[\u0E00-\u0E7F]')
ARABIC = re.compile(r'[\u0600-\u06FF]')
RUSSIAN = re.compile(r'[\u0400-\u04FF]')


# ---------------------------------------------------
# Language Names
# ---------------------------------------------------

LANGUAGE_NAMES = {

    "en": "English",
    "ta": "Tamil",
    "hi": "Hindi",
    "te": "Telugu",
    "kn": "Kannada",
    "ml": "Malayalam",
    "gu": "Gujarati",
    "bn": "Bengali",
    "pa": "Punjabi",
    "or": "Odia",
    "ur": "Urdu",
    "ja": "Japanese",
    "zh": "Chinese",
    "ko": "Korean",
    "th": "Thai",
    "ar": "Arabic",
    "ru": "Russian"

}


# ---------------------------------------------------
# Unicode Detection
# ---------------------------------------------------

def detect_by_unicode(text):

    if TAMIL.search(text):
        return "ta"

    if HINDI.search(text):
        return "hi"

    if TELUGU.search(text):
        return "te"

    if KANNADA.search(text):
        return "kn"

    if MALAYALAM.search(text):
        return "ml"

    if GUJARATI.search(text):
        return "gu"

    if BENGALI.search(text):
        return "bn"

    if PUNJABI.search(text):
        return "pa"

    if ORIYA.search(text):
        return "or"

    if URDU.search(text):
        return "ur"

    if CHINESE.search(text):
        return "zh"

    if JAPANESE.search(text):
        return "ja"

    if KOREAN.search(text):
        return "ko"

    if THAI.search(text):
        return "th"

    if ARABIC.search(text):
        return "ar"

    if RUSSIAN.search(text):
        return "ru"

    return None


# ---------------------------------------------------
# Main Detection
# ---------------------------------------------------

def detect_language(texts):
    """
    Input:
        list of OCR strings

    Output:
        en
        ta
        hi
        te
        ...
    """

    if isinstance(texts, list):
        text = " ".join(texts)
    else:
        text = str(texts)

    text = text.strip()

    if len(text) == 0:
        return "en"

    # First use Unicode detection (fast and reliable)
    unicode_lang = detect_by_unicode(text)

    if unicode_lang:
        return unicode_lang

    # Fallback to langdetect
    try:

        lang = detect(text)

        if lang in LANGUAGE_NAMES:
            return lang

    except Exception:
        pass

    return "en"


# ---------------------------------------------------
# Language Name
# ---------------------------------------------------

def language_name(code):

    return LANGUAGE_NAMES.get(code, "Unknown")


# ---------------------------------------------------
# English Check
# ---------------------------------------------------

def is_english(text):

    return all(ord(c) < 128 for c in text)


# ---------------------------------------------------
# Mixed Language
# ---------------------------------------------------

def contains_multiple_languages(text):

    count = 0

    patterns = [

        TAMIL,
        HINDI,
        TELUGU,
        KANNADA,
        MALAYALAM,
        GUJARATI,
        BENGALI,
        PUNJABI,
        ORIYA,
        URDU,
        CHINESE,
        JAPANESE,
        KOREAN,
        THAI,
        ARABIC,
        RUSSIAN

    ]

    for pattern in patterns:

        if pattern.search(text):
            count += 1

    if is_english(text):
        count += 1

    return count > 1


# ---------------------------------------------------
# Debug
# ---------------------------------------------------

if __name__ == "__main__":

    samples = [

        "MADURAI",

        "நத்தம்",

        "ಬೆಂಗಳೂರು",

        "തിരുവനന്തപുരം",

        "दिल्ली",

        "東京",

        "北京",

        "서울"

    ]

    for sample in samples:

        code = detect_language(sample)

        print(
            sample,
            "->",
            code,
            "(",
            language_name(code),
            ")"
        )