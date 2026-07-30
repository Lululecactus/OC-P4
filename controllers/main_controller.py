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
)
from utils import clear_screen


class MainController:
    def __init__(self):
        self.menu_view = MenuView()
        self.player_controller = PlayerController(PlayerView())
        self.tournament_controller = TournamentController(TournamentView())
        self.report_controller = ReportController(ReportView())

    def run(self):
        while True:
            clear_screen()
            choice = self.menu_view.show_main_menu()

            if choice == MAIN_PLAYERS:
                self.player_controller.player_menu()
            elif choice == MAIN_TOURNAMENTS:
                self.tournament_controller.tournament_menu()
            elif choice == MAIN_REPORTS:
                self.report_controller.reports_menu()
            elif choice == MAIN_QUIT:
                self.menu_view.show_message("Au revoir !")
                break
            else:
                self.menu_view.show_message("Choix invalide, réessayez.")
