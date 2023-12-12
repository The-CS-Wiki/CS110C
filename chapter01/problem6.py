#
#  Author: Benjamin Herrera
#
#  CS110C // Basics of Python
#  Chapter 1: Variables
#  Practice 4, List and Dictionaries
#

# Answers
answers = {}

"""
PROBLEM:
    For the following problems, create lists and dictionaries based on
    the problem description
"""

# EXAMPLE 1
#   Create a list where the first element is "1234", and the second element is 2
example = ["1234", 2]

# Create a list where we have the following index descriptions:
#   0: "12342"
#   1: -23.42
#   2: 90
#   3: True
#   4: None
answers[0] = 

# Given the following list `a_list`, remove the first `pop` value
a_list = ["rock", "key", "pop", "2342"]
# Replace this comment with your solution
answers[1] = a_list

# Given the following list, append the value "joker" to it
b_list = [2, 234, 4.2, False]
# Replace this comment with your solution
answers[2] = b_list

# Given the following dictionary, remove the `icon` key
a_dict = {
    "lock": 922,
    "icon": str
}
# Replace this comment with your solution
answers[3] = a_dict

# Given the following dictionary, add a new key-value pair
#   where the key is "june" and the value is [1, -3, None]
b_dict = {
    "add": "a",
    "new": "key-pair"
}
# Replace this comment with your solution
answers[4] = b_dict

"""

RUN PROCESS

<!> DO NOT EDIT BELOW THIS <!>

"""


# Main method to print the user's inputs
def main():
    for i in answers:
        print(answers[i])
