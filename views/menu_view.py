from interfaces.menu_interface import MenuInterface


class MenuView(MenuInterface):

    def show_main_menu(self):
        print("\n=== Gestion de tournoi d'échecs ===")
        print("1. Ajouter un joueur")
        print("2. Lister les joueurs")
        print("3. Gérer les tournois")
        print("4. Rapports")
        print("5. Quitter")
        return input("Votre choix : ")

    def show_message(self, message):
        print(message)