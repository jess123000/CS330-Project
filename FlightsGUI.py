#!/usr/bin/env python3

# --------------------------------------------------
# FLightsGUI.py
# Alex Harris and Dez Turkson
# March/April 2021
# --------------------------------------------------

from ManagerView import *
from CustomerView import *
from OpeningView import *
from Plane import *

def main():
    # create initial window
    win = GraphWin("FlightsGUI", 1000, 600)

    plane = Plane()
    openingVIew = OpeningView(win)
    customerView = CustomerView(win, plane)
    managerView = ManagerView(win, plane)

    clicked = True
    while clicked:
        selection = openingVIew.drawOpeningView()
        if selection == "customer":
            customerView.drawStartCustomerView()
        elif selection == "manager":
            managerView.drawManagerView()

    return

if __name__ == '__main__':
    main()
