from Guess_The_Number.play import Play
from Guess_The_Number.play import Game

class Player(Play):
    def __init__(self, player_name, number introduced):
        super().__init__()
        self.player_name = player_name
        self.opportunities=6
        self.number_introduced = number_introduced

player1 = Player("player_1")
player1.game()