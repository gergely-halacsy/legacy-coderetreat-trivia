from random import randrange

from trivia import Game
import pytest
from contextlib import contextmanager
import io
import sys


@contextmanager
def redirect_stdout():
    try:
        cap = io.StringIO()
        sys.stdout = cap
        yield cap
    finally:
        sys.stdout = sys.__stdout__


def test_adding_player():
    with redirect_stdout() as output:
        game = Game()
        game.add('Chet')
        assert output.getvalue() == 'Chet was added\nThey are player number 1\n'


def test_create_rock_question():
    game = Game()
    created_question = game.create_rock_question(42)
    assert created_question == "Rock Question 42"


def test_is_playable_false():
    game = Game()
    game.add('Chet')
    assert game.is_playable() == False


def test_is_playable_true():
    game = Game()
    game.add('Chet')
    game.add('Pat')
    assert game.is_playable() == True


def test_roll():
    with redirect_stdout() as output:
        game = Game()
        game.add('Chet')
        game.add('Pat')
        game.add('Sue')
