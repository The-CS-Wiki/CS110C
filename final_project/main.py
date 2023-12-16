#
#  Author: Benjamin Herrera
#

# Imports
import random
from player import Player
from team import Team
from league import League


def create_random_player(name):
    """Function to create a random player

    Args:
        name (str): Name for the player

    Returns:
        Player: player instance that was randomly created
    """
    return Player(
        name=name,
        spd=random.uniform(0.5, 1),
        off=random.uniform(0.5, 1),
        dfn=random.uniform(0.5, 1),
        hnd=random.uniform(0.5, 1),
        att=random.uniform(0, 0.3),
    )


def create_random_team(name):
    """Function to create a random team

    Args:
        name (str): Name of the team to create

    Returns:
        Team: the team instance for the league
    """
    team = Team(name)
    for i in range(10):
        player_name = f"Player_{name}_{i+1}"
        team.add_player(create_random_player(player_name))
    return team


# Main execution
if __name__ == "__main__":
    # Create the league
    phoenix_league = League("Phoenix League")

    # Create and add 6 teams
    for i in range(6):
        team_name = f"Team_{i+1}"
        phoenix_league.add_team(create_random_team(team_name))
        
    # Print the league standings    
    phoenix_league.pretty_print_standings()

    # Start the season
    res = phoenix_league.start_season()
    if not res:
        exit()

    # Determine the standings
    phoenix_league.determine_standings()

    # Print the league standings
    phoenix_league.pretty_print_standings()

    # Conduct the final tournament
    phoenix_league.conduct_tournament()
