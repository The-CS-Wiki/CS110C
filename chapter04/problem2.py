#
#  Author: Benjamin Herrera
#
#  CS110C // Basics of Python
#  Chapter 4: Functions and OOP
#  Practice 2, Instances
#

# Answers
answers = {}

"""
PROBLEM:
    Based on the given class make certain instances of it and pass it
    into the answers array
"""

"""Here's the Class to work with"""


class Player:
    def __init__(self, name, team, aptitude, reaction_time, sport):
        self.name = name
        self.team = team
        self.aptitude = aptitude
        self.reaction_time = reaction_time
        self.sport = sport

    def info(self):
        return (
            f"{self.name} {self.team} {self.aptitude} {self.reaction_time}"
            + f" {self.sport}"
        )


# Make a player instance with the following information
#   Name: Lionel Messi
#   Team: Inter Miami FC
#   Aptitude: 100
#   Reaction Time: 160
#   Sport: Football
example = Player("Lionel Messi", "Inter Miami FC", 100, 160, "Football")


# Make a player instance with the following information
#   Name: Lee Sang-hyeok
#   Team: T1
#   Aptitude: 100
#   Reaction Time: 170
#   Sport: League of Legends ESports
answers[0] = 

# Make a player instance with the following information
#   Name: Patrick Beverley
#   Team: 76ers
#   Aptitude: 200
#   Reaction Time: 360
#   Sport: Basketball
answers[1] = 

"""

RUN PROCESS

<!> DO NOT EDIT BELOW THIS <!>

"""


# Main method to print the user's inputs
def main():
    for i in answers:
        print(answers[i].info())