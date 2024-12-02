class Player:
    def __init__(self, name):
        self.name = name
        self.purse = 0
        self.place = 0
        self.in_penalty_box = False
        self.is_getting_out_of_penalty_box = False

    def add_score(self, score):
        self.purse += score

    def move(self, places):
        self.place = places

    def put_in_penalty_box(self):
        self.in_penalty_box = True

    def take_out_of_penalty_box(self):
        self.in_penalty_box = False

    def is_in_penalty_box(self):
        return self.in_penalty_box

    def set_getting_out_of_penalty_box(self, value):
        self.is_getting_out_of_penalty_box = value

    def __str__(self):
        return f"{self.name} has {self.purse} coins"

    def did_player_win(self):
        return not self.purse == 6