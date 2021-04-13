#!/usr/bin/env python3

# --------------------------------------------------
# ManagerView.py
# Alex Harris and Dez Turkson
# March/April 2021
# --------------------------------------------------

import sys
from Plane import *
import random


class ManagerView:

    def __init__(self, win: GraphWin, plane: Plane):
        # create all the buttons and text
        self.__quitButton = Rectangle(Point(450, 500), Point(550, 550))
        self.__quitText = Text(Point(500, 525), "Quit")
        self.__logOffButton = Rectangle(Point(350, 390), Point(450, 440))
        self.__logOffText = Text(Point(400, 415), "Log Off")
        self.__redoButton = Rectangle(Point(550, 390), Point(650, 440))
        self.__redoText = Text(Point(600, 415), "Redo")
        self.__managerViewText = Text(Point(500, 20), "Manager View")
        self.win = win
        self.plane = plane

    def drawManagerView(self) -> None:
        # draw all buttons and text
        self.__quitButton.draw(self.win)
        self.__quitText.draw(self.win)
        self.__logOffButton.draw(self.win)
        self.__logOffText.draw(self.win)
        self.__redoButton.draw(self.win)
        self.__redoText.draw(self.win)
        self.__managerViewText.draw(self.win)
        self.__calculateSatisfactionIndex()
        return


    def undrawManagerView(self) -> None:
        # undraw all buttons and text
        self.__quitButton.undraw()
        self.__quitText.undraw()
        self.__logOffButton.undraw()
        self.__logOffText.undraw()
        self.__redoButton.undraw()
        self.__redoText.undraw()
        self.__managerViewText.undraw()
        return

    def __calculateSatisfactionIndex(self) -> None:
        # calculate satisfaction index here
        if self.plane.numGroups < 10:
            drawn = Text(Point(500, 100), "Not enough groups for satisfaction results")
        else:
            tenRandom = random.choices(self.plane.customerSatisfactionIndex, k=10)
            index = 0
            for i in tenRandom:
                index += i
            index /= 10
            drawn = Text(Point(500, 100), f"Customer Satisfaction Index: {index}")
        flightSize = Text(Point(500, 120), f"Number of groups: {self.plane.numGroups}")
        drawn.draw(self.win)
        flightSize.draw(self.win)
        # wait for button to be pressed and undraw
        pt = self.win.getMouse()
        flightSize.undraw()
        drawn.undraw()
        self.clicked(pt)
        return

    def clicked(self, pt: Point) -> None:
        # check what button was clicked
        clicked = True
        while clicked:
            # if the exit button is clicked
            if (450 < pt.x < 550) and (500 < pt.y < 550):
                sys.exit()
            # if the log off button was clicked
            elif (350 < pt.x < 450) and (390 < pt.y < 440):
                 self.undrawManagerView()
                 return
            # if redo button was clicked
            elif (550 < pt.x < 650) and (390 < pt.y < 440):
                self.__calculateSatisfactionIndex()
                return
            else:
                # no button was clicked, wait again
                pt = self.win.getMouse()
        return