""" Intro to Python III - Guided Project 

    This document contains examples for CS Intro to Python, module 3. Examples focus on object-orientated programming in Python. This paradigm allows us to abstract away implementation details and its modular nature allows us to easily debug, test, maintain, and reuse code.
"""

from item import Item

# How do we create a class with 2-3 attributes?

class Store:
    def __init__(self, name, categoires):
        self.name = name
        self.categoires = categoires

    # What function do we need to define to print out an instance of a class? 
    def __str__(self):
        store_string = self.name
        i = 1
        for cat in self.categoires:
            store_string += f"\n{i}. {cat.get_name()}"
            i+=1
        return store_string

    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
    
    def get_categories(self):
        return self.categoires
    
    def set_categories(self, new_categories):
        self.categoires = new_categories

# Let's create an instance of our Store and try printing it! 
my_store = Store("Josh's Bodega! ay Ay ay",
[Category("Produce", [Item("apples", 0.89), Item("lettuce", 1.45)]), 
Category("Dairy", [Item("yogurt", 0.56), Item("cheese", 5.46), Milk("milk", 4.35, "almond", "Jan 30")]), Category("Meat")])
print(my_store)

# If we want users to be able to interact with our classes, we need to give them a way to provide input via the terminal
selection = ""
while selection is not "q":
    selection = input(f"Please enter a number between 1 and " \
        f"{len(my_store.get_categories())} or 'q' to quit: ")
    print(f"{my_store.get_categories()[int(selection)-1]}")

class Category:
    def __init__(self, name, items=[]):
        self.name = name 
        self.items = items 
    
    def __str__(self):
        output = f"{self.name} contains items: "
        for i in self.items:
            output += f"\n\t{i}"

        return output
    
    def get_name(self):
        return self.name 
    
    def set_name(self, new_name):
        self.name = new_name

class Item:

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price}"

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price
    
# Milk IS AN Item (Inheritannce)
class Milk(Item):
    def __init__(self, name, price, milk_type, date):
        super().__init__(name, price)
        self.milk_type = milk_type
        self.date = date

    def __str__(self):
        return f"{super().__str__()} - type: {self.milk_type} expires on {self.date}"    


    # def __repr__(self):


# Let's create an instance of our Store and try printing it!
my_store = Store("Elissa's Groceries", [Category("Produce"), Category("Dairy"), Category("Meat")])
print(my_store)

# If we want users to be able to interact with our classes, we need to give them a way to provide input via the terminal 
selection = ""
while selection is not "q":
    selection = input(f"Please enter a number between 1 and " \
        f"{len(my_store.categoires)} or 'q' to quit: ")
    print(f"The user selected {selection}")

