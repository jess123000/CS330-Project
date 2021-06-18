# CS330 SP21 Project

## To run start this program, run the FlightsGUI.py file

This is a software system to make seat
arrangement for a small airline which operates between two cities: X and Y. 
The flight has 20 rows of six seats, arranged 3-3. The first 2 rows are business select.
Passengers come in one of three categories: business travelers, tourists and families.

(a) Business travelers are always alone. They can request business select seats or normal seats.

(b) Tourists are always in pairs. They always want one window seat, with, of course, the other person having the adjacent seat (sharing a window).

(c) Families consist of 2 adults + a number of children from 1 to 3. The must be seated together if possible. They want as many aisle seats as possible. 

Seat allocation is first-come, first-served. The check-in agents try to accommodate each preference, but of
course as the flight becomes full, people must take what they get. Getting their preference gives each group
a satisfaction level:

(a) -10 if groups are broken up.

(b) -5 if business select is ignored.

(c) 0 if seating preference is ignored but business select preference is granted.

(d) +5 for each window or aisle seat preference granted.

(e) +10 for keeping a group together.

The system should accommodate passengers' request for a change of their seating arrangement.

An airliner ticket should be generated for each passenger. At the end of the flight, 10 groups are randomly
chosen and polled for their cumulative satisfaction index. The system should allow the manager of the airliner
to generate a report which includes number of passengers and their cumulative satisfaction index for each flight.
