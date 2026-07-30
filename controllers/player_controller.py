import re

from models.player import Player
from models.player_storage import PlayerStorage
from interfaces.player_interface import PlayerInterface
from constants import PLAYER_ADD, PLAYER_LIST, PLAYER_BACK
from utils import clear_screen

CHESS_ID_PATTERN = re.compile(r"^[A-Za-z]{2}\d{5}$")


class PlayerController:
    def __init__(self, view: PlayerInterface):
        self.view = view
        self.storage = PlayerStorage()
        self.players = self.storage.load()

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
        self.storage.save(self.players)
        self.view.show_message(f"Joueur {new_player} ajouté avec succès.")

    def list_players(self):
        sorted_players = sorted(self.players, key=lambda p: p.last_name)
        self.view.show_players(sorted_players)

    def get_players_dict(self):
        return {p.chess_id: p for p in self.players}

    def player_menu(self):
        while True:
            clear_screen()
            choice = self.view.show_player_menu()

            if choice == PLAYER_ADD:
                self.create_player()
            elif choice == PLAYER_LIST:
                self.list_players()
                input("\nAppuyez sur Entrée pour continuer...")
            elif choice == PLAYER_BACK:
                break
            else:
                self.view.show_message("Choix invalide.")