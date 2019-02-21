# LOSE = 0
# WIN = 1
#
# enum
#
# guess_number = 999
# number_oportunities = 23
# game=Game(guess_number, number_oportunities)
# game.play() -> Win, Lose, Higher, Lower
# return WIN

import random

class Play():
    def __init__(self):
        self.number_to_guess = 5
        self.selected_number = 0


    def number_introduced(self):
        return random.randint(1, 10)

    def compare_number(self, num1, num2):
        if num1 == num2:
            print("You Win")
            self.opportunities = 0
        elif num1 > num2:
            print("Your number is greater than the number to guess")
            self.opportunities-=1
        else:
            print(" Your number is lesser than the number to guess")
            self.opportunities -= 1

    def game(self):
        while(self.opportunities > 0):
            #self.selected_number = self.number_introduced()
            self.compare_number(self.selected_number, self.number_to_guess)
            if self.opportunities == 0:
                print("You loss")