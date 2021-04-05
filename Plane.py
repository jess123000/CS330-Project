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

    def createTicket(self, seats:list) -> Point:
        pass
        tickets = []
        for i in range(len(seats)):
            # find the row and column of the seat
            row = seats[i] // 20
            column = seats[i] % 6
            # create the ticket
            tickets.append(Text(Point(500, 100 + (i * 10)), f"Seat number {seats[i] + 1}. Row {row}, seat {self.column[column - 1]}."))
            tickets[i].draw(self.win)
        pt = self.win.getMouse()
        for i in range(len(tickets)):
            tickets[i].undraw()
        return pt

    def touristTicketSelection(self, seats: list,  i: int) -> (Point, list):
        if (self.availableSeats[i] + 1) % 6 == 1:
            # if the adjacent seat is available
            if self.availableSeats[i + 1] == self.availableSeats[i] + 1:
                # add both seats
                seats.append(self.availableSeats[i])
                seats.append(self.availableSeats[i + 1])
                # remove seats from available seats
                self.availableSeats.pop(i)
                # other seat was already removed so i will be the adjacent seat now
                self.availableSeats.pop(i)
                # generate the ticket
                return self.createTicket(seats), seats
        # else if there's a middle seat on the right side of the plane
        elif (self.availableSeats[i] + 1) % 6 == 5:
            # if the adjacent window seat is available
            if self.availableSeats[i + 1] == self.availableSeats[i] + 1:
                # add both seats
                seats.append(self.availableSeats[i])
                seats.append(self.availableSeats[i + 1])
                # remove seats from available seats
                self.availableSeats.pop(i)
                # other seat was already removed so i will be the adjacent seat now
                self.availableSeats.pop(i)
                # generate the ticket
                return self.createTicket(seats), seats
        else:
            return None, seats

    def assignSeat(self, seatType: str, currentSeat:list = None, size:int = None) -> (Point, list):
        if self.availableSeatsNum < size:
            return self.flightFull(), currentSeat
        elif seatType == "business":
            if currentSeat:
                # if there aren't more seats in business class
                if self.availableSeats[0] > 12:
                    return self.noBetterSeat(), currentSeat
                else:
                    # assign the next best seat available
                    seat = [self.availableSeats[0]]
                    # take the seat out of available seats
                    self.availableSeats.pop(0)
                    # readd the seat no longer wanted
                    self.availableSeats.append(currentSeat[0])
                    self.availableSeats.sort()
                    return self.createTicket(seat), seat
            # else assign a new seat
            else:
                # add how many groups are in the flight
                self.numGroups += 1
                # subtract the amount of seats available
                self.availableSeatsNum -= size
                # assign the first seat available
                seat = [self.availableSeats[0]]
                # take the seat out of available seats
                self.availableSeats.pop(0)
                # if the seat is in business class, satisfaction is 5
                if seat < 12:
                    self.customerSatisfactionIndex.append(5)
                # else seat isn't business class, satisfaction is -5
                else:
                    self.customerSatisfactionIndex.append(-5)
                # generate the ticket
                self.createTicket(seat)
                pt = self.win.getMouse()
                return pt, seat
        elif seatType == "tourist":
            if currentSeat:
                # check if there is any better seat
                seats = []
                for i in range(len(self.availableSeats)):
                    # if the seat is a business class seat
                    if self.availableSeats[i] < 12:
                        pass
                    else:
                        pt, seats = self.touristTicketSelection(seats, i)
                        # if a seat was found, return
                        if pt is not None:
                            for j in range(len(currentSeat)):
                                self.availableSeats.append(currentSeat[j])
                            self.availableSeats.sort()
                            return pt, seats
                if not seats:
                    return self.noBetterSeat(), currentSeat
            # else assign a new seat
            else:
                # add how many groups are in the flight
                self.numGroups += 1
                # subtract the amount of seats available
                self.availableSeats -= size
                seats = []
                for i in range(len(self.availableSeats)):
                    # if the seat is business class, don't use it yet
                    if self.availableSeats[i] < 12:
                        pass
                    else:
                        pt, seats = self.touristTicketSelection(seats, i)
                        # if a seat was found, return
                        if pt is not None:
                            return pt, seats
                # if no seat was found through previous loop
                if not seats:
                    i = 0
                    # allow for business seats to be given
                    while self.availableSeats[i] < 12:
                        pt, seats = self.touristTicketSelection(seats, i)
                        # if a seat was found, return
                        if pt is not None:
                            return pt, seats
                        i += 1
                    # if the function hasn't return yet, there are no window seats with adjacent seat available
                    # assign two random seats from the back to avoid business class if possible
                    seats.append(self.availableSeats[-1])
                    seats.append(self.availableSeats[-2])
                    # remove those seats from availability
                    self.availableSeats.pop(-1)
                    self.availableSeats.pop(-1)
                    return self.createTicket(seats), seats

        elif seatType == "family":
            if currentSeat:
                # check if there is any better seat
                # TODO draw ticket
                pass
            # else assign a new seat
            else:
                # add how many groups are in the flight
                self.numGroups += 1
                # subtract the amount of seats available
                self.availableSeats -= size
                # TODO draw ticket
