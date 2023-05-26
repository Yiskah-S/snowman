import pytest
from io import StringIO
from unittest.mock import patch
from wonderwords import RandomWord
from game import snowman, MIN_WORD_LENGTH, MAX_WORD_LENGTH

def test_prints_success_message_if_all_letters_guessed(monkeypatch):
    input_letters = ['n', 'a', 'm', 'w', 'o', 'n', 's']
    monkeypatch.setattr('builtins.input', lambda _: input_letters.pop(0))
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        snowman('snowman')
    assert "you win" in mock_stdout.getvalue().lower()


def test_prints_success_message_with_3_wrong_guesses_and_the_rest_right(monkeypatch):
    input_letters = ['s', 'n', 'b', 'o', 'w', 'm', 'a', 'q', 'v', 'n']
    monkeypatch.setattr('builtins.input', lambda _: input_letters.pop(0))
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        snowman('snowman')
    assert "you win" in mock_stdout.getvalue().lower()
    assert "sorry, you lose!" not in mock_stdout.getvalue().lower()
    assert "the word was snowman" not in mock_stdout.getvalue().lower()


def test_prints_failure_message_with_7_straight_wrong_guesses(monkeypatch):
    input_letters = ['b', 'c', 'p', 'z', 'q', 'v', 'x']
    monkeypatch.setattr('builtins.input', lambda _: input_letters.pop(0))
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        snowman('snowman')
    assert "you win" not in mock_stdout.getvalue().lower()
    assert "sorry, you lose!" in mock_stdout.getvalue().lower()
    assert "the word was snowman" in mock_stdout.getvalue().lower()


def test_prints_failure_message_with_7_wrong_guesses_and_two_right(monkeypatch):
    input_letters = ['s', 'b', 'c', 'p', 'n', 'z', 'q', 'v', 'x']
    monkeypatch.setattr('builtins.input', lambda _: input_letters.pop(0))
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        snowman('snowman')
    assert "you win" not in mock_stdout.getvalue().lower()
    assert "sorry, you lose!" in mock_stdout.getvalue().lower()
    assert "the word was snowman" in mock_stdout.getvalue().lower()
