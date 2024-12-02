import io
import sys
import json
from contextlib import contextmanager

import pytest
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


def test_init():
    game = Game()
    game_json = json.dumps(vars(game), indent=4, sort_keys=True)
    verify(game_json)


def test_players_after_add():
    game = Game()
    game.add('Chet')
    assert game.players[0] == 'Chet'


def test_places_after_add():
    game = Game()
    game.add('Chet')
    assert game.places[0] == 0


def test_purses_after_add():
    game = Game()
    game.add('Chet')
    assert game.purses[0] == 0


def test_in_penalty_box_after_add():
    game = Game()
    game.add('Chet')
    assert game.in_penalty_box[0] == False


def test_how_many_players_after_add():
    game = Game()
    game.add('Chet')
    assert game.how_many_players == 1


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


def test_was_correctly_answered_right_result():
    game = Game()
    game.add('Chet')
    with redirect_stdout() as output:
        game.was_correctly_answered()
        assert output.getvalue() == "The answer was correct!\nChet now has 1 Gold Coins.\n"


def test_add_many_player():
    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')
    game.add('John')
    game.add('Doe')

    with redirect_stdout() as output:
        game.add('Jane')
        assert output.getvalue() == "Jane was added\nThey are player number 6\n"


def test_start_game_with_one_player():
    game = Game()
    game.add('Chet')
    with pytest.raises(Exception, match="Not enough players. At least 2 players are required to start the game."):
        game.roll(5)
