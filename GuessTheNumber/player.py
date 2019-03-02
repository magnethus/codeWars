from GuessTheNumber.multiplayer import Multiplayer
from GuessTheNumber.guess_game import GuessGame
from random import randint

class Player(GuessGame, Multiplayer):

    def __init__(self, player_name):
        self.player_name = player_name
        self.number_of_attempts = 4
        self.number_to_guess = randint(1, 10)

    def __repr__(self):
        return f"{self.player_name}"







