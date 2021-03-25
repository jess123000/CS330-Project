#!/usr/bin/env python3

# --------------------------------------------------
# FLightsGUI.py
# Alex Harris and Dez Turkson
# March/April 2021
# --------------------------------------------------

class Plane:

    def __init__(self):
        self.availableSeats = []
        for i in range(120):
            self.availableSeats.append(f"seat {i}")
        self.takenSeats = []
        self.availableSeatsNum = 120
        self.customerSatisfactionIndex = [int]
        self.numGroups = 0

    def addSatisfactionIndex(self):
        pass

    def assignSeat(self, seatType: str, currentSeat:list = None, size:int = None) -> bool:
        if seatType == "business":
            # if a seat had already been assigned
            if currentSeat:
                pass
            # else if there's not enough room in the flight
            elif self.availableSeatsNum < 1:
                return True
            else:
                self.numGroups += 1
                self.availableSeatsNum -= 1
        elif seatType == "tourist":
            # if a seat had already been assigned
            if currentSeat:
                pass
            # else if there's not enough room in the flight
            elif self.availableSeatsNum < 2:
                return True
            else:
                self.numGroups += 1
                self.availableSeats -= 2
        elif seatType == "family":
            # if a seat had already been assigned
            if currentSeat:
                pass
            # else if there's not enough room in the flight
            elif self.availableSeatsNum < size:
                return True
            else:
                self.numGroups += 1
                self.availableSeats -= size
