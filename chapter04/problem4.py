#
#  Author: Benjamin Herrera
#
#  CS110C // Basics of Python
#  Chapter 4: Functions and OOP
#  Practice 4, Inheritance and Import
#

# Answers
answers = {}

"""
PROBLEM:
    Import the the material.py module located in ./material/material.py to use
    the Material class. Use this class as a parent class to make a child class
    called Wood. In the Wood class, inherit all methods and variables from the
    Material class. For the constructor of the Wood class, take in another
    variable called type_of_wood that intakes the type of wood it is. The
    signature of the constructor (order of arguments) should be:
        __init__(self, cost, durability, material_uid, type_of_wood):
    Feel free to poke around the ./material/ directory to see the contents of
    the material.py module.

    NOTE:
        These are the datatypes for the Wood class' constructor's arguments:
            cost: float
            durability: int
            material_uid: str
            type_of_word: str
"""

# Place your answer here!


"""

RUN PROCESS

<!> DO NOT EDIT BELOW THIS <!>

"""


# Main method to print the user's inputs
def main():
    instance = Wood(234.22, 100, "WOOD_1232", "Mahogany")
    instance.info()
