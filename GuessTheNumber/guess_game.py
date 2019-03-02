from GuessTheNumber.game_status import GameStatus


class GuessGame:
    def __init__(self, number_to_guess, number_of_attempts):
        self.number_to_guess = number_to_guess
        self.number_of_attempts = number_of_attempts

    #Hint
    def play(self, number: int):

        if number == self.number_to_guess and self.number_of_attempts > 0:
            self.number_of_attempts -= 1
            return GameStatus.WIN

        if number < self.number_to_guess and self.number_of_attempts > 0:
            self.number_of_attempts -= 1
            return GameStatus.LOWER

        if number > self.number_to_guess and self.number_of_attempts > 0:
            self.number_of_attempts -= 1
            return GameStatus.HIGHER

        if number != self.number_to_guess and self.number_of_attempts == 0:
            return GameStatus.LOSE