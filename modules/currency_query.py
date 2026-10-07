"""
==========================================
AI SMART VISION
Currency Query Detector
==========================================

Detects whether the user's
voice command is asking about
currency.

Author:
Hybotron
"""

import re


class CurrencyQuery:

    def __init__(self):

        self.patterns = [

            # General
            r"money",
            r"currency",
            r"cash",
            r"note",
            r"rupees",
            r"rupee",

            # Questions
            r"how much money",
            r"how much is this",
            r"how much is this money",
            r"what currency",
            r"what note",
            r"which note",
            r"identify currency",
            r"identify note",
            r"identify this",
            r"read money",
            r"read currency",
            r"read note",

            # Simple commands
            r"detect currency",
            r"detect money",
            r"detect note",
            r"recognize currency",
            r"recognize money",
            r"recognize note"

        ]

    # -----------------------------------------------------

    def is_currency_query(self, text):

        """
        Returns True if the user
        is asking about currency.
        """

        if text is None:
            return False

        text = text.lower().strip()

        for pattern in self.patterns:

            if re.search(pattern, text):

                return True

        return False

    # -----------------------------------------------------

    def extract_query(self, text):

        """
        Returns:

            detect_currency

        or

            None
        """

        if self.is_currency_query(text):

            return "detect_currency"

        return None