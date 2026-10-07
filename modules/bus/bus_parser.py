"""
==========================================
AI SMART VISION
Bus OCR Intelligent Parser
==========================================

This parser extracts:

1. Bus Number
2. Destination
3. Language
4. Confidence

from OCR text.

Supported Languages

• English
• Tamil
• Hindi
• Malayalam
• Telugu
• Kannada

Author:
Hybotron
"""

from dataclasses import dataclass, field
from typing import List
import re

# ==========================================================
# Bus Information
# ==========================================================

@dataclass
class BusInfo:
    """
    Stores parsed bus information.
    """

    bus_number: str = ""

    destination: str = ""

    language: str = "unknown"

    confidence: float = 0.0

    raw_text: List[str] = field(default_factory=list)


# ==========================================================
# OCR Cleaning Symbols
# ==========================================================

REMOVE_SYMBOLS = [

    "|",
    "[",
    "]",
    "{",
    "}",
    "(",
    ")",
    "<",
    ">",
    "_",
    "=",
    "+",
    "*",
    "^",
    "~",
    "`",
    '"',
    "'",
    ";",
    ":",
    ",",
    "\\",
    "/"

]


# ==========================================================
# Common Bus Keywords
# ==========================================================

BUS_KEYWORDS = {

    "BUS",
    "TNSTC",
    "SETC",
    "MTC",
    "KSRTC",
    "APSRTC",
    "TSRTC",
    "RTC",

    "CITY",
    "EXP",
    "EXPRESS",
    "SUPER",
    "DELUXE",
    "ULTRA",
    "FAST",
    "ORDINARY",
    "SPECIAL",
    "LIMITED",
    "SERVICE"

}


# ==========================================================
# Ignore Words
# ==========================================================

IGNORE_WORDS = {

    "WELCOME",

    "STOP",

    "ENTRY",

    "EXIT",

    "EMERGENCY",

    "AIR",

    "SUSPENSION",

    "HYBRID",

    "DIESEL",

    "BS6",

    "ELECTRIC",

    "VOLVO",

    "ASHOK",

    "LEYLAND",

    "TATA"

}


# ==========================================================
# Supported Languages
# ==========================================================

SUPPORTED_LANGUAGES = {

    "english",

    "tamil",

    "hindi",

    "malayalam",

    "telugu",

    "kannada"

}


# ==========================================================
# Regular Expressions
# ==========================================================

# Examples:
# 21G
# 47B
# A12
# M500
# TN45
# 12

BUS_NUMBER_PATTERN = re.compile(

    r"^[A-Z]{0,3}\d{1,4}[A-Z]{0,3}$",

    re.IGNORECASE

)

ONLY_NUMBER_PATTERN = re.compile(

    r"^\d+$"

)

ONLY_LETTERS_PATTERN = re.compile(

    r"^[A-Za-z]+$"

)
# ==========================================================
# OCR PREPROCESSING
# ==========================================================

