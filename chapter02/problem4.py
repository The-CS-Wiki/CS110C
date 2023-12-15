#
#  Author: Benjamin Herrera
#
#  CS110C // Basics of Python
#  Chapter 2: Conditions
#  Practice 4, Try-Except 
#

# Answers
answers = {}

"""
PROBLEM:
    Wrap a try-except block around the necessary line of code.
    Additionally, try to make it so that the final conditions
    will return your answers as a "Correct!" string value.
"""

# EXAMPLE 1
# BEFORE: (Commented out for compiling purposes)
# a = [1, 2, 3, 4]
# b = 0
# for i in range(20):
#     b += a[i]
# if b == 100000:
#     example = "Correct!"
# else:
#     example = "Wrong!"

# AFTER:
a = [1, 2, 3, 4]
b = 0
try:
    for i in range(20):
        b += a[i]
except:
    b = 100000
if b == 100000:
    example = "Correct!"
else:
    example = "Wrong!"



# Answer 1
a = ["Tyler", ", ", "the", "Creator"]
b = ""
try:
    for i in range(20):
        b += a[i]
except:
    b = "Tyler, the Creator"
if b == "Tyler, the Creator":
    answers[0] = "Correct!"
else:
    answers[0] = "Wrong!"



# Answer 2
you = {
    "name": "John Doe",
    "age": 45,
    "height": 56
}
you["location"] = you["location"]
if you["location"] == "AZ":
    answers[1] = "Correct!"
else:
    answers[1] = "Wrong!"

"""

RUN PROCESS

<!> DO NOT EDIT BELOW THIS <!>

"""


# Main method to print the user's inputs
def main():
    for i in answers:
        print(answers[i])
