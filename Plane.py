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
        self.availableSeatsNum = 120
        self.customerSatisfactionIndex = [int]
        self.numGroups = 0
        self.win = win
        self.flightFullText = Text(Point(500, 100), "Flight full")
        self.noBetterSeatText = Text(Point(500, 100), "No Better Seat Available")
        # a = left window, b = left middle, c = left aisle, d = right aisle, e = right middle, f = right window
        self.column = ["a", "b", "c", "d", "e", "f"]

    def flightFull(self) -> Point:
        # display flight is full and wait
        self.flightFullText.draw(self.win)
        pt = self.win.getMouse()
        self.flightFullText.undraw()
        return pt

    def noBetterSeat(self) -> Point:
        # display no better seat and wait
        self.noBetterSeatText.draw(self.win)
        pt = self.win.getMouse()
        self.noBetterSeatText.undraw()
        return pt

    def createTicket(self, seats:list) -> (Point, list):
        pass
        # tickets = []
        # for i in len(seats):
        #     # find the row and column of the seat
        #     row = seat // 20
        #     column = seat % 6
        #     # create the ticket
        #     tickets.append(Text(Point(500, 100), f"Seat number {seat + 1}. Row {row}, seat {self.column[column - 1]}."))
        #     pt = self.win.getMouse()

    def assignSeat(self, seatType: str, currentSeat:list = None, size:int = None) -> (Point, list):
        if seatType == "business":
            # if a seat had already been assigned
            if currentSeat:
                # see if there's seats available
                if self.availableSeatsNum < size:
                    return self.noBetterSeat(), currentSeat
                # see if the seats are worse
                elif self.availableSeats[0] > 12:
                    return self.noBetterSeat(), currentSeat
                # if neither are true, assign the new seat and wait for click
                else:
                    # assign the next best seat available
                    seat = [self.availableSeats[0]]
                    # take the seat out of available seats
                    self.availableSeats.pop(0)
                    # readd the seat no longer wanted
                    self.availableSeats.append(currentSeat[0])
                    self.availableSeats.sort()
                    return self.createTicket(seat)
            # else if there's not enough room in the flight
            elif self.availableSeatsNum < size:
                return self.flightFull(), currentSeat
            # else assign a new seat
            else:
                # add how many groups are in the flight
                self.numGroups += 1
                # subtract the amount of seats available
                self.availableSeatsNum -= size
                # assign the first seat available
                seat = self.availableSeats[0]
                # take the seat out of available seats
                self.availableSeats.pop(0)
                # if the seat is in business class, satisfaction is 5
                if seat < 12:
                    self.customerSatisfactionIndex.append(5)
                # else seat isn't business class, satisfaction is -5
                else:
                    self.customerSatisfactionIndex.append(-5)
                # find the row and column of the seat
                row = seat // 20
                column = seat % 6
                # create the ticket
                ticket = Text(Point(500, 100), f"Seat number {seat + 1}. Row {row}, seat {self.column[column - 1]}.")
                ticket.draw(self.win)
                pt = self.win.getMouse()
                ticket.undraw()
                return pt, seat
        elif seatType == "tourist":
            # if a seat had already been assigned
            if currentSeat:
                # check if there is any better seat
                if len(self.availableSeats) < size:
                    return self.noBetterSeat(), currentSeat
                else:
                    # TODO draw ticket
                    pass
            # else if there's not enough room in the flight
            elif self.availableSeatsNum < size:
                return self.flightFull(), currentSeat
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
                    return self.noBetterSeat(), currentSeat
                else:
                    # TODO draw ticket
                    pass
            # else if there's not enough room in the flight
            elif self.availableSeatsNum < size:
                return self.flightFull(), currentSeat
            # else assign a new seat
            else:
                self.numGroups += 1
                self.availableSeats -= size
                # TODO draw ticket
