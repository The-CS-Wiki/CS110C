#
#  Author: Benjamin Herrera
#
#  CS110C // Basics of Python
#  Chapter 4: Functions and OOP
#  Practice 1, Functions
#

# Answers
answers = {}

"""
PROBLEM:
    Make functions based on the following descriptions
"""


# EXAMPLE 1
#   Make a function that subtracts a to b and returns its value
def foo(a, b):
    return a - b
example = foo(3, 2)


# Make a function called answer1 that calculates the value of a**b
# and adds c to it. Make sure to return this value
answers[1] = answer1(9, 3, 2)

# Make a function called answer2 that concatenates two strings together
answers[2] = answer2("Jake ", "Paul")

# Make a function called answer3 that turns a string into a float and
# then adds given value to it. Return the result
answers[3] = answer3("92.3", 7)

# Make a function that gets the second element in a list and power it
# by the value of the first element in the list. Return it as a string
answers[4] = answer4([4, 422, 23 2]) + "a"

"""

RUN PROCESS

<!> DO NOT EDIT BELOW THIS <!>

"""


# Main method to print the user's inputs
def main():
    for i in answers:
        print(answers[i])
