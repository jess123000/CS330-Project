#!/usr/bin/env python3

# --------------------------------------------------
# CustomerView.py
# Alex Harris and Dez Turkson
# March/April 2021
# --------------------------------------------------

import sys
from Plane import *

class CustomerView:

    def __init__(self, win: GraphWin, plane: Plane):
        # create all the buttons and text
        self.__quitButton = Rectangle(Point(450, 500), Point(550, 550))
        self.__quitText = Text(Point(500, 525), "Quit")
        self.__logOffButton = Rectangle(Point(450, 390), Point(550, 440))
        self.__logOffText = Text(Point(500, 415), "Log Off")
        self.__customerViewText = Text(Point(500, 20), "Customer View")
        self.__businessButton = Rectangle(Point(250, 200), Point(350, 250))
        self.__businessText = Text(Point(300, 225), "Business")
        self.__touristButton = Rectangle(Point(450, 200), Point(550, 250))
        self.__touristText = Text(Point(500, 225), "Tourist")
        self.__familyButton = Rectangle(Point(650, 200), Point(750, 250))
        self.__familyText = Text(Point(700, 225), "Family")
        self.__familyViewText = Text(Point(500, 20), "How many children do you have?")
        self.__oneButton = Rectangle(Point(250, 200), Point(350, 250))
        self.__oneText = Text(Point(300, 225), "One")
        self.__twoButton = Rectangle(Point(450, 200), Point(550, 250))
        self.__twoText = Text(Point(500, 225), "Two")
        self.__threeButton = Rectangle(Point(650, 200), Point(750, 250))
        self.__threeText = Text(Point(700, 225), "Three")
        self.__redoButton = Rectangle(Point(250, 390), Point(350, 440))
        self.__redoText = Text(Point(300, 415), "Redo")
        self.win = win
        self.plane = plane

    def drawAllNeed(self) -> None:
        # draw things all views need
        self.__quitButton.draw(self.win)
        self.__quitText.draw(self.win)
        self.__logOffButton.draw(self.win)
        self.__logOffText.draw(self.win)
        return

    def undrawAllNeed(self) -> None:
        # undraw things all view need
        self.__quitButton.undraw()
        self.__quitText.undraw()
        self.__logOffButton.undraw()
        self.__logOffText.undraw()
        return

    def drawStartCustomerView(self) -> None:
        # draw all the buttons and  text
        self.drawAllNeed()
        self.__customerViewText.draw(self.win)
        self.__businessButton.draw(self.win)
        self.__businessText.draw(self.win)
        self.__touristButton.draw(self.win)
        self.__touristText.draw(self.win)
        self.__familyButton.draw(self.win)
        self.__familyText.draw(self.win)

        # wait for click and see what was clicked
        self.clickedStart(self.win.getMouse())
        return

    def undrawStartCustomerView(self) -> None:
        # undraw all the buttons and text
        self.__customerViewText.undraw()
        self.__businessButton.undraw()
        self.__businessText.undraw()
        self.__touristButton.undraw()
        self.__touristText.undraw()
        self.__familyButton.undraw()
        self.__familyText.undraw()
        return

    def clickedStart(self, pt: Point) -> None:
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

    def drawFamilyView(self) -> None:
        # draw the family selection choices
        self.__familyViewText.draw(self.win)
        self.__oneButton.draw(self.win)
        self.__oneText.draw(self.win)
        self.__twoButton.draw(self.win)
        self.__twoText.draw(self.win)
        self.__threeButton.draw(self.win)
        self.__threeText.draw(self.win)

        # wait for click and see what was clicked
        return self.clickedFamily(self.win.getMouse())

    def undrawFamilyView(self) -> None:
        # undraw family view
        self.__familyViewText.undraw()
        self.__oneButton.undraw()
        self.__oneText.undraw()
        self.__twoButton.undraw()
        self.__twoText.undraw()
        self.__threeButton.undraw()
        self.__threeText.undraw()
        return

    def clickedFamily(self, pt: Point) -> None:
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

    def drawSeatSelection(self) -> None:
        self.__redoButton.draw(self.win)
        self.__redoText.draw(self.win)
        return

    def undrawSeatSelection(self) -> None:
        self.__redoButton.undraw()
        self.__redoText.undraw()
        return

    def clickedSeatSelection(self, pt: Point, seatType: str, currentSeat:list = None, size:int = None) -> None:
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
            else:
                # no button was clicked, wait again
                pt = self.win.getMouse()
        return

    def selectSeat(self, seatType:str, currentSeat:list = None, size:int = None) -> None:
        # get seat and next click
        pt, seat = self.plane.assignSeat(seatType, currentSeat, size)
        self.clickedSeatSelection(pt, seatType, seat, size)
        return