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
    def __init__(self, guess_number):
        self.guess_number = guess_number
        self.oportunities = 0
        self.number_to_guess = 12
        self.win = 1
        self.lose = 2
        self.higher = 3
        self.lower = 4

    def play(self):
        while self.oportunities < 6:
            self.oportunities += 1
            if self.guess_number < self.number_to_guess:
                return self.lower
            elif self.guess_number > self.number_to_guess:
                return self.higher
            elif self.guess_number == self.number_to_guess:
                return self.win
            else:
                return self.lose
 f
game1 = Game(23)
game1.play()
