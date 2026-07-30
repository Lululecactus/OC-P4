"""Contrôleur rapports."""

from models.tournament_storage import TournamentStorage
from models.player_storage import PlayerStorage
from interfaces.report_interface import ReportInterface
from constants import (
    REPORT_ALL_PLAYERS,
    REPORT_ALL_TOURNAMENTS,
    REPORT_TOURNAMENT_INFO,
    REPORT_TOURNAMENT_PLAYERS,
    REPORT_TOURNAMENT_ROUNDS,
    REPORT_BACK,
)
from utils import clear_screen


class ReportController:
    """Gère la logique d'affichage des rapports."""

    def __init__(self, view: ReportInterface):
        self.view = view
        self.storage = TournamentStorage()
        self.player_storage = PlayerStorage()

    def _get_players_dict(self):
        players = self.player_storage.load()
        return {p.chess_id: p for p in players}

    def report_all_players(self):
        players = self.player_storage.load()
        self.view.show_all_players_alpha(players)

    def report_all_tournaments(self):
        tournaments_data = self.storage.load_all()
        self.view.show_all_tournaments(tournaments_data)

    def _select_and_load_tournament(self):
        tournaments_data = self.storage.load_all()
        name = self.view.prompt_select_tournament(tournaments_data)
        if name is None:
            return None
        players_dict = self._get_players_dict()
        return self.storage.load(name, players_dict)

    def report_tournament_info(self):
        tournament = self._select_and_load_tournament()
        if tournament:
            self.view.show_tournament_info(tournament)

    def report_tournament_players(self):
        tournament = self._select_and_load_tournament()
        if tournament:
            self.view.show_tournament_players_alpha(tournament)

    def report_tournament_rounds(self):
        tournament = self._select_and_load_tournament()
        if tournament:
            self.view.show_tournament_rounds_and_matches(tournament)

    def reports_menu(self):
        """Sous-menu rapports."""
        while True:
            clear_screen()
            choice = self.view.show_report_menu()

            if choice == REPORT_ALL_PLAYERS:
                self.report_all_players()
                self.view.show_message("Rapport affiche.")
            elif choice == REPORT_ALL_TOURNAMENTS:
                self.report_all_tournaments()
                self.view.show_message("Rapport affiche.")
            elif choice == REPORT_TOURNAMENT_INFO:
                self.report_tournament_info()
                self.view.show_message("Rapport affiche.")
            elif choice == REPORT_TOURNAMENT_PLAYERS:
                self.report_tournament_players()
                self.view.show_message("Rapport affiche.")
            elif choice == REPORT_TOURNAMENT_ROUNDS:
                self.report_tournament_rounds()
                self.view.show_message("Rapport affiche.")
            elif choice == REPORT_BACK:
                break
            else:
                self.view.show_message("Choix invalide.")
