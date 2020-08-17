# Write a class to hold player information, e.g. what room they are in
# currently.
import sys
class Player:
    def __init__(self, name, hp, mp, location, bag = {}):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.location = location
        self.input = None
        self.bag = bag
    def __str__(self):
        return f"{self.name} reporting for duty!"
    
    def userInput(self):
                
        print("What do you want to do? Type 'help' to get the options")
        self.input = input("").lower()
        command = self.input.split(' ')[0]
        if(len(self.input.split(' ')) > 1):
            action = self.input.split(' ')[1]

        if(self.input == "q"):
            print("You gave up!")
            return sys.exit()
        if(command == "go"):
            self.move(action)
            self.userInput()        
        elif(command == "inspect"):
            self.location.inspect()
            self.userInput()        
        elif(command == "help"):
            print("You can interact with the world using the following commands:")
            print("go [direction]")
            print("inspect")
            self.userInput()
        elif(command == "grab"):
            grabbed_item = self.location.grabItem(action)
            if(grabbed_item == None):
                print("This room doesn't have the item you are looking for.")
            else:
                self.bag.update({action: grabbed_item})
                print(f"{action.capitalize()} has been added to your bag")
            self.userInput()
        elif(command == "drop"):
            if (action in self.bag):
                self.location.dropItem({action: self.bag[action]})
                self.bag.pop(action)
                print(f"{action.capitalize()} dropped")
            else:
                print(f"You don't have {action.capitalize} in your bag")
            self.userInput()
        elif(command == "mybag"):
            [print(f"{k}: {v}") for k, v in enumerate(self.bag)]
            self.userInput()
            
    
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
        except KeyError as err:
            print(err)
            print("This location doesn't exists")
            self.userInput()
            self.move(self.input)

    
    

    





 

