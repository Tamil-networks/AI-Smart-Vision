"""
=====================================================
AI Smart Vision Assistant
Bus Detection Configuration
Author : Hybotron
=====================================================
"""

from pathlib import Path

# ---------------------------------------------------
# Project Root
# ---------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# ---------------------------------------------------
# Bus Detection
# ---------------------------------------------------

ENABLE_BUS_DETECTION = True

# YOLO model path (change if required)
BUS_MODEL_PATH = PROJECT_ROOT / "models" / "bus.pt"

# Minimum confidence for detecting a bus
BUS_CONFIDENCE = 0.50

# ---------------------------------------------------
# OCR
# ---------------------------------------------------

ENABLE_OCR = True

OCR_CONFIDENCE = 0.45

# OCR Languages
# (Future use if multiple OCR engines are supported)
OCR_LANGUAGES = [
    "en",
    "ta",
    "hi",
    "te",
    "ml",
    "kn"
]

# ---------------------------------------------------
# Bus Parser
# ---------------------------------------------------

ENABLE_BUS_NUMBER = True
ENABLE_DESTINATION = True
ENABLE_OPERATOR = True

# Maximum OCR text length
MAX_TEXT_LENGTH = 100

# ---------------------------------------------------
# Voice
# ---------------------------------------------------

ENABLE_VOICE = True

VOICE_REPEAT_DELAY = 10      # seconds

VOICE_SPEED = 170

# ---------------------------------------------------
# Camera
# ---------------------------------------------------

FRAME_WIDTH = 1280
FRAME_HEIGHT = 720

# ---------------------------------------------------
# Cropping
# ---------------------------------------------------

# Upper portion of bus generally contains
# number and destination display

BUS_TOP_RATIO = 0.45

# ---------------------------------------------------
# Logging
# ---------------------------------------------------

DEBUG = True

SHOW_OCR = True
SHOW_CROPPED_BUS = False
SHOW_PARSER_RESULT = True

# ---------------------------------------------------
# Future AI
# ---------------------------------------------------

ENABLE_LLM_PARSER = False

LLM_MODEL = None