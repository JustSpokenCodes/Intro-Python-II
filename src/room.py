# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        room_string = self.name
        i = 1 
        for dog in self.description:
            room_string = f"\n{i}. {dog.get_name()}"
            i+=1
        return room_string
    
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
    
    def get_description(self):
        return self.description
    
    def set_description(self, new_description):
        return self.new_description

class Inventory: 
    def __init__(self,name,get_items,add_item,remove_item)
        self.name = name
        self.get_items = get_items
        self.add_item = add_item
        self.remove_item = remove_item
    
    def __str__(self):
        output = f"{self.name} contains this many tings: "
        for i in self.items: 
            output += f"\n\t{i}"
        return output
    
    def get_name(self):
        return self.name 
    
    def set_name(self, new_name):
        return self.new_name
    
    def get_items():
        return self.get_items
    
    def add_item(item):
        return self.add_item(item)
    
    def remove_item(item):
        return self.remove_item(item)

class Item: 
    def __init__(self,name,effectiveness)
        self.name = name 
        self.effectiveness = effectiveness
    
    def __str__(self):
        output = f"{self.name} has this much effect: {self.effectiveness}"
        for i in self.effectiveness:
            output += f"\n\t{i}"
        return output
    
    def get_name(self):
        return self.name 
    
    def set_name(self, new_name):
        return self.new_name
    
    def get_effectiveness(self):
        return self.effectiveness
    
    def set_effectiveness(self, new_effectiveness):
        self.effectiveness = new_effectiveness
    
