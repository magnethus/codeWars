# LOSE = 0
# WIN = 1
#
# enum
#
# guess_number = 999
# number_oportunities = 0
# game=Game(guess_number, number_oportunities)
# game.play() -> Win, Lose, Higher, Lower
# return WIN

class Game():
    def __init__(self, guess_number, number_oportunities):
        self.guess_number = guess_number
        self.number_oportunities = number_oportunities
        self.win = 1
        self.lose = 2
        self.higher = 3
        self.lower = 4
        self.counter = 0


    def compare_number(self, number_introduced, guess_number ):
        while self.counter < self.number_oportunities:
            self.counter += 1
            if self.number_introduced < self.guess_number:
                return {self.lower}
            elif self.number_introduced > self.guess_number:
                return {self.higher}
            elif self.number_introduced == self.guess_number:
                return {self.win}
            else:
                return {self.lose}

