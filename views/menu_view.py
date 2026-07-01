class MenuView:

    @staticmethod
    def show_main_menu():
        print("\n=== Gestion de tournoi d'échecs ===")
        print("1. Ajouter un joueur")
        print("2. Lister les joueurs")
        print("3. Quitter")
        return input("Votre choix : ")

    @staticmethod
    def show_message(message):
        print(message)