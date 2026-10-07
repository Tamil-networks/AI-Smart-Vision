"""
====================================================
AI Smart Vision Assistant
Bus Memory Manager

Author : Hybotron
====================================================
"""

import time


class BusMemory:

    def __init__(self, repeat_delay=10):

        self.repeat_delay = repeat_delay

        self.last_bus_number = None

        self.last_destination = None

        self.last_operator = None

        self.last_time = 0


    # ------------------------------------------
    # Reset Memory
    # ------------------------------------------

    def reset(self):

        self.last_bus_number = None

        self.last_destination = None

        self.last_operator = None

        self.last_time = 0


    # ------------------------------------------
    # Build Unique ID
    # ------------------------------------------

    def _create_id(self,
                   bus_number,
                   destination,
                   operator):

        return (

            str(bus_number),

            str(destination),

            str(operator)

        )


    # ------------------------------------------
    # Check New Bus
    # ------------------------------------------

    def is_new_bus(self,
                   bus_number,
                   destination,
                   operator=None):

        current = self._create_id(

            bus_number,

            destination,

            operator

        )

        previous = self._create_id(

            self.last_bus_number,

            self.last_destination,

            self.last_operator

        )

        return current != previous


    # ------------------------------------------
    # Time Check
    # ------------------------------------------

    def time_expired(self):

        return (

            time.time()

            - self.last_time

        ) >= self.repeat_delay


    # ------------------------------------------
    # Can Speak?
    # ------------------------------------------

    def should_speak(self,
                     bus_number,
                     destination,
                     operator=None):

        if self.is_new_bus(

                bus_number,

                destination,

                operator):

            return True

        if self.time_expired():

            return True

        return False


    # ------------------------------------------
    # Save Current Bus
    # ------------------------------------------

    def update(self,
               bus_number,
               destination,
               operator=None):

        self.last_bus_number = bus_number

        self.last_destination = destination

        self.last_operator = operator

        self.last_time = time.time()


    # ------------------------------------------
    # Get Current Memory
    # ------------------------------------------

    def current_bus(self):

        return {

            "bus_number": self.last_bus_number,

            "destination": self.last_destination,

            "operator": self.last_operator,

            "time": self.last_time

        }


# ----------------------------------------------------
# Global Memory Object
# ----------------------------------------------------

bus_memory = BusMemory()