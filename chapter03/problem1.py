#
#  Author: Benjamin Herrera
#
#  CS110C // Basics of Python
#  Chapter 3: Loops
#  Practice 1, For and While Loop Practice
#

# Answers
answers = {}

"""
PROBLEM:
    Use a for or while loop to solve the following problems
"""

# EXAMPLE 1
#   Set the value example with values from 0 to 30
a = []
for i in range(31):
    a.append(i)
example = a

# Answer 1
#   Set the value of answers[0] to a list of even numbers
#   from 0 to 20
answers[0] = a

# Answer 2
#   Set the value of answers[1] to get int values that have
#   the digit 3 at the end of the value from -200 to 329
#
#   HINT: to set values to positive numbers from negative
#         numbers, use abs(<Negative number>)
answers[1] =

# Answer 3
#   Create a 4 x 4 matrix. When the ith element of the vertical
#   side and the jth element of the horizontal are the same value,
#   that part of the matrix will be valued at 1. If not, it will be 0.
#   Set this matrix as the value of answers[2]
#
#   Example:
#       [[1, 0, 0, 0]
#        [0, 1, 0, 0]
#        [0, 0, 1, 0]
#        [0, 0, 0, 1]]
#
#   Hint: Nest loops into each other!
answers[2] =


"""

RUN PROCESS

<!> DO NOT EDIT BELOW THIS <!>

"""


# Main method to print the user's inputs
def main():
    for i in answers:
        print(answers[i])

