import re

from models.player import Player
from models.player_storage import save_players
from interfaces.player_interface import PlayerInterface

CHESS_ID_PATTERN = re.compile(r"^[A-Za-z]{2}\d{5}$")


class PlayerController:

    def __init__(self, players: list, view: PlayerInterface):
        self.players = players
        self.view = view

    def create_player(self):
        last_name, first_name, birth_date, chess_id = (
            self.view.prompt_new_player()
        )

        if not CHESS_ID_PATTERN.match(chess_id):
            self.view.show_message(
                "Identifiant invalide. Format attendu : "
                "deux lettres suivies de cinq chiffres (ex: AB12345)."
            )
            return

        new_player = Player(last_name, first_name, birth_date, chess_id)
        self.players.append(new_player)
        save_players(self.players)
        self.view.show_message(
            f"Joueur {new_player} ajouté avec succès."
        )

    def list_players(self):
        sorted_players = sorted(self.players, key=lambda p: p.last_name)
        self.view.show_players(sorted_players)