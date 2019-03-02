from GuessTheNumber.game_status import GameStatus
# Multiplayer:
# -Each player will have a number to guess
# - All players will have the same amount of attempts
# - First player to guess wins

# game = GuessGame(number_to_guess, number_of_attempts)

class Multiplayer:
    def __init__(self, players):
        self.players = players

    def __repr__(self):
        return f"{self.players}"

    def rotate(self, players):









    # def __init__(self, players=None):
    #     if players is None:
    #         self.players = []
    #     else:
    #         self.players = players
    # def add_player(self, player):
    #     if player not in self.players:
    #         self.players.append(player)
    #
    # def remove_emp(self, player):
    #     if player in self.players:
    #         self.players.remove(player)
    #
    # def print_emps(self):
    #     for player in self.players:
    #         print("-->", player.player_name)

