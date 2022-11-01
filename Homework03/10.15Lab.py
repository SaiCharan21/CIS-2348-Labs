# Name: Sai Todupunoori
# PSID: 2048092

class Team:
    def __init__(self, team_name='none', team_wins=0, team_losses=0):
        self.team_name = team_name
        self.team_wins = team_wins
        self.team_losses = team_losses

    def get_win_percentage(self):
        percent = self.team_wins / (self.team_wins + self.team_losses)
        return percent

    def res(self):
        print('Congratulations, Team', self.team_name,
              'has a winning average!') if self.get_win_percentage() > 0.5 else print('Team', self.team_name,
                                                                                      'has a losing average.')


if __name__ == '__main__':
    name = input()
    wins = int(input())
    losses = int(input())

    t1 = Team(name, wins, losses)
    t1.res()
