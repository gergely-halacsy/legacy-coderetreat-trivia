import io
import sys
from contextlib import contextmanager

from approvaltests.approvals import verify

from trivia import Game


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
    game = Game()
    game.add('Chet')
    game.add('Pat')
    game.add('Sue')
    with redirect_stdout() as output:
        game.roll(5)
        verify(output.getvalue())


def test_roll_in_penalty_box():
    game = Game()
    game.add('Chet')
    game.wrong_answer()
    with redirect_stdout() as output:
        game.roll(4)
        verify(output.getvalue())


def test_roll_in_penalty_box_get_out():
    game = Game()
    game.add('Chet')
    game.wrong_answer()
    with redirect_stdout() as output:
        game.roll(5)
        verify(output.getvalue())


def test_wrong_answer():
    game = Game()
    game.add('Chet')
    with redirect_stdout() as output:
        result = game.wrong_answer()
        verify(output.getvalue())
        assert result

def test_was_correctly_answered():
    game = Game()
    game.add('Chet')
    with redirect_stdout() as output:
        result = game.was_correctly_answered()
        assert result
        verify(output.getvalue())
        
def test_was_correctly_answered_after_wrong_answer():
    game = Game()
    game.add('Chet')
    game.wrong_answer()
    with redirect_stdout() as output:
        result = game.was_correctly_answered()
        assert result
        verify(output.getvalue())

def test_was_correctly_answered_after_wrong_answer_out_of_penalty_box():
    game = Game()
    game.add('Chet')
    game.wrong_answer()
    game.is_getting_out_of_penalty_box = True 
    with redirect_stdout() as output:
        result = game.was_correctly_answered()
        assert result
        verify(output.getvalue())