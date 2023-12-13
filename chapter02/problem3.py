#
#  Author: Benjamin Herrera
#
#  CS110C // Basics of Python
#  Chapter 1: Variables
#  Practice 3, Variable Initialization
#

# Answers
answers = {}

"""
PROBLEM:
    Complete/Make if, elif, or else statements to get the
    correct output
"""

# EXAMPLE 1
#   Expected example value: "EXAMPLE TARGETED OUTPUT"
a = 98
b = 98
if a > b:
    example = "Not the right output"
elif a < b:
    example = "Still not the right output"
else:                                       # Lines 22-23 was added
    example = "EXAMPLE TARGETED OUTPUT"     #   to get the output

# Problem 1
#   Expected answers[0] value: "pwn.college{XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD}"
a = 3
if  # Complete this if statement
    answers[0] = "pwn.college{XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD}"

# Problem 2
#   Expected answers[1] value: "Accounts are the same"
bank_acc_1 = 22_000
bank_acc_2 = 22_000
if bank_acc_1 < bank_acc_2:
    answers[1] = "Account 1 is lower than 2"
elif bank_acc_1 > bank_acc_2:
    answers[1] = "Account 1 is greater than 2"
# Complete this condition at this line!
    answers[1] = "Accounts are the same"

# Problem 3
#   Expected answers[2] value: "Overweight"
bmi = 25.2
if bmi < 18.5:
    answers[2] = "Underweight"
elif bmi >= 18.5 and bmi < 25:
    answers[2] = "Normal"
elif    # This elif statement needs to be completed
    answers[2] = "Overweight"
elif bmi >= 30 and bmi < 35:
    answers[2] = "Obese"
else:
    answers[2] = "Extremely Obese"


"""

RUN PROCESS

<!> DO NOT EDIT BELOW THIS <!>

"""


# Main method to print the user's inputs
def main():
    print(answer_1, type(answer_1))
    print(test2, type(test2))
    print(poppy, type(poppy))
    print(lu_cky, type(lu_cky))
    print(kilo, type(kilo))
