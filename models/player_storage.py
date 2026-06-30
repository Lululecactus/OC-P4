import json
import os

from models.player import Player

PLAYERS_FILE = "data/players.json"


def load_players():
    if not os.path.exists(PLAYERS_FILE):
        return []
    with open(PLAYERS_FILE, "r", encoding="utf-8") as file:
        raw_data = json.load(file)
    return [Player.from_dict(player_data) for player_data in raw_data]


def save_players(players):
    os.makedirs(os.path.dirname(PLAYERS_FILE), exist_ok=True)
    raw_data = [player.to_dict() for player in players]
    with open(PLAYERS_FILE, "w", encoding="utf-8") as file:
        json.dump(raw_data, file, indent=2, ensure_ascii=False)