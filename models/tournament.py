import random


class Tournament:

    def __init__(self, name, location, start_date, end_date, number_of_rounds=4, description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.current_round = 0
        self.rounds = []
        self.players = []
        self.description = description

    def add_player(self, player):
        self.players.append(player)

    def is_finished(self):
        return self.current_round >= self.number_of_rounds

    def generate_round_pairs_random(self):
        
        shuffled_players = self.players.copy()
        random.shuffle(shuffled_players)

        pairs = []
        for i in range(0, len(shuffled_players) - 1, 2):
            pairs.append((shuffled_players[i], shuffled_players[i + 1]))
        return pairs

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "description": self.description,
            "players": [player.chess_id for player in self.players],
            "rounds": [round_.to_dict() for round_ in self.rounds],
        }

    def __repr__(self):
        return (
            f"{self.name} ({self.location}) - "
            f"tour {self.current_round}/{self.number_of_rounds}"
        )