from models.tournament_storage import load_all_tournaments, load_tournament
from interfaces.report_interface import ReportInterface
from constants import (
    REPORT_ALL_PLAYERS,
    REPORT_ALL_TOURNAMENTS,
    REPORT_TOURNAMENT_INFO,
    REPORT_TOURNAMENT_PLAYERS,
    REPORT_TOURNAMENT_ROUNDS,
    REPORT_BACK,
)


class ReportController:

    def __init__(self, players_dict: dict, view: ReportInterface):
        self.players_dict = players_dict
        self.view = view

    def report_all_players(self):
        players = list(self.players_dict.values())
        self.view.show_all_players_alpha(players)

    def report_all_tournaments(self):
        tournaments_data = load_all_tournaments()
        self.view.show_all_tournaments(tournaments_data)

    def _select_and_load_tournament(self):
        tournaments_data = load_all_tournaments()
        name = self.view.prompt_select_tournament(tournaments_data)
        if name is None:
            return None
        return load_tournament(name, self.players_dict)

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
        while True:
            print("\n--- Rapports ---")
            print(f"{REPORT_ALL_PLAYERS}. Tous les joueurs (alphabétique)")
            print(f"{REPORT_ALL_TOURNAMENTS}. Tous les tournois")
            print(f"{REPORT_TOURNAMENT_INFO}. Informations d'un tournoi")
            print(f"{REPORT_TOURNAMENT_PLAYERS}. Joueurs d'un tournoi")
            print(f"{REPORT_TOURNAMENT_ROUNDS}. Tours et matchs d'un tournoi")
            print(f"{REPORT_BACK}. Retour au menu principal")

            choice = input("Votre choix : ")

            if choice == REPORT_ALL_PLAYERS:
                self.report_all_players()
            elif choice == REPORT_ALL_TOURNAMENTS:
                self.report_all_tournaments()
            elif choice == REPORT_TOURNAMENT_INFO:
                self.report_tournament_info()
            elif choice == REPORT_TOURNAMENT_PLAYERS:
                self.report_tournament_players()
            elif choice == REPORT_TOURNAMENT_ROUNDS:
                self.report_tournament_rounds()
            elif choice == REPORT_BACK:
                break
            else:
                self.view.show_message("Choix invalide.")