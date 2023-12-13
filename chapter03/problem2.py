#
#  Author: Benjamin Herrera
#
#  CS110C // Basics of Python
#  Chapter 1: Variables
#  Practice 2, Variable Values
#

# Answers
answers = {}

"""
PROBLEM:
    There are incomplete for loops that need if statements and 
    breaks. Apply these two appropriate to the problem question
"""

# EXAMPLE 1
#   Apply a break when b = 12
b = 0
c = 0
while True:
    if b == c:
        break
    b += c
    c += 1
example = b

# Break the loop when the length of res is 34
res = []
a = 0
while True:
    res.append(a)
    a += 1
answers[0] = res

# Stop when a False is encountered
res = []
temp = [True, True, True, True, True, True, True, False, True, True]
for i in temp:
    res.append(i)
answers[1] = res


"""

RUN PROCESS

<!> DO NOT EDIT BELOW THIS <!>

"""


# Main method to print the user's inputs
def main():
    for i in answers:
        print(answers[i])

main()