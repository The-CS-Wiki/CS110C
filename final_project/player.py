#
#  Author: Benjamin Herrera
#

# Import
import math


class Player:
    """Player class to represent players"""

    def __init__(self, name, spd, off, dfn, hnd, att):
        """Constructor for the Player class

        Args:
            name (str): Name of the player
            spd (float), [0, 1]: Determines the speed of the player
            off (float), [0, 1]: Determines the offensive skill of the player
            dfn (float), [0, 1]: Determines the defensiive skill of the player
            hnd (float), [0, 1]: Determines the handling of the player
            att (float), [0, 1]: Determines the attitude of the player
        """
        # TODO: Implement attributes

        # TODO: Calculate and save the apptitude for the instance

    """Create a method that calculates the aptitude of the player based on
    the equation provided to you in the README.md. The method should return the
    calculated aptitude.

    TIP: To represent log(x) in Python use `math.log(x)`
    TIP: To represent the minimum of two values (e.g. a, b), use `min(a, b)`
    TIP:    and this function call will return the minimum of a or b. This
    TIP:    applies to max as well.
    """
    # TODO: Create an instance method that can calculates and returns a 
    # TODO:     player's aptitude.

    def train(self):
        """Method to train the player. Remember that players improve their
        lowest attribute (except att) by 0.02 before a match starts.
        Additionally, training will increase their attitude by 0.005.

        TODO: Create a control flow to determine what attribute,
        other than att, to improve and increase attitude by 0.005. DO NOT
        FORGET to updated the player's aptitude
        """
        # TODO: Create a control flow to determine what attribute,
        # TODO:     other than att, to improve and increase attitude by 0.005.
        # TODO:     DO NOT FORGET to update the player's aptitude.

    def therapy(self):
        """Method to send a player to therapy. Note that therapy should not
        decrease their att to a negative value.
        """
        # TODO: Implement code to reduce a player's att through therapy.
        # TODO:     DO NOT FORGET to update the player's aptitude
