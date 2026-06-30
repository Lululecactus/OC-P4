import json
import random

from models.player import Player
from models.match import Match
from models.round import Round
from models.tournament import Tournament


def load_players_from_json(path):
    with open(path, "r", encoding="utf-8") as file:
        raw_data = json.load(file)
    return [Player.from_dict(player_data) for player_data in raw_data]


def main():
    players = load_players_from_json("data/players.json")
    print("--- Joueurs chargés depuis le JSON ---")
    for player in players:
        print(player)

    tournament = Tournament(
        name="Tournoi de printemps",
        location="Salle des fêtes",
        start_date="2026-06-21",
        end_date="2026-06-22",
        number_of_rounds=2,
        description="Tournoi de test pour valider les modèles",
    )
    for player in players:
        tournament.add_player(player)

    print(f"\n--- Tournoi créé : {tournament} ---")

    pairs = tournament.generate_round_pairs_random()
    round1 = Round("Round 1")
    matches = []
    for player1, player2 in pairs:
        match = Match(player1, player2)
        round1.add_match(match)
        matches.append(match)

    tournament.rounds.append(round1)
    tournament.current_round = 1

    print(f"\n--- Appariements générés pour {round1.name} ---")
    for match in matches:
        print(match)

    for match in matches:
        result = random.choice([0, 1, 2])
        match.set_result(result)

    round1.close()

    print(f"\n--- Résultats de {round1.name} ---")
    for match in matches:
        print(match)

    print("\n--- Classement après le tour ---")
    ranked_players = sorted(players, key=lambda p: p.points, reverse=True)
    for player in ranked_players:
        print(player)

    print(f"\nTour commencé à : {round1.start_datetime}")
    print(f"Tour terminé à  : {round1.end_datetime}")
    print(f"\nLe tournoi est-il terminé ? {tournament.is_finished()}")


if __name__ == "__main__":
    main()