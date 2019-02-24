from Guess_The_Number.game_status import GameStatus


class GuessGame:
    def __init__(self, number_to_guess):
        self.number_to_guess = number_to_guess

    def play(self, number, attemps):
        if number == self.number_to_guess and attemps > 0:
            return GameStatus.WIN

        if number < self.number_to_guess and attemps > 0:
            return GameStatus.LOWER

        if number > self.number_to_guess and attemps > 0:
            return GameStatus.HIGHER

        if  attemps == 0:
            return GameStatus.LOSE
