import unittest
from Guess_The_Number.game_status import GameStatus
from Guess_The_Number.guess_game import GuessGame

class MyTestCase(unittest.TestCase):

    def test_win(self):
        expected = GameStatus.WIN
        print("for Test Win")
        game = GuessGame(3)
        actual = game.play(3, 5)
        self.assertEqual(expected, actual)

    def test_Higuer(self):
        expected = GameStatus.HIGHER
        print("for Test Higuer")
        game = GuessGame(3)
        actual = game.play(4, 5)
        self.assertEqual(expected, actual)

    def test_lower(self):
        expected = GameStatus.LOWER
        print("for Test lower")
        game = GuessGame(3)
        actual = game.play(2, 4)
        self.assertEqual(expected, actual)

    def test_lose(self):
        expected = GameStatus.LOSE
        print("for Test loose")
        game = GuessGame(3)
        actual = game.play(5, 0)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()