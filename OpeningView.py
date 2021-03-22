#!/usr/bin/env python3

# --------------------------------------------------
# OpeningView.py
# Alex Harris and Dez Turkson
# March/April 2021
# --------------------------------------------------

import sys
from graphics import *

class OpeningView:

    def __init__(self, win: GraphWin):
        # create all the buttons and  text
        self.quitButton = Rectangle(Point(450, 500), Point(550, 550))
        self.quitText = Text(Point(500, 525), "Quit")
        self.customerButton = Rectangle(Point(250, 200), Point(350, 250))
        self.customerText = Text(Point(300, 225), "Customer")
        self.managerButton = Rectangle(Point(650, 200), Point(750, 250))
        self.managerText = Text(Point(700, 225), "Manager")
        self.win = win

    def drawOpeningView(self) -> str:
        # draw all the buttons and  text
        self.quitButton.draw(self.win)
        self.quitText.draw(self.win)
        self.customerButton.draw(self.win)
        self.customerText.draw(self.win)
        self.managerButton.draw(self.win)
        self.managerText.draw(self.win)

        # wait for click and see what was clicked
        return self.clicked(self.win.getMouse())

    def undrawOpeningView(self) -> None:
        # undraw all the buttons and text
        self.quitButton.undraw()
        self.quitText.undraw()
        self.customerButton.undraw()
        self.customerText.undraw()
        self.managerButton.undraw()
        self.managerText.undraw()
        return

    def clicked(self, pt: Point) -> str:
        # check what button was clicked
        clicked = True
        while clicked:
            # if the exit button is clicked
            if (450 < pt.x < 550) and (500 < pt.y < 550):
                sys.exit()
            # if the customer button is clicked
            elif (250 < pt.x < 350) and (200 < pt.y < 250):
                self.undrawOpeningView()
                return "customer"
            # if the manager button is clicked
            elif (650 < pt.x < 750) and (200 < pt.y < 250):
                self.undrawOpeningView()
                return "manager"
            else:
                # no button was clicked, wait again
                pt = self.win.getMouse()