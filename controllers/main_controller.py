from models.player_storage import load_players
from views.menu_view import MenuView
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from views.report_view import ReportView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController
from constants import (
    MAIN_PLAYERS,
    MAIN_TOURNAMENTS,
    MAIN_REPORTS,
    MAIN_QUIT,
    PLAYER_ADD,
    PLAYER_LIST,
    PLAYER_BACK,
)


class MainController:

    def __init__(self):
        players = load_players()
        players_dict = {p.chess_id: p for p in players}

        self.menu_view = MenuView()
        player_view = PlayerView()
        tournament_view = TournamentView()
        report_view = ReportView()

        self.player_controller = PlayerController(players, player_view)
        self.tournament_controller = TournamentController(
            players_dict, tournament_view
        )
        self.report_controller = ReportController(players_dict, report_view)

    def _player_menu(self):
        while True:
            choice = self.menu_view.show_player_menu()

            if choice == PLAYER_ADD:
                self.player_controller.create_player()
                self.menu_view.wait_for_enter()

            elif choice == PLAYER_LIST:
                self.player_controller.list_players()
                self.menu_view.wait_for_enter()

            elif choice == PLAYER_BACK:
                break

            else:
                self.menu_view.show_message("Choix invalide.")

    def run(self):
        while True:
            choice = self.menu_view.show_main_menu()

            if choice == MAIN_PLAYERS:
                self._player_menu()

            elif choice == MAIN_TOURNAMENTS:
                self.tournament_controller.tournament_menu()

            elif choice == MAIN_REPORTS:
                self.report_controller.reports_menu()

            elif choice == MAIN_QUIT:
                self.menu_view.show_message("Au revoir !")
                break

            else:
                self.menu_view.show_message("Choix invalide, réessayez.")