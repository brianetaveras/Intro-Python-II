from room import Room
from player import Player
import textwrap
import os
import sys




# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# player = Player("Brian", 100, 100, "outside")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def clear():
    if(sys.platform == "win32"):
        os.system('cls')
    else:
        os.system('clear')

def handleInput():
    user_input = input('')
    if(user_input.lower() == "q"):
        clear()
        print("You gave up!")
        return sys.exit()
    return user_input


        

while True:
    try:
        clear()
        print("Hello Adventurer! Welcome to the Amazing world of Revium. What is your name? ")
        name = handleInput()
        player = Player(name, 100, 100, room["outside"])
        print(f"Excellent, {player.name}! Let's begin with the adventure." )
        print(f"Your current location is [{player.location.name}]")
        print(player.location.description)
        print(f"Where do you want to go? [North, South, East, West]")
        player.userInput()
        player.move(player.input)
        



        
        







    except ValueError as e:
        clear()
        print("Please insert the requested value")
        continue

