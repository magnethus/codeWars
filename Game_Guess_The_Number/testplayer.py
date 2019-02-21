import unittest

from Game_Guess_The_Number.player import Player


class Guest_number_test(unittest.TestCase):
    def test_equal_number(self):
        # AAA Arrange Act Assert
        # Arrange - preparar los datos de prueba
        player1 = Player("player_1")


        # Act
        player1.number_to_guess = 1
        player1.selected_number = 1

        # Assert
        player1.game
        self.assertEqual(None, actual_result)


