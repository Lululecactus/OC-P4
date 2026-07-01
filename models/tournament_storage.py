import json
import os

from models.player_storage import load_players
from models.tournament import Tournament
from models.round import Round
from models.match import Match

TOURNAMENTS_DIR = "data/tournaments"


def get_tournament_path(tournament_name):
    safe_name = tournament_name.replace(" ", "_").lower()
    return os.path.join(TOURNAMENTS_DIR, f"{safe_name}.json")


def save_tournament(tournament):
    os.makedirs(TOURNAMENTS_DIR, exist_ok=True)
    path = get_tournament_path(tournament.name)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(tournament.to_dict(), file, indent=2, ensure_ascii=False)


def load_all_tournaments():
    if not os.path.exists(TOURNAMENTS_DIR):
        return []

    tournaments = []
    for filename in os.listdir(TOURNAMENTS_DIR):
        if filename.endswith(".json"):
            path = os.path.join(TOURNAMENTS_DIR, filename)
            with open(path, "r", encoding="utf-8") as file:
                tournaments.append(json.load(file))

    return tournaments


def load_tournament(tournament_name, players_dict):
    path = get_tournament_path(tournament_name)

    if not os.path.exists(path):
        return None

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    tournament = Tournament(
        name=data["name"],
        location=data["location"],
        start_date=data["start_date"],
        end_date=data["end_date"],
        number_of_rounds=data.get("number_of_rounds", 4),
        description=data.get("description", ""),
    )
    tournament.current_round = data.get("current_round", 0)

    for chess_id in data.get("players", []):
        if chess_id in players_dict:
            tournament.add_player(players_dict[chess_id])

    for round_data in data.get("rounds", []):
        round_obj = Round(round_data["name"])
        round_obj.start_datetime = round_data["start_datetime"]
        round_obj.end_datetime = round_data["end_datetime"]

        for match_data in round_data.get("matches", []):
            p1 = players_dict.get(match_data[0][0])
            p2 = players_dict.get(match_data[1][0])
            if p1 and p2:
                match = Match(p1, p2)
                match.data[0][1] = match_data[0][1]
                match.data[1][1] = match_data[1][1]
                round_obj.add_match(match)

        tournament.rounds.append(round_obj)

    return tournament