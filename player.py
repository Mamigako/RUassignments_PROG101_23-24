class Player:

    def __init__(self, first_name="", last_name="", goals=0):
        self.first_name = first_name
        self.last_name = last_name
        self.goals = goals

    def add_goals(self, goals):
        self.goals += goals

    def __str__(self):
        return self.first_name + " " + self.last_name +", Goals: " + str(self.goals)

    