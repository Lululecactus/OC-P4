from views.menu_view import MenuView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController


def main():
    player_controller = PlayerController()

    players_dict = {p.chess_id: p for p in player_controller.players}

    tournament_controller = TournamentController(players_dict)
    report_controller = ReportController(players_dict)

    while True:
        choice = MenuView.show_main_menu()

        if choice == "1":
            player_controller.create_player()
            players_dict[player_controller.players[-1].chess_id] = (
                player_controller.players[-1]
            )
        elif choice == "2":
            player_controller.list_players()
        elif choice == "3":
            tournament_controller.tournament_menu()
        elif choice == "4":
            report_controller.reports_menu()
        elif choice == "5":
            MenuView.show_message("Au revoir !")
            break
        else:
            MenuView.show_message("Choix invalide, réessayez.")


if __name__ == "__main__":
    main()