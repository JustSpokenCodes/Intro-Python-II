""" Intro to Python III - Guided Project 

    This document contains examples for CS Intro to Python, module 3. Examples focus on object-orientated programming in Python. This paradigm allows us to abstract away implementation details and its modular nature allows us to easily debug, test, maintain, and reuse code.
"""

from category import Category 

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
            store_string += f"\n{i}. {cat}"
            i+=1

        return store_string

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

