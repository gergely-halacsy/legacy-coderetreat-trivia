from random import randrange

from trivia import Game
import pytest
from contextlib import contextmanager
import io
import sys

from approvaltests.approvals import verify


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
        verify(output.getvalue())


def test_create_rock_question():
    game = Game()
    created_question = game.create_rock_question(42)
    verify(created_question)


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
