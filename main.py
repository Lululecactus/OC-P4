from views.menu_view import MenuView
from controllers.player_controller import PlayerController


def main():
    player_controller = PlayerController()

    while True:
        choice = MenuView.show_main_menu()

        if choice == "1":
            player_controller.create_player()
        elif choice == "2":
            player_controller.list_players()
        elif choice == "3":
            MenuView.show_message("Au revoir !")
            break
        else:
            MenuView.show_message("Choix invalide, réessayez.")


if __name__ == "__main__":
    main()
