# CONSTANTS
"""
The players have three letter names beginning with the first four letters of the alphabet
This makes it easier to keep track of them
"""
player_names = [ "Ash", "Bev", "Col", "Dom" ]

"""
The suits are colours
R = Red
Y = Yellow
G = Green
B = Blue
The order is important.
If no player has R11 at the start of the game, it goes to the next colour in the list
"""
suits = ["R", "Y", "G", "B"]

"""
Debug prints out all the actions in the game to the console
"""
DEBUG = False

"""
When there are 4 players they each get 15 cards
"""
n_starting_hand = 15