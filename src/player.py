# Write a class to hold player information, e.g. what room they are in
# currently.
import sys
class Player:
    def __init__(self, name, hp, mp, location):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.location = location
        self.input = None
    def __str__(self):
        return f"{self.name} reporting for duty!"
    
    def userInput(self):
        self.input = input().lower()
        if(self.input.lower() == "q"):
            print("You gave up!")
            return sys.exit()
        print(f"You inserted {self.input}")
    
    def move(self, dir):
        try:
            dirMap = {
                "north": "n_to",
                "south": "s_to",
                "east": "e_to",
                "west": "w_to"
                }
            newRoom = getattr(self.location, dirMap[dir.lower()])
            
            if(newRoom == None):
                print("You can't go that way. Try again!")
                self.userInput()
                return self.move(self.input)

            print(self.location.description)
            self.location = newRoom
            self.userInput()
            self.move(self.input)
        except KeyError as err:
            print(err)
            print("This location doesn't exists")
            self.userInput()
            self.move(self.input)

    





 

