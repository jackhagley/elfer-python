# LIBRARIES
import random
import numpy as np

# CONSTANTS
"""
The players have three letter names beginning with the first four letters of the alphabet
This makes it easier to keep track of them
"""
PLAYER_NAMES = [ "Ash", "Bev", "Col", "Dom" ]

"""
The suits are colours
R = Red
Y = Yellow
G = Green
B = Blue
The order is important.
If no player has R11 at the start of the game, it goes to the next colour in the list
"""
SUITS = ["R", "Y", "G", "B"]

"""
Debug prints out all the actions in the game to the console
"""
DEBUG = False

"""
When there are 4 players they each get 15 cards
"""
N_STARTING_HAND = 15
