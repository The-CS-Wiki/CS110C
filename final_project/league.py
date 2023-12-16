class League:
    """Class that runs the league"""

    def __init__(self, name):
        """Constructor for the league instance

        Args:
            name (name): Name of the league
        """
        self.name = name
        self.teams = []

    def add_team(self, team):
        """Adds a team to the league

        Args:
            team (Team): team to add to the league
        """
        # If the number of players on the team is 10, add them
        if len(team.players) == 10:
            self.teams.append(team)

        # If not, do not add them
        else:
            print(
                f"{team.name} does not have 10 players and cannot be added.\n"
            )

    def start_season(self):
        """Method to calculate the outcomes of teams facing each other once.

        Returns:
            bool: False if there is an error, True if not
        """
        # Throw an error to the caller if there are less than 2 players
        if len(self.teams) < 2:
            print("Not enough teams to start the season.")
            return False

        # Throw an error to the caller if one of the teams doesn't have ten
        # characters
        for team in self.teams:
            if len(team.players) != 10:
                print(
                    f"{team.name} doesn't have 10 players. Season can't start."
                )
                return False

        # Print that the season is starting
        print("Season starting...\n")

        # TODO: Create a loop to play each team in a match. Use nested loops.

        # Return True if all is sucessful
        return True

    def play_match(self, team1, team2):
        """Simulate a match happening between two teams. First, the league
        sends the highest att player of both teams to therapy. Afterwards,
        each team trains their remaining players. Once that is done, simulate
        a match between the two teams. Return the team that has the highest
        aptitude after playing the match.

        Args:
            team1 (Team): Team 1 instance to compare to Team 2
            team2 (Team): Team 2 instance to compare to Team 1
        """
        # TODO: Send highest att player to therapy
        
        # TODO: Train players
        
        # TODO: Play the match
        
        # TODO: Return the winning team

    def send_highest_att_to_therapy(self, team):
        """Sends the highest att player to therapy based on the given team

        Args:
            team (Team): Team to figure out what player to send to therapy
        """
        highest_att_player = max(team.players, key=lambda player: player.att)
        team.send_player_to_therapy(highest_att_player.name)

    def determine_standings(self):
        """Sort the teams based on the criteria: points, wins, losses,
        red cards, team aptitude
        """
        self.teams.sort(
            key=lambda team: (
                -team.points,
                -team.wins,
                team.losses,
                team.red_cards,
                -team.calculate_team_aptitude(),
            )
        )

    def pretty_print_standings(self):
        """Pretty prints the standing of the league"""
        print(f"Standings in {self.name}:")
        for idx, team in enumerate(self.teams, start=1):
            print(
                f"{idx}. {team.name} - Points: {team.points}, "
                + f"Wins: {team.wins}, Losses: {team.losses}, "
                + f"Red Cards: {team.red_cards}, "
                + f"Team Aptitude: {team.calculate_team_aptitude():.2f}"
            )
        print()

    def conduct_tournament(self):
        """Conducts the tournament to see who is the winner of the current
        season
        """

        # If there are less than four teams, then no tournament takes place
        if len(self.teams) < 4:
            print("Not enough teams for the tournament.")
            return

        # Ensure the standings are up-to-date
        self.determine_standings()

        # TODO: Select the top four teams after sorting the list

        print("Tournament starting...\n")

        # TODO: Call the play_match() method to get the team who won
        # TODO:     their semi-finals

        # TODO: Call the play_match() method to get the team who won their
        # TODO:     finals

        # Print the champion for this season
        print(f"The champion of the {self.name} is {champion.name}!\n")
