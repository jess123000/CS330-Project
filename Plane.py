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

    def assignSeat(self, seatType: str, currentSeat:list = None, size:int = None) -> (Point, int):
        if seatType == "business":
            # if a seat had already been assigned
            if currentSeat:
                # check if there is any better seat
                pass
            # else if there's not enough room in the flight
            elif self.availableSeatsNum < 1:
                # display flight is full and wait
                self.flightFullText.draw(self.win)
                point = self.win.getMouse()
                self.flightFullText.undraw()
                return point, None
            # else assign a new seat
            else:
                self.numGroups += 1
                self.availableSeatsNum -= 1
                seat = self.availableSeats[0]
                if seat < 12:
                    self.customerSatisfactionIndex.append(5)
                else:
                    self.customerSatisfactionIndex.append(-5)
                    seat = [seat]
                point = self.win.getMouse()
                self.flightFullText.undraw()
                return point, seat
        elif seatType == "tourist":
            # if a seat had already been assigned
            if currentSeat:
                # check if there is any better seat
                pass
            # else if there's not enough room in the flight
            elif self.availableSeatsNum < 2:
                # display flight is full and wait
                self.flightFullText.draw(self.win)
                point = self.win.getMouse()
                self.flightFullText.undraw()
                return point, None
            # else assign a new seat
            else:
                self.numGroups += 1
                self.availableSeats -= 2
        elif seatType == "family":
            # if a seat had already been assigned
            if currentSeat:
                # check if there is any better seat
                pass
            # else if there's not enough room in the flight
            elif self.availableSeatsNum < size:
                # display flight is full and wait
                self.flightFullText.draw(self.win)
                point = self.win.getMouse()
                self.flightFullText.undraw()
                return point, None
            # else assign a new seat
            else:
                self.numGroups += 1
                self.availableSeats -= size
