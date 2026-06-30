class PlayerView:

    @staticmethod
    def prompt_new_player():
        print("\n--- Ajouter un nouveau joueur ---")
        last_name = input("Nom de famille : ")
        first_name = input("Prénom : ")
        birth_date = input("Date de naissance (AAAA-MM-JJ) : ")
        chess_id = input("Identifiant national (ex: AB12345) : ")
        return last_name, first_name, birth_date, chess_id

    @staticmethod
    def show_players(players):
        if not players:
            print("\nAucun joueur enregistré pour le moment.")
            return

        print("\n--- Liste des joueurs ---")
        for player in players:
            print(f"{player.last_name} {player.first_name} "
                  f"- {player.chess_id} - {player.points} pts")

    @staticmethod
    def show_message(message):
        """Affiche un message générique (confirmation, erreur...)."""
        print(message)