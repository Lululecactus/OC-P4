from models.player_storage import load_players
from views.menu_view import MenuView
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from views.report_view import ReportView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController
from constants import (
    MAIN_ADD_PLAYER,
    MAIN_LIST_PLAYERS,
    MAIN_TOURNAMENTS,
    MAIN_REPORTS,
    MAIN_QUIT,
)


class MainController:

    def __init__(self):
        players = load_players()
        players_dict = {p.chess_id: p for p in players}

        menu_view = MenuView()
        player_view = PlayerView()
        tournament_view = TournamentView()
        report_view = ReportView()

        self.menu_view = menu_view
        self.player_controller = PlayerController(players, player_view)
        self.tournament_controller = TournamentController(
            players_dict, tournament_view
        )
        self.report_controller = ReportController(players_dict, report_view)

    def run(self):
        while True:
            choice = self.menu_view.show_main_menu()

            if choice == MAIN_ADD_PLAYER:
                self.player_controller.create_player()

            elif choice == MAIN_LIST_PLAYERS:
                self.player_controller.list_players()

            elif choice == MAIN_TOURNAMENTS:
                self.tournament_controller.tournament_menu()

            elif choice == MAIN_REPORTS:
                self.report_controller.reports_menu()

            elif choice == MAIN_QUIT:
                self.menu_view.show_message("Au revoir !")
                break

            else:
                self.menu_view.show_message("Choix invalide, réessayez.")