'''
This will be the main overall screen, but since i want the main menu to be within the board, this will work.
'''
import curses, sys
from utilities import variables as var

def board(stdscr):
    # I don't need an x or y position for the cursor here, as this is the everything static on the board
    k = 0 # K holds any input. 

    