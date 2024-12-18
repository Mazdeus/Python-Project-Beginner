import unittest
from unittest.mock import patch
from io import StringIO
import random
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from _1_number_guessing_game import number_to_guess, chances

class TestNumberGuessingGame(unittest.TestCase):

    @patch('builtins.input', side_effect=[number_to_guess])
    @patch('sys.stdout', new_callable=StringIO)
    def test_correct_guess(self, mock_stdout, mock_input):
        # Simulate the game
        guess_counter = 0
        while guess_counter < chances:
            guess_counter += 1
            my_guess = int(input("Enter your guess: "))
            if my_guess == number_to_guess:
                print(f'The number is {number_to_guess} and you found it right!! in the {guess_counter} attempt')
                break
        output = mock_stdout.getvalue().strip()
        self.assertIn(f'The number is {number_to_guess} and you found it right!! in the {guess_counter} attempt', output)

    @patch('builtins.input', side_effect=[number_to_guess + 1] * chances)
    @patch('sys.stdout', new_callable=StringIO)
    def test_exhausted_chances(self, mock_stdout, mock_input):
        # Simulate the game
        guess_counter = 0
        while guess_counter < chances:
            guess_counter += 1
            my_guess = int(input("Enter your guess: "))
            if my_guess == number_to_guess:
                print(f'The number is {number_to_guess} and you found it right!! in the {guess_counter} attempt')
                break
            elif guess_counter >= chances and my_guess != number_to_guess:
                print(f'You have exhausted all your chances. The number was {number_to_guess}')
            elif my_guess > number_to_guess:
                print("Your guess is too high")
            else:
                print("Your guess is too low")
        output = mock_stdout.getvalue().strip()
        self.assertIn(f'You have exhausted all your chances. The number was {number_to_guess}', output)

    @patch('builtins.input', side_effect=[number_to_guess + 1, number_to_guess])
    @patch('sys.stdout', new_callable=StringIO)
    def test_guess_too_high_then_correct(self, mock_stdout, mock_input):
        # Simulate the game
        guess_counter = 0
        while guess_counter < chances:
            guess_counter += 1
            my_guess = int(input("Enter your guess: "))
            if my_guess == number_to_guess:
                print(f'The number is {number_to_guess} and you found it right!! in the {guess_counter} attempt')
                break
            elif guess_counter >= chances and my_guess != number_to_guess:
                print(f'You have exhausted all your chances. The number was {number_to_guess}')
            elif my_guess > number_to_guess:
                print("Your guess is too high")
            else:
                print("Your guess is too low")
        output = mock_stdout.getvalue().strip()
        self.assertIn("Your guess is too high", output)
        self.assertIn(f'The number is {number_to_guess} and you found it right!! in the {guess_counter} attempt', output)

    @patch('builtins.input', side_effect=[number_to_guess - 1, number_to_guess])
    @patch('sys.stdout', new_callable=StringIO)
    def test_guess_too_low_then_correct(self, mock_stdout, mock_input):
        # Simulate the game
        guess_counter = 0
        while guess_counter < chances:
            guess_counter += 1
            my_guess = int(input("Enter your guess: "))
            if my_guess == number_to_guess:
                print(f'The number is {number_to_guess} and you found it right!! in the {guess_counter} attempt')
                break
            elif guess_counter >= chances and my_guess != number_to_guess:
                print(f'You have exhausted all your chances. The number was {number_to_guess}')
            elif my_guess > number_to_guess:
                print("Your guess is too high")
            else:
                print("Your guess is too low")
        output = mock_stdout.getvalue().strip()
        self.assertIn("Your guess is too low", output)
        self.assertIn(f'The number is {number_to_guess} and you found it right!! in the {guess_counter} attempt', output)

if __name__ == '__main__':
    unittest.main()