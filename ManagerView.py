#!/usr/bin/env python3

# --------------------------------------------------
# ManagerView.py
# Alex Harris and Dez Turkson
# March/April 2021
# --------------------------------------------------

import sys
from graphics import *

class ManagerView:

    def __init__(self, win: GraphWin):
        # create all the buttons and text
        self.quitButton = Rectangle(Point(450, 500), Point(550, 550))
        self.quitText = Text(Point(500, 525), "Quit")
        self.logOffButton = Rectangle(Point(350, 390), Point(450, 440))
        self.logOffText = Text(Point(400, 415), "Log Off")
        self.redoButton = Rectangle(Point(550, 390), Point(650, 440))
        self.redoText = Text(Point(600, 415), "Redo")
        self.managerViewText = Text(Point(500, 20), "Manager View")
        self.win = win

    def drawManagerView(self):
        # draw all buttons and text
        self.quitButton.draw(self.win)
        self.quitText.draw(self.win)
        self.logOffButton.draw(self.win)
        self.logOffText.draw(self.win)
        self.redoButton.draw(self.win)
        self.redoText.draw(self.win)
        self.managerViewText.draw(self.win)
        self.calculateSatisfactionIndex()
        return


    def undrawManagerView(self):
        # undraw all buttons and text
        self.quitButton.undraw()
        self.quitText.undraw()
        self.logOffButton.undraw()
        self.logOffText.undraw()
        self.redoButton.undraw()
        self.redoText.undraw()
        self.managerViewText.undraw()
        return

    def calculateSatisfactionIndex(self):
        # calculate satisfaction index here

        # wait for button to be pressed
        self.clicked(self.win.getMouse())
        return

    def clicked(self, pt: Point):
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
                self.calculateSatisfactionIndex()
                return
            else:
                # no button was clicked, wait again
                pt = self.win.getMouse()
        return