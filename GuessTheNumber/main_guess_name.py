from GuessTheNumber.game_status import GameStatus
from GuessTheNumber.player import Player
from GuessTheNumber.multiplayer import Multiplayer

# number_to_guess = randint(1, 10)

player1 = Player("Alex")
player2 = Player("Ksyus")
players = [player1, player2]


for p in players:
    while p.number_of_attempts >= 0:
        number = input(f"Please enter a number: {p}") #String
        result = p.play(int(number))
        if result != GameStatus.WIN:
            if result == GameStatus.WIN:
                print("You Won!")
                p.rotate(players, result)
            elif result == GameStatus.LOSE:
                print("You LOST!")
                break
            elif result == GameStatus.HIGHER:
                print("The number is higher")
            elif result == GameStatus.LOWER:
                print("The number is lower")