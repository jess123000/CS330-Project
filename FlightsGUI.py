#!/usr/bin/env python3

# --------------------------------------------------
# FLightsGUI.py
# Alex Harris and Dez Turkson
# March/April 2021
# --------------------------------------------------

from ManagerView import *
from CustomerView import *
from OpeningView import *

def main():
    # create initial window
    win = GraphWin("FlightsGUI", 1000, 600)

    openingVIew = OpeningView(win)
    customerView = CustomerView(win)
    managerView = ManagerView(win)

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
