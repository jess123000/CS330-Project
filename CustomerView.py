#!/usr/bin/env python3

# --------------------------------------------------
# CustomerView.py
# Alex Harris and Dez Turkson
# March/April 2021
# --------------------------------------------------

import sys
from graphics import *
from Plane import *

class CustomerView:

    def __init__(self, win: GraphWin, plane: Plane):
        # create all the buttons and text
        self.quitButton = Rectangle(Point(450, 500), Point(550, 550))
        self.quitText = Text(Point(500, 525), "Quit")
        self.logOffButton = Rectangle(Point(450, 390), Point(550, 440))
        self.logOffText = Text(Point(500, 415), "Log Off")
        self.customerViewText = Text(Point(500, 20), "Customer View")
        self.businessButton = Rectangle(Point(250, 200), Point(350, 250))
        self.businessText = Text(Point(300, 225), "Business")
        self.touristButton = Rectangle(Point(450, 200), Point(550, 250))
        self.touristText = Text(Point(500, 225), "Tourist")
        self.familyButton = Rectangle(Point(650, 200), Point(750, 250))
        self.familyText = Text(Point(700, 225), "Family")
        self.familyViewText = Text(Point(500, 20), "Family View")
        self.oneButton = Rectangle(Point(250, 200), Point(350, 250))
        self.oneText = Text(Point(300, 225), "One")
        self.twoButton = Rectangle(Point(450, 200), Point(550, 250))
        self.twoText = Text(Point(500, 225), "Two")
        self.threeButton = Rectangle(Point(650, 200), Point(750, 250))
        self.threeText = Text(Point(700, 225), "Three")
        self.redoButton = Rectangle(Point(250, 390), Point(350, 440))
        self.redoText = Text(Point(300, 415), "Redo")
        self.win = win
        self.plane = plane

    def drawAllNeed(self):
        # draw things all views need
        self.quitButton.draw(self.win)
        self.quitText.draw(self.win)
        self.logOffButton.draw(self.win)
        self.logOffText.draw(self.win)
        return

    def undrawAllNeed(self):
        # undraw things all view need
        self.quitButton.undraw()
        self.quitText.undraw()
        self.logOffButton.undraw()
        self.logOffText.undraw()
        return

    def drawStartCustomerView(self):
        # draw all the buttons and  text
        self.drawAllNeed()
        self.customerViewText.draw(self.win)
        self.businessButton.draw(self.win)
        self.businessText.draw(self.win)
        self.touristButton.draw(self.win)
        self.touristText.draw(self.win)
        self.familyButton.draw(self.win)
        self.familyText.draw(self.win)

        # wait for click and see what was clicked
        self.clickedStart(self.win.getMouse())
        return

    def undrawStartCustomerView(self) -> None:
        # undraw all the buttons and text
        self.customerViewText.undraw()
        self.businessButton.undraw()
        self.businessText.undraw()
        self.touristButton.undraw()
        self.touristText.undraw()
        self.familyButton.undraw()
        self.familyText.undraw()
        return

    def clickedStart(self, pt: Point):
        # check what button was clicked
        clicked = True
        while clicked:
            # if the exit button is clicked
            if (450 < pt.x < 550) and (500 < pt.y < 550):
                sys.exit()
            # if the log off button is clicked
            elif (450 < pt.x < 550) and (390 < pt.y < 440):
                self.undrawStartCustomerView()
                self.undrawAllNeed()
                return
            # if the business button is clicked
            elif (250 < pt.x < 350) and (200 < pt.y < 250):
                self.undrawStartCustomerView()
                self.drawSeatSelection()
                self.selectSeat("business", size = 1)
                return
            # if the tourist button is clicked
            elif (450 < pt.x < 550) and (200 < pt.y < 250):
                self.undrawStartCustomerView()
                self.drawSeatSelection()
                self.selectSeat("tourist", size = 2)
                return
            # if the family button is clicked
            elif (650 < pt.x < 750) and (200 < pt.y < 250):
                self.undrawStartCustomerView()
                self.drawFamilyView()
                return
            else:
                # no button was clicked, wait again
                pt = self.win.getMouse()
        return

    def drawFamilyView(self):
        # draw the family selection choices
        self.familyViewText.draw(self.win)
        self.oneButton.draw(self.win)
        self.oneText.draw(self.win)
        self.twoButton.draw(self.win)
        self.twoText.draw(self.win)
        self.threeButton.draw(self.win)
        self.threeText.draw(self.win)

        # wait for click and see what was clicked
        return self.clickedFamily(self.win.getMouse())

    def undrawFamilyView(self):
        # undraw family view
        self.familyViewText.undraw()
        self.oneButton.undraw()
        self.oneText.undraw()
        self.twoButton.undraw()
        self.twoText.undraw()
        self.threeButton.undraw()
        self.threeText.undraw()
        return

    def clickedFamily(self, pt: Point):
        # check what button was clicked
        clicked = True
        while clicked:
            # if exit button was clicked
            if (450 < pt.x < 550) and (500 < pt.y < 550):
                sys.exit()
            # if log off button was clicked
            elif (450 < pt.x < 550) and (390 < pt.y < 440):
                self.undrawFamilyView()
                self.undrawAllNeed()
                return
            # if one button was clicked
            elif (250 < pt.x < 350) and (200 < pt.y < 250):
                self.undrawFamilyView()
                self.drawSeatSelection()
                # family size is three
                self.selectSeat("family", size=3)
                return
            # if two button was clicked
            elif (450 < pt.x < 550) and (200 < pt.y < 250):
                self.undrawFamilyView()
                self.drawSeatSelection()
                # family size is 4
                self.selectSeat("family", size=4)
                return
            # if three button was clicked
            elif (650 < pt.x < 750) and (200 < pt.y < 250):
                self.undrawFamilyView()
                self.drawSeatSelection()
                # family size is 5
                self.selectSeat("family", size=5)
                return
            else:
                # no button was clicked, wait again
                pt = self.win.getMouse()
        return

    def drawSeatSelection(self):
        self.redoButton.draw(self.win)
        self.redoText.draw(self.win)
        return

    def undrawSeatSelection(self):
        self.redoButton.undraw()
        self.redoText.undraw()
        return

    def clickedSeatSelection(self, pt: Point, seatType: str, currentSeat:list = None, size:int = None):
        # check what button was clicked
        clicked = True
        while clicked:
            # if exit button was clicked
            if (450 < pt.x < 550) and (500 < pt.y < 550):
                sys.exit()
            # if log off button was clicked
            elif (450 < pt.x < 550) and (390 < pt.y < 440):
                self.undrawAllNeed()
                self.undrawSeatSelection()
                return
            # if redo button was selected redo the type of seat selection
            elif (250 < pt.x < 350) and (390 < pt.y < 440):
                self.selectSeat(seatType, currentSeat, size)
        return

    def selectSeat(self, seatType:str, currentSeat:list = None, size:int = None):
        # get seat and next click
        pt, seat = self.plane.assignSeat(seatType, currentSeat, size)
        self.clickedSeatSelection(pt, seatType, seat, size)
        return