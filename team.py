class Team:

    def __init__(self, team_name="", players=None):
        self.team_name = team_name
        self.players = set() if players is None else players

    def add_player(self, player):
        self.players.add(player)

    def most_goals_player(self):

        stringz = sorted(self.players, key=lambda p: p.goals, reverse=True)[0] 
        #f"{self.team_name}:\n"

        #for player in sorted(self.players, key=lambda p: p.goals, reverse=True):
        #    stringz += f"\t{player.first_name} {player.last_name}, Goals: {player.goals}\n"

        return stringz
           
    def __add__(self, other_team):
        # Combine team names
        combined_team_name = f"{self.team_name}+{other_team.team_name}"

        # Create a new list with unique players from both teams
        combined_players = self.players.union(other_team.players)

        # Create a new Team object with the combined data
        combined_team = Team(combined_team_name, combined_players)

        return combined_team

    def __str__(self):
        stringz = ""
        stringz = f"{self.team_name}:\n"
        for player in sorted(self.players, key=lambda p: p.goals, reverse=True):
            stringz += f"\t{player.first_name} {player.last_name}, Goals: {player.goals}\n"    

        return stringz

        