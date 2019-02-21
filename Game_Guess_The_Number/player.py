from Game_Guess_The_Number.play import Play

class Player(Play):
    def __init__(self, player_name):
        super().__init__()
        self.player_name = player_name
        self.opportunities=6
        self.score=0

player1 = Player("player_1")
player1.game()