class MenuView:
   

    def show_main_menu(self):
        print("\n========================================")
        print("   Gestion de tournoi d'échecs")
        print("========================================")
        print("1. Joueurs")
        print("2. Tournois")
        print("3. Rapports")
        print("4. Quitter")
        print("----------------------------------------")
        return input("Votre choix : ")

    def show_player_menu(self):
        print("\n--- Joueurs ---")
        print("1. Ajouter un joueur")
        print("2. Lister les joueurs")
        print("0. Retour")
        return input("Votre choix : ")

    def show_message(self, message):
        print(message)

    def wait_for_enter(self):
        input("\nAppuyez sur Entrée pour continuer...")