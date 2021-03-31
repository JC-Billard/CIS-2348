# Jake Billard UHID 1582534

class Team:

    #Default Constructor with starter values.
    def __init__(self):
        self.team_name = "none"
        self.team_wins = 0
        self.team_losses = 0


    def set_team_name(self, team_name): #   connects team name to the default constructor
        self.team_name = team_name
    def set_team_wins(self, team_wins):   #   connects team wins to the default constructor
        self.team_wins = team_wins
    def set_team_losses(self, team_losses):   #   connects team losses to the default constructor
        self.team_losses = team_losses

    # TODO: Define get_win_percentage()
    ###   WIN PERCENTAGE   ###
    def get_win_percentage(self):
        win_percentage = self.team_wins / (self.team_wins + self.team_losses)
        return win_percentage
    ###   WIN PERCENTAGE   ###

if __name__ == "__main__":

    team = Team()

    ###   NAME, WINS, and LOSSES INPUT   ###
    team_name = input()
    team_wins = int(input())
    team_losses = int(input())
    ###   NAME, WINS, and LOSSES INPUT   ###

    # Connects each definition to the Team() class
    team.set_team_name(team_name)
    team.set_team_wins(team_wins)
    team.set_team_losses(team_losses)

    # If percentage is greater or equal to 0.5 then they are winning, if not, they are losing.
    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.team_name, 'has a winning average!')
    else:
        print('Team', team.team_name, 'has a losing average.')