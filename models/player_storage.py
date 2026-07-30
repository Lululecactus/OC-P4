"""Classe de persistance pour les joueurs."""

import json
import os

from models.player import Player

PLAYERS_FILE = "data/players.json"


class PlayerStorage:

    def __init__(self, filepath=PLAYERS_FILE):
        self.filepath = filepath

    def load(self):
        if not os.path.exists(self.filepath):
            return []

        with open(self.filepath, "r", encoding="utf-8") as file:
            raw_data = json.load(file)

        return [Player.from_dict(data) for data in raw_data]

    def save(self, players):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        raw_data = [player.to_dict() for player in players]

        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump(raw_data, file, indent=2, ensure_ascii=False)