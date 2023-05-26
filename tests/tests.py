import sys
import io
import unittest
from unittest.mock import patch

from snowman.snowman import snowman

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class TestSnowman(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_success_message_if_all_letters_guessed(self, mock_stdout):
        input_letters = [
            'n',
            'a',
            'm',
            'w',
            'o',
            'n',
            's',
        ]

        try:
            with unittest.mock.patch('builtins.input', side_effect=input_letters):
                snowman('snowman')
    
            assert "you win" in mock_stdout.getvalue().lower()

        except StopIteration as e:
            raise StopIteration("Code continued to request letters after game should have finished.").with_traceback(e.__traceback__)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_success_message_with_3_wrong_guesses_and_the_rest_right(self, mock_stdout):
        input_letters = [
            's',
            'n',
            'b',
            'o',
            'w',
            'm',
            'a',
            'q',
            'v',
            'n',
        ]

        try:
            with unittest.mock.patch('builtins.input', side_effect=input_letters):
            snowman('snowman')

            assert "you win" in mock_stdout.getvalue().lower()  
            assert "sorry, you lose!" not in mock_stdout.getvalue().lower()
            assert "the word was snowman" not in mock_stdout.getvalue().lower()

        except StopIteration as e:
            raise StopIteration("Code continued to request letters after game should have finished.").with_traceback(e.__traceback__)



    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_failure_message_with_7_straight_wrong_guesses(self, mock_stdout):
        input_letters = [
            'b',
            'c',
            'p',
            'z',
            'q',
            'v',
            'x',
        ]
        try:
            with unittest.mock.patch('builtins.input', side_effect=input_letters):
            snowman('snowman')

            assert "you win" not in mock_stdout.getvalue().lower()  
            assert "sorry, you lose!" in mock_stdout.getvalue().lower()
            assert "the word was snowman" in mock_stdout.getvalue().lower()

        except StopIteration as e:
            raise StopIteration("Code continued to request letters after game should have finished.").with_traceback(e.__traceback__)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_failure_message_with_7_wrong_guesses_and_two_right(self, mock_stdout):
        input_letters = [
            's',
            'b',
            'c',
            'p',
            'n',
            'z',
            'q',
            'v',
            'x',
        ]
        try:
            with unittest.mock.patch('builtins.input', side_effect=input_letters):
            snowman('snowman')
    
            assert "you win" not in mock_stdout.getvalue().lower()  
            assert "sorry, you lose!" in mock_stdout.getvalue().lower()
            assert "the word was snowman" in mock_stdout.getvalue().lower()

        except StopIteration as e:
            raise StopIteration("Code continued to request letters after game should have finished.").with_traceback(e.__traceback__)

    # Invalid letter please enter a single character.
if __name__ == '__main__':
    unittest.main(exit=False)