#!/usr/bin/env python3
from typing import List

from Player import Player
from i18n import LANGUAGES, I18n


class Game:
    def __init__(self, lang:LANGUAGES='de'):
        self.players: List[Player] = []

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0

        for i in range(50):
            self.pop_questions.append(f"Pop Question %s" % i)
            self.science_questions.append(f"Science Question %s" % i)
            self.sports_questions.append(f"Sports Question %s" % i)
            self.rock_questions.append(self.create_rock_question(i))

    def create_rock_question(self, index):
        return "Rock Question %s" % index

    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        self.players.append(Player(name=player_name))

        print(f"{player_name} was added with number {len(self.players)}")

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    @property
    def num_fields(self):
        return 16

    def roll(self, roll):
        if not self.is_playable():
            raise ValueError("Not enough players. At least 2 players are required to start the game.")
        current_player = self.players[self.current_player]
        print("%s is the current player" % current_player.name)
        print("They have rolled a %s" % roll)

        if current_player.in_penalty_box:
            if roll % 2 != 0:
                current_player.set_getting_out_of_penalty_box(True)

                print("%s is getting out of the penalty box" % current_player.name)
                current_player.move(current_player.place + roll)
                if current_player.place > self.num_fields - 1:
                    current_player.move(current_player.place - self.num_fields)

                print(current_player.name + \
                      '\'s new location is ' + \
                      str(current_player.place))
                print("The category is %s" % self._current_category)
                self._ask_question()
            else:
                print("%s is not getting out of the penalty box" % current_player.name)
                current_player.set_getting_out_of_penalty_box(False)
        else:
            current_player.move(current_player.place + roll)
            if current_player.place > 11:
                current_player.move(current_player.place - 12)

            print(current_player.name + \
                  '\'s new location is ' + \
                  str(current_player.place))
            print("The category is %s" % self._current_category)
            self._ask_question()

    def _ask_question(self):
        if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category == 'Rock': print(self.rock_questions.pop(0))

    @property
    def _current_category(self):
        current_player = self.players[self.current_player]
        if current_player.place == 0: return 'Pop'
        if current_player.place == 4: return 'Pop'
        if current_player.place == 8: return 'Pop'
        if current_player.place == 12: return 'Pop'
        if current_player.place == 1: return 'Science'
        if current_player.place == 5: return 'Science'
        if current_player.place == 9: return 'Science'
        if current_player.place == 13: return 'Science'
        if current_player.place == 2: return 'Sports'
        if current_player.place == 6: return 'Sports'
        if current_player.place == 10: return 'Sports'
        if current_player.place == 14: return 'Sports'
        return 'Rock'

    def was_correctly_answered(self):
        current_player = self.players[self.current_player]
        if current_player.in_penalty_box and not current_player.is_getting_out_of_penalty_box:
            self.current_player += 1
            if self.current_player == len(self.players): self.current_player = 0
            return True

        print("The answer was correct!")
        current_player.add_score(1)
        print(current_player.name + \
              ' now has ' + \
              str(current_player.purse) + \
              ' Gold Coins.')

        winner = current_player.did_player_win()
        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0

        return winner

    def wrong_answer(self):
        current_player = self.players[self.current_player]
        print('Question was incorrectly answered')
        print(current_player.name + " was sent to the penalty box")
        current_player.put_in_penalty_box()

        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return True



from random import randrange

if __name__ == '__main__':
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break
