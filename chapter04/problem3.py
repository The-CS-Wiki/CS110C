#
#  Author: Benjamin Herrera
#
#  CS110C // Basics of Python
#  Chapter 4: Functions and OOP
#  Practice 3, Classes
#

# Answers
answers = {}

"""
PROBLEM:
    Create classes and its methods based on the following question
"""

# Create a House class that has the following attributes:
#   - Address
#   - Price
#   - Number of Bedrooms
#   - Number of Bathrooms
# Additionally, create a method called info that formats the info of the house into
# the following format:
#   "<Address>, <Price>, Number of Bedrooms: <Num of Bedrooms>, Number of Bathrooms: <Num of Bathrooms>"
class House():
    def __init__(self, address, price, num_bed, num_bath):
        self.address = address
        self.price = price
        self.num_bed = num_bed
        self.num_bath = num_bath
    def info(self):
        print(self.address + ", " + self.price + ", Number of Bedrooms: " + self.num_bed + ", Number of Bathrooms: " + self.num_bath)


# Create a Phone class that has the following attributes:
#   - Model
#   - Brand
#   - Price (Formatted as a str, e.g. "$XXX.XX")
# Additionally, create a method called details that formats the info of the phone into
# the following format:
#   "<Model>\nMade by <Brand>\nPrice: <Price>"
# Additionally, create a method called get_price that just returns the price of the phone


"""

RUN PROCESS

<!> DO NOT EDIT BELOW THIS <!>

"""


# Main method to print the user's inputs
def main():
    instance = Phone("iPhone 15 Pro Max, 256 GB", "Apple", "$1000")
    instance.details()
    print(instance.get_price())