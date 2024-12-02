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


def test_dummy():
    with redirect_stdout() as output:
        game = Game()
        game.add('Chet')
        assert output.getvalue() == 'Chet was added\nThey are player number 1\n'
