#!/usr/bin/env python3

# --------------------------------------------------
# FLightsGUI.py
# Alex Harris and Dez Turkson
# March/April 2021
# --------------------------------------------------

from graphics import *

class Plane:

    def __init__(self, win: GraphWin):
        self.__availableSeats = []
        for i in range(120):
            self.__availableSeats.append(i)
        self.__availableSeatsNum = 120
        self.customerSatisfactionIndex = []
        self.numGroups = 0
        self.win = win
        self.__flightFullText = Text(Point(500, 100), "Flight full")
        self.__noBetterSeatText = Text(Point(500, 100), "No Better Seat Available")
        # a = left window, b = left middle, c = left aisle, d = right aisle, e = right middle, f = right window
        self.__column = ["a", "b", "c", "d", "e", "f"]
        self.__layout = []
        for i in range(6):
            self.__layout.append(Rectangle(Point(350 + 50 * i, 250), Point(400 + 50 * i, 300)))
            self.__layout.append(Text(Point(375 + 50 * i, 275), f"{self.__column[i]}"))

    def __flightFull(self) -> Point:
        # display flight is full and wait
        self.__flightFullText.draw(self.win)
        pt = self.win.getMouse()
        self.__flightFullText.undraw()
        return pt

    def __noBetterSeat(self) -> Point:
        # display no better seat and wait
        self.__noBetterSeatText.draw(self.win)
        pt = self.win.getMouse()
        self.__noBetterSeatText.undraw()
        return pt

    def __createTicket(self, seats:list) -> Point:

        tickets = []
        for i in range(len(self.__layout)):
            self.__layout[i].draw(self.win)
        for i in range(len(seats)):
            # find the row and __column of the seat
            row = seats[i] // 6 + 1
            __column = seats[i] % 6
            # create the ticket
            tickets.append(Text(Point(500, 100 + (i * 20)), f"Seat number {seats[i] + 1}. Row {row}, seat {self.__column[__column]}."))
            tickets[i].draw(self.win)
        drawn1 = Text(Point(500, 230), "Front of plane")
        drawn2 = Text(Point(500, 320), "Back of plane")
        drawn1.draw(self.win)
        drawn2.draw(self.win)
        pt = self.win.getMouse()
        for i in range(len(self.__layout)):
            self.__layout[i].undraw()
        for i in range(len(tickets)):
            tickets[i].undraw()
        drawn1.undraw()
        drawn2.undraw()
        return pt

    def __touristTicketSelection(self, seats: list,  i: int) -> (Point, list):
        if (self.__availableSeats[i] + 1) % 6 == 1:
            # if the adjacent seat is available
            if self.__availableSeats[i + 1] == self.__availableSeats[i] + 1:
                # if already have seats, remove them
                if len(seats) > 0:
                    seats.pop(0)
                    seats.pop(0)
                # add both seats
                seats.append(self.__availableSeats[i])
                seats.append(self.__availableSeats[i + 1])
                # remove seats from available seats
                self.__availableSeats.pop(i)
                # other seat was already removed so i will be the adjacent seat now
                self.__availableSeats.pop(i)
                # generate the ticket
                return self.__createTicket(seats), seats
        # else if there's a middle seat on the right side of the plane
        elif (self.__availableSeats[i] + 1) % 6 == 5:
            # if the adjacent window seat is available
            if self.__availableSeats[i + 1] == self.__availableSeats[i] + 1:
                # if seats already has seats picked, remove them
                if len(seats) > 0:
                    seats.pop(0)
                    seats.pop(0)
                # add both seats
                seats.append(self.__availableSeats[i])
                seats.append(self.__availableSeats[i + 1])
                # remove seats from available seats
                self.__availableSeats.pop(i)
                # other seat was already removed so i will be the adjacent seat now
                self.__availableSeats.pop(i)
                # generate the ticket
                return self.__createTicket(seats), seats
        return None, seats

    def __familyTicketSelection(self, seats: list, i: int, size: int) -> (Point, list):
        if (self.__availableSeats[i] + 1) % 6 == 3:
            seatsGiven = 1
            seatsToCheck = [1, 6, 7, -1, 2, 5, 8]
            j = 0
            seats.append(self.__availableSeats[i])
            currentSeatNumber = self.__availableSeats[i]
            self.__availableSeats.pop(i)
            while seatsGiven < size:
                if j == 7:
                    for k in range(len(seats)):
                        self.__availableSeats.append(seats[k])
                    self.__availableSeats.sort()
                    return None, []
                if currentSeatNumber + seatsToCheck[j] in self.__availableSeats:
                    seatsGiven += 1
                    index = self.__availableSeats.index(currentSeatNumber + seatsToCheck[j])
                    seats.append(self.__availableSeats[index])
                    self.__availableSeats.pop(index)
                j += 1
            return self.__createTicket(seats), seats
        return None, []

    def assignSeat(self, seatType: str, currentSeat:list = None, size:int = None) -> (Point, list):
        if self.__availableSeatsNum < size:
            return self.__flightFull(), currentSeat
        elif seatType == "business":
            if currentSeat:
                # if there aren't more seats in business class
                if self.__availableSeats[0] > 12:
                    return self.__noBetterSeat(), currentSeat
                else:
                    # assign the next best seat available
                    seat = [self.__availableSeats[0]]
                    # take the seat out of available seats
                    self.__availableSeats.pop(0)
                    # readd the seat no longer wanted
                    self.__availableSeats.append(currentSeat[0])
                    self.__availableSeats.sort()
                    return self.__createTicket(seat), seat
            # else assign a new seat
            else:
                # add how many groups are in the flight
                self.numGroups += 1
                # subtract the amount of seats available
                self.__availableSeatsNum -= size
                # assign the first seat available
                seat = [self.__availableSeats[0]]
                # take the seat out of available seats
                self.__availableSeats.pop(0)
                # if the seat is in business class, satisfaction is 5
                if seat[0] < 12:
                    self.customerSatisfactionIndex.append(5)
                # else seat isn't business class, satisfaction is -5
                else:
                    self.customerSatisfactionIndex.append(-5)
                # generate the ticket
                return self.__createTicket(seat), seat
        elif seatType == "tourist":
            if currentSeat:
                # check if there is any better seat
                seats = []
                for i in range(-1, -self.__availableSeatsNum - 1, -1):
                    pt, seats = self.__touristTicketSelection(seats, i)
                    if pt is not None:
                        for j in range(len(currentSeat)):
                            self.__availableSeats.append(currentSeat[j])
                        self.__availableSeats.sort()
                        return pt, seats
                if not seats:
                    return self.__noBetterSeat(), currentSeat
            # else assign a new seat
            else:
                # add how many groups are in the flight
                self.numGroups += 1
                # subtract the amount of seats available
                self.__availableSeatsNum -= size
                seats = []
                for i in range(-1, -self.__availableSeatsNum - 1, -1):
                    pt, seats = self.__touristTicketSelection(seats, i)
                    if pt is not None:
                        self.customerSatisfactionIndex.append(15)
                        return pt, seats
                # if the function hasn't return yet, there are no window seats with adjacent seat available
                # assign two random seats from the back to avoid business class if possible
                seats.append(self.__availableSeats[-1])
                seats.append(self.__availableSeats[-2])
                if self.__availableSeats[-1] - 1 == self.__availableSeats[-2]:
                    self.customerSatisfactionIndex.append(10)
                else:
                    self.customerSatisfactionIndex.append(-10)
                # remove those seats from availability
                self.__availableSeats.pop(-1)
                self.__availableSeats.pop(-1)
                return self.__createTicket(seats), seats
        elif seatType == "family":
            if currentSeat:
                # check if there is any better seat
                seats = []
                for i in range(-1, -self.__availableSeatsNum - 1, -1):
                    pt, seats = self.__familyTicketSelection(seats, i, size)
                    if pt is not None:
                        for j in range(len(currentSeat)):
                            self.__availableSeats.append(currentSeat[j])
                        self.__availableSeats.sort()
                        return pt, seats
                if not seats:
                    return self.__noBetterSeat(), currentSeat
            # else assign a new seat
            else:
                # add how many groups are in the flight
                self.numGroups += 1
                # subtract the amount of seats available
                self.__availableSeatsNum -= size
                seats = []
                for i in range(-1, -self.__availableSeatsNum - 1, -1):
                    pt, seats = self.__familyTicketSelection(seats, i, size)
                    if pt is not None:
                        self.customerSatisfactionIndex.append(15)
                        return pt, seats
                # if the function hasn't returned yet, there are not seats in the style wanted
                # assign random seats from the back
                for i in range(size):
                    seats.append(self.__availableSeats[-1])
                    self.__availableSeats.pop(-1)
                self.customerSatisfactionIndex.append(-10)
                return self.__createTicket(seats), seats