#
#  Author: Benjamin Herrera
#

# Imports
import random


class Team:
    """Team class to represent a team in the league"""

    """Create a construct for the Team class that keeps track of the teams:
    name, players, points, wins, losses, red_cards, and the current player in
    therapy. Name is the only argument for this constructor.
    """
    # TODO: Create a constructor for the Team class

    """Create a method that adds a player to the team. Remember, a team
    can have up to 10 players."""
    # TODO: Create a method to add up to 10 players

    """Create a method that calculates the team's aptitude by getting the
    average of every player's individual aptitude. If a team does not have 10
    people, return 0"""

    # TODO: Create a method that set the value of the team's aptitude

    def play_match(self, opponent):
        """Method to simulate a match between the current instance and the
        instance of the other team (via the opponent argument). Additionally,
        it also calculates the current instance and the opponent's number of
        red cards achieved for this match.

        Args:
            opponent (Team): Opponent team
        """
        # TODO: If this team's aptitude is greater, change the values of the
        # TODO:     team's points and wins, while also changing the oponent's
        # TODO:     points and wins.

    """Create a method that caculates the total number of red cards made from
    a match. This will be used inside the play_match() method.

    TIP: To get a random [0, 1] float value, use the `random.random()` value.
    TIP: Remember that a red card is handed if the random value is less than
    TIP:    the player's attitude.
    """
    # TODO: Create a method to calculate the team's red cards

    """Create a method that trains players to improve their worst attribute.
    
    TIP: Remember, we don't train the individual who is going to therapy. Use
    TIP:    that therapy player tracker wisely
    """
    # TODO: Create a method to train players

    """Create a method that sends a given player to therapy based on the name.
    
    TIP: When we send a player to therapy, we must track that the player is in
    TIP:    therapy
    """
    # TODO: Create a method to send a player into therapy
