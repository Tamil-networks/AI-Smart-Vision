"""
==========================================
AI SMART VISION
Currency Memory
==========================================

Prevents repeated announcements
of the same currency.

Author:
Hybotron
"""

import time


class CurrencyMemory:

    def __init__(self, cooldown=5):

        self.last_note = None
        self.last_time = 0

        self.cooldown = cooldown

    # -------------------------------------

    def should_speak(self, note):

        """
        Returns True if currency
        should be spoken.
        """

        now = time.time()

        # Different currency
        if note != self.last_note:

            self.last_note = note
            self.last_time = now

            return True

        # Same currency after cooldown
        if now - self.last_time >= self.cooldown:

            self.last_time = now

            return True

        return False

    # -------------------------------------

    def reset(self):

        """
        Clears memory.
        """

        self.last_note = None
        self.last_time = 0