class BusParser:

    def __init__(self):

        pass

    # ------------------------------------------------------

    def clean_text(self, text: str) -> str:
        """
        Remove unwanted symbols and spaces.
        """

        if text is None:
            return ""

        text = text.strip()

        for symbol in REMOVE_SYMBOLS:
            text = text.replace(symbol, " ")

        # Remove multiple spaces
        text = " ".join(text.split())

        return text

    # ------------------------------------------------------

    def normalize_text(self, text: str) -> str:
        """
        Normalize OCR text.
        """

        text = self.clean_text(text)

        return text.upper()

    # ------------------------------------------------------

    def remove_duplicate_words(self, texts):
        """
        Remove duplicate OCR results.
        """

        unique = []
        seen = set()

        for text in texts:

            key = self.normalize_text(text)

            if key not in seen:

                seen.add(key)

                unique.append(text)

        return unique

    # ------------------------------------------------------

    def filter_noise(self, texts):
        """
        Remove unnecessary OCR words.
        """

        filtered = []

        for text in texts:

            t = self.normalize_text(text)

            if len(t) <= 1:
                continue

            if t in IGNORE_WORDS:
                continue

            filtered.append(text)

        return filtered

    # ------------------------------------------------------

    def prepare_ocr(self, ocr_results):
        """
        Convert PaddleOCR output into clean text list.
        """

        texts = []

        if not ocr_results:
            return texts

        for item in ocr_results:

            try:

                # Dictionary format
                if isinstance(item, dict):

                    text = item.get("text", "")

                # String format
                elif isinstance(item, str):

                    text = item

                else:
                    continue

                text = self.clean_text(text)

                if text != "":
                    texts.append(text)

            except Exception:

                continue

        texts = self.remove_duplicate_words(texts)

        texts = self.filter_noise(texts)

        return texts

    # ------------------------------------------------------

    def print_ocr(self, texts):

        print("\n========== OCR ==========")

        for t in texts:

            print(t)

        print("=========================\n")
    def bbox_center(self, bbox):
      """
        Return center (x,y) of OCR bounding box.
      """

      xs = [p[0] for p in bbox]
      ys = [p[1] for p in bbox]

      return (
        sum(xs) / len(xs),
        sum(ys) / len(ys)
      )
    def bbox_width(self, bbox):

      xs = [p[0] for p in bbox]

      return max(xs) - min(xs)
    def bbox_height(self, bbox):

     ys = [p[1] for p in bbox]

     return max(ys) - min(ys)
    def destination_score(self, item, bus_number):

     text = item["text"]

     bbox = item["bbox"]

     conf = item["conf"]

     score = 0

     score += conf * 40

     score += len(text) * 2

     score += self.bbox_width(bbox) * 0.05

     _, y = self.bbox_center(bbox)

     score += y * 0.02

     if text == bus_number:
        score -= 100

     if text.upper() in BUS_KEYWORDS:
         score -= 50

     if text.upper() in IGNORE_WORDS:
         score -= 50

     return score
# ==========================================================
# AI PARSER
# ==========================================================

    def find_bus_number(self, texts):
        """
        Detect bus number from cleaned OCR text.
        Examples:
        21G
        47B
        A12
        M500
        TN45
        12
        """

        for text in texts:

            value = self.normalize_text(text)

            if BUS_NUMBER_PATTERN.match(value):
                return value

        return ""


    # ------------------------------------------------------

    def find_destination(self, texts, bus_number):
        """
        Detect destination.

        Strategy:
        1. Ignore bus number
        2. Ignore bus keywords
        3. Ignore noise words
        4. Choose longest remaining text
        """

        candidates = []

        for text in texts:

            value = self.normalize_text(text)

            if value == "":
                continue

            if value == bus_number:
                continue

            if value in BUS_KEYWORDS:
                continue

            if value in IGNORE_WORDS:
                continue

            if len(value) < 2:
                continue

            candidates.append(text)

        if len(candidates) == 0:
            return ""

        return max(candidates, key=len)


    # ------------------------------------------------------

    def detect_language(self, text):

        if text == "":
            return "unknown"

        for ch in text:

            code = ord(ch)

            # Tamil
            if 0x0B80 <= code <= 0x0BFF:
                return "tamil"

            # Telugu
            if 0x0C00 <= code <= 0x0C7F:
                return "telugu"

            # Kannada
            if 0x0C80 <= code <= 0x0CFF:
                return "kannada"

            # Malayalam
            if 0x0D00 <= code <= 0x0D7F:
                return "malayalam"

            # Hindi
            if 0x0900 <= code <= 0x097F:
                return "hindi"

        return "english"


    # ------------------------------------------------------

    def calculate_confidence(
            self,
            bus_number,
            destination):

        score = 0.0

        if bus_number:
            score += 0.60

        if destination:
            score += 0.40

        return round(score, 2)


    # ------------------------------------------------------

    def parse(self, ocr_results):
        """
        Main parser.

        Input:
            OCR output from read_text()

        Output:
            BusInfo
        """

        texts = self.prepare_ocr(ocr_results)

        info = BusInfo()

        info.raw_text = texts

        info.bus_number = self.find_bus_number(texts)

        info.destination = self.find_destination(
            texts,
            info.bus_number
        )

        info.language = self.detect_language(
            info.destination
        )

        info.confidence = self.calculate_confidence(
            info.bus_number,
            info.destination
        )

        return info