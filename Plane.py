#!/usr/bin/env python3

# --------------------------------------------------
# FLightsGUI.py
# Alex Harris and Dez Turkson
# March/April 2021
# --------------------------------------------------

from graphics import *

class Plane:

    def __init__(self, win: GraphWin):
        self.availableSeats = []
        for i in range(120):
            self.availableSeats.append(i)
        self.takenSeats = []
        self.availableSeatsNum = 120
        self.customerSatisfactionIndex = []
        self.numGroups = 0
        self.win = win
        self.flightFullText = Text(Point(500, 100), "Flight full")
        self.noBetterSeatText = Text(Point(500, 100), "No Better Seat Available")

    def flightFull(self, currentSeat:list) -> (Point, int):
        # display flight is full and wait
        self.flightFullText.draw(self.win)
        pt = self.win.getMouse()
        self.flightFullText.undraw()
        return pt, currentSeat

    def noBetterSeat(self, currentSeat:list) -> (Point, int):
        # display no better seat and wait
        self.noBetterSeatText.draw(self.win)
        pt = self.win.getMouse()
        self.noBetterSeatText.undraw()
        return pt, currentSeat

    def assignSeat(self, seatType: str, currentSeat:list = None, size:int = None) -> (Point, int):
        if seatType == "business":
            # if a seat had already been assigned
            if currentSeat:
                # see if there's seats available
                if self.availableSeatsNum < size:
                    return self.noBetterSeat(currentSeat)
                # see if the seats are worse
                elif self.availableSeats[0] > 12:
                    return self.noBetterSeat(currentSeat)
                # if neither are true, assign the new seat and wait for click
                else:
                    seat = self.availableSeats[0]
                    # TODO draw ticket
                    pt = self.win.getMouse()
                    return pt, seat
            # else if there's not enough room in the flight
            elif self.availableSeatsNum < size:
                self.flightFull(currentSeat)
            # else assign a new seat
            else:
                # add how many groups are in the flight
                self.numGroups += 1
                # subtract the amount of seats available
                self.availableSeatsNum -= size
                seat = self.availableSeats[0]
                if seat < 12:
                    self.customerSatisfactionIndex.append(5)
                else:
                    self.customerSatisfactionIndex.append(-5)
                # TODO draw ticket
                pt = self.win.getMouse()
                return pt, seat
        elif seatType == "tourist":
            # if a seat had already been assigned
            if currentSeat:
                # check if there is any better seat
                if len(self.availableSeats) < size:
                    return self.noBetterSeat(currentSeat)
                else:
                    # TODO draw ticket
                    pass
            # else if there's not enough room in the flight
            elif self.availableSeatsNum < size:
                return self.flightFull(currentSeat)
            # else assign a new seat
            else:
                self.numGroups += 1
                self.availableSeats -= size
                # TODO draw ticket
        elif seatType == "family":
            # if a seat had already been assigned
            if currentSeat:
                # check if there is any better seat
                if len(self.availableSeats) < size:
                    return self.noBetterSeat(currentSeat)
                else:
                    # TODO draw ticket
                    pass
            # else if there's not enough room in the flight
            elif self.availableSeatsNum < size:
                self.flightFull(currentSeat)
            # else assign a new seat
            else:
                self.numGroups += 1
                self.availableSeats -= size
                # TODO draw ticket
