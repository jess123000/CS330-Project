#!/usr/bin/envp ython3

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

    # create the different objects for the GUI
    plane = Plane(win)
    openingVIew = OpeningView(win)
    customerView = CustomerView(win, plane)
    managerView = ManagerView(win, plane)

    clicked = True
    # not an infinite loop because of sys.exit calls within classes
    while clicked:
        selection = openingVIew.drawOpeningView()
        if selection == "customer":
            customerView.drawStartCustomerView()
        elif selection == "manager":
            managerView.drawManagerView()

    return

if __name__ == '__main__':
    main()
