from models.player_storage import load_players
from models.tournament_storage import load_all_tournaments, load_tournament
from views.report_view import ReportView


class ReportController:

    def __init__(self, players_dict):
        self.players_dict = players_dict

    def report_all_players(self):
       
        players = list(self.players_dict.values())
        ReportView.show_all_players_alpha(players)

    def report_all_tournaments(self):
        
        tournaments_data = load_all_tournaments()
        ReportView.show_all_tournaments(tournaments_data)

    def _select_and_load_tournament(self):
        tournaments_data = load_all_tournaments()
        name = ReportView.prompt_select_tournament(tournaments_data)
        if name is None:
            return None
        return load_tournament(name, self.players_dict)

    def report_tournament_info(self):
        
        tournament = self._select_and_load_tournament()
        if tournament:
            ReportView.show_tournament_info(tournament)

    def report_tournament_players(self):
        tournament = self._select_and_load_tournament()
        if tournament:
            ReportView.show_tournament_players_alpha(tournament)

    def report_tournament_rounds(self):
        tournament = self._select_and_load_tournament()
        if tournament:
            ReportView.show_tournament_rounds_and_matches(tournament)

    def reports_menu(self):
        while True:
            print("\n--- Rapports ---")
            print("1. Tous les joueurs (alphabétique)")
            print("2. Tous les tournois")
            print("3. Informations d'un tournoi")
            print("4. Joueurs d'un tournoi (alphabétique)")
            print("5. Tours et matchs d'un tournoi")
            print("0. Retour au menu principal")

            choice = input("Votre choix : ")

            if choice == "1":
                self.report_all_players()
            elif choice == "2":
                self.report_all_tournaments()
            elif choice == "3":
                self.report_tournament_info()
            elif choice == "4":
                self.report_tournament_players()
            elif choice == "5":
                self.report_tournament_rounds()
            elif choice == "0":
                break
            else:
                ReportView.show_message("Choix invalide.")