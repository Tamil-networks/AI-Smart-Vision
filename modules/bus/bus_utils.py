"""
====================================================
AI Smart Vision Assistant
Bus Utility Functions

Author : Hybotron
====================================================
"""

import re
import math
from typing import List, Dict


# --------------------------------------------------
# TEXT FUNCTIONS
# --------------------------------------------------

def clean_text(text: str) -> str:
    """
    Clean OCR text.
    """

    if text is None:
        return ""

    text = text.strip()

    text = re.sub(r"\s+", " ", text)

    return text


def normalize_text(text: str) ->str:
    """
    Normalize OCR output.
    """

    text = clean_text(text)

    return text.upper()


# --------------------------------------------------
# OCR
# --------------------------------------------------

def remove_duplicate_texts(texts: List[str]) -> List[str]:
    """
    Remove duplicate OCR results.
    """

    unique = []

    for t in texts:

        t = clean_text(t)

        if t and t not in unique:
            unique.append(t)

    return unique


def filter_short_texts(texts: List[str], minimum=2):

    result = []

    for t in texts:

        if len(clean_text(t)) >= minimum:

            result.append(t)

    return result


# --------------------------------------------------
# BUS NUMBER
# --------------------------------------------------

BUS_NUMBER_PATTERNS = [

    r"^\d{1,4}$",              # 12
    r"^\d{1,4}[A-Z]$",         # 21G
    r"^[A-Z]\d{1,4}$",         # M15
    r"^\d+[A-Z]+\d*$",         # 47B
    r"^[A-Z]{1,3}\d+$",        # TN21

]


def is_bus_number(text: str) -> bool:

    text = normalize_text(text)

    for pattern in BUS_NUMBER_PATTERNS:

        if re.fullmatch(pattern, text):

            return True

    return False


# --------------------------------------------------
# BOUNDING BOX
# --------------------------------------------------

def bbox_center(box):

    """
    box =
    [[x1,y1],
     [x2,y2],
     [x3,y3],
     [x4,y4]]
    """

    xs = [p[0] for p in box]

    ys = [p[1] for p in box]

    return (

        sum(xs) / len(xs),

        sum(ys) / len(ys)

    )


def bbox_width(box):

    x1 = box[0][0]

    x2 = box[1][0]

    return abs(x2 - x1)


def bbox_height(box):

    y1 = box[0][1]

    y4 = box[3][1]

    return abs(y4 - y1)


# --------------------------------------------------
# DISTANCE
# --------------------------------------------------

def euclidean_distance(p1, p2):

    return math.sqrt(

        (p1[0]-p2[0])**2 +

        (p1[1]-p2[1])**2

    )


# --------------------------------------------------
# SORTING
# --------------------------------------------------

def sort_top_to_bottom(results):

    """
    Sort OCR lines.
    """

    return sorted(

        results,

        key=lambda x: bbox_center(x["bbox"])[1]

    )


def sort_left_to_right(results):

    return sorted(

        results,

        key=lambda x: bbox_center(x["bbox"])[0]

    )


# --------------------------------------------------
# OCR CONFIDENCE
# --------------------------------------------------

def filter_by_confidence(results, minimum=0.45):

    output = []

    for item in results:

        if item["conf"] >= minimum:

            output.append(item)

    return output


# --------------------------------------------------
# TEXT EXTRACTION
# --------------------------------------------------

def get_only_text(results):

    texts = []

    for item in results:

        texts.append(item["text"])

    return texts


# --------------------------------------------------
# OPERATOR
# --------------------------------------------------

KNOWN_OPERATORS = [

    "TNSTC",

    "SETC",

    "MTC",

    "KSRTC",

    "BMTC",

    "APSRTC",

    "TSRTC",

    "KERALA",

    "GOVT"

]


def is_operator(text):

    text = normalize_text(text)

    for op in KNOWN_OPERATORS:

        if op in text:

            return True

    return False


# --------------------------------------------------
# DEBUG
# --------------------------------------------------

def print_results(results):

    print("\n----------- OCR RESULTS -----------")

    for r in results:

        print(

            f"{r['text']}"

            f" | Conf={r['conf']:.2f}"

        )

    print("-----------------------------------")