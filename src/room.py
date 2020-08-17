# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = {}):
        self.name = name
        self.description = description
        # self.x_size = x_size
        # self.y_size = y_size
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items
    def inspect(self):
        if(len(self.items)):
            [print(item) for item in self.items]
            return
        print("No items in this room")
    def grabItem(self, item):
        if(item in self.items):
            return self.items.pop(item)
        return None
    def dropItem(self, item):
        self.items.update(item)

        



