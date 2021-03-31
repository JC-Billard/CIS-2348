#Jake Billard UHID 1582534

class Team:
    def __init__(self):
        self.team_name = "none"
        self.team_wins = 0
        self.team_losses = 0


        # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        return (self.team_wins / (self.team_wins + self.team_losses))

if __name__ == "__main__":
    the_team = Team()
    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    # Connecting Team Class to Variables.
    Team.team_name = team_name
    Team.team_wins = team_wins
    Team.team_losses = team_losses
    Team().get_win_percentage()


 #0.5 is the threshold. Raven's winning average is 0.8 and Angel's losing average is 0.4.
    if Team.get_win_percentage() >= 0.5:
        print("Congratulations, Team ", team_name, " has a winning average!")
    else:
        print("Team ", team_name, " has a losing average" )

