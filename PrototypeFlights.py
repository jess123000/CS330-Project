#!/usr/bin/env python3

# --------------------------------------------------
# Prototype of Flight.py
# This file is not intended to work as one might think
# This file was created simply to take photos of what we wanted the file product to look like
# Alex Harris and Dez Turkson
# March/April 2021
# --------------------------------------------------

from graphics import *

def openingView(win):

    # draw the welcome screen
    # create un-clickable customer button
    customerButton = Rectangle(Point(250, 200), Point(350, 250))
    customerButton.draw(win)
    customerText = Text(Point(300, 225), "Customer")
    customerText.draw(win)

    # create un-clickable manager button
    managerButton = Rectangle(Point(650, 200), Point(750, 250))
    managerButton.draw(win)
    managerText = Text(Point(700, 225), "Manager")
    managerText.draw(win)

    # window changes on mouse click
    win.getMouse()

    # reset the screen to default
    customerText.undraw()
    customerButton.undraw()
    managerText.undraw()
    managerButton.undraw()

def customerView(win):
    # create the un-clickable business button
    businessButton = Rectangle(Point(250, 200), Point(350, 250))
    businessButton.draw(win)
    businessText = Text(Point(300, 225), "Business")
    businessText.draw(win)

    # create the un-clickable tourist button
    touristButton = Rectangle(Point(450, 200), Point(550, 250))
    touristButton.draw(win)
    touristText = Text(Point(500, 225), "Tourist")
    touristText.draw(win)

    # create the un-clickable family button
    familyButton = Rectangle(Point(650, 200), Point(750, 250))
    familyButton.draw(win)
    familyText = Text(Point(700, 225), "Family")
    familyText.draw(win)

    # window changes on mouse click
    win.getMouse()

    # reset the screen to default
    businessText.undraw()
    businessButton.undraw()
    touristText.undraw()
    touristButton.undraw()
    familyText.undraw()
    familyButton.undraw()

def familyView(win):
    # create the un-clickable one button
    oneButton = Rectangle(Point(250, 200), Point(350, 250))
    oneButton.draw(win)
    oneText = Text(Point(300, 225), "One")
    oneText.draw(win)

    # create the un-clickable two button
    twoButton = Rectangle(Point(450, 200), Point(550, 250))
    twoButton.draw(win)
    twoText = Text(Point(500, 225), "Two")
    twoText.draw(win)

    # create the un-clickable three button
    threeButton = Rectangle(Point(650, 200), Point(750, 250))
    threeButton.draw(win)
    threeText = Text(Point(700, 225), "Three")
    threeText.draw(win)

    # window changes on mouse click
    win.getMouse()

    # reset the screen to default
    oneText.undraw()
    oneButton.undraw()
    twoText.undraw()
    twoButton.undraw()
    threeText.undraw()
    threeButton.undraw()

def sampleTicketGeneration(win):
    # create a business ticket example
    businessTicket = Text(Point(500, 200), "Your seat is: row 5, seat 6")
    businessTicket.draw(win)

    # window changes on mouse click
    win.getMouse()

    # reset the screen to default
    businessTicket.undraw()

    # create a tourist ticket example
    touristTicketOne = Text(Point(500, 200), "Your seat is: row 15, seat: 1")
    touristTicketTwo = Text(Point(500, 250), "Your seat is: row 15, seat: 2")
    touristTicketOne.draw(win)
    touristTicketTwo.draw(win)

    # window changes on mouse click
    win.getMouse()

    # reset the screen to default
    touristTicketOne.undraw()
    touristTicketTwo.undraw()

    # create a family ticket example
    familyTicketOne = Text(Point(500, 200), "Your seat is row 20, seat 3")
    familyTicketTwo = Text(Point(500, 250), "Your seat is row 20, seat 4")
    familyTicketThree = Text(Point(500, 300), "Your seat is row 20, seat 5")
    familyTicketFour = Text(Point(500, 350), "Your seat is row 20, seat 6")
    familyTicketOne.draw(win)
    familyTicketTwo.draw(win)
    familyTicketThree.draw(win)
    familyTicketFour.draw(win)

    # window changes on mouse click
    win.getMouse()

    #reset screen to default
    familyTicketOne.undraw()
    familyTicketTwo.undraw()
    familyTicketThree.undraw()
    familyTicketFour.undraw()

def managerView(win):
    # create sample satisfaction index result show
    satisfactionReport = Text(Point(500, 200), "Satisfaction Index Result: 100")
    satisfactionReport.draw(win)

    redoButton = Rectangle(Point(450, 400), Point(550, 450))
    redoButton.draw(win)
    redoText = Text(Point(500, 425), "Redo")
    redoText.draw(win)

    # window changes on mouse click
    win.getMouse()

    # reset screen to default
    satisfactionReport.undraw()
    redoText.undraw()
    redoButton.undraw()

def main():
    # create initial window
    win = GraphWin("demo", 1000, 600)

    # create un-clickable quit button
    quitButton = Rectangle(Point(450, 500), Point(550, 550))
    quitButton.draw(win)
    quitText = Text(Point(500, 525), "Quit")
    quitText.draw(win)

    openingView(win)
    customerView(win)
    familyView(win)
    sampleTicketGeneration(win)
    managerView(win)

if __name__ == '__main__':
    main()