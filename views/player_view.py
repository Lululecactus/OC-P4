from interfaces.player_interface import PlayerInterface


class PlayerView(PlayerInterface):

    def prompt_new_player(self):
        print("\n--- Ajouter un nouveau joueur ---")
        last_name = input("Nom de famille : ")
        first_name = input("Prénom : ")
        birth_date = input("Date de naissance (AAAA-MM-JJ) : ")
        chess_id = input("Identifiant national (ex: AB12345) : ")
        return last_name, first_name, birth_date, chess_id

    def show_players(self, players):
        if not players:
            print("\nAucun joueur enregistré pour le moment.")
            return
        print("\n--- Liste des joueurs ---")
        for player in players:
            print(f"{player.last_name} {player.first_name} "
                  f"- {player.chess_id} - {player.points} pts")

    def show_message(self, message):
        print(message)