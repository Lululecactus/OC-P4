class TournamentView:

    @staticmethod
    def prompt_new_tournament():
        print("\n--- Créer un nouveau tournoi ---")
        name = input("Nom du tournoi : ")
        location = input("Lieu : ")
        start_date = input("Date de début (AAAA-MM-JJ) : ")
        end_date = input("Date de fin (AAAA-MM-JJ) : ")
        number_of_rounds = input("Nombre de tours (laisser vide = 4) : ")
        description = input("Description (optionnel) : ")
        return name, location, start_date, end_date, number_of_rounds, description

    @staticmethod
    def show_tournaments(tournaments_data):
        if not tournaments_data:
            print("\nAucun tournoi enregistré pour le moment.")
            return

        print("\n--- Liste des tournois ---")
        for t in tournaments_data:
            print(f"{t['name']} - {t['location']} "
                  f"({t['start_date']} -> {t['end_date']})")

    @staticmethod
    def prompt_select_tournament(tournaments_data):
        if not tournaments_data:
            print("\nAucun tournoi disponible.")
            return None

        print("\n--- Sélectionner un tournoi ---")
        for i, t in enumerate(tournaments_data, 1):
            print(f"{i}. {t['name']} ({t['start_date']})")

        choice = input("Numéro du tournoi (0 pour annuler) : ")
        if choice == "0" or not choice.isdigit():
            return None

        index = int(choice) - 1
        if 0 <= index < len(tournaments_data):
            return tournaments_data[index]["name"]
        return None

    @staticmethod
    def prompt_add_player(players):
        if not players:
            print("\nAucun joueur disponible.")
            return None

        print("\n--- Inscrire un joueur au tournoi ---")
        for i, player in enumerate(players, 1):
            print(f"{i}. {player.first_name} {player.last_name} "
                  f"({player.chess_id})")

        choice = input("Numéro du joueur (0 pour terminer) : ")
        if choice == "0" or not choice.isdigit():
            return None

        index = int(choice) - 1
        if 0 <= index < len(players):
            return players[index].chess_id
        return None

    @staticmethod
    def show_round(round_obj):
        print(f"\n--- {round_obj.name} ---")
        for i, match in enumerate(round_obj.matches, 1):
            p1, s1 = match.data[0]
            p2, s2 = match.data[1]
            print(f"{i}. {p1.first_name} {p1.last_name} "
                  f"vs {p2.first_name} {p2.last_name}")

    @staticmethod
    def prompt_match_result(match, match_number):
        p1 = match.data[0][0]
        p2 = match.data[1][0]
        print(f"\nMatch {match_number} : "
              f"{p1.first_name} {p1.last_name} "
              f"vs {p2.first_name} {p2.last_name}")
        print("1. Victoire joueur 1")
        print("2. Victoire joueur 2")
        print("0. Match nul")
        choice = input("Résultat : ")
        if choice in ["0", "1", "2"]:
            return int(choice)
        return 0

    @staticmethod
    def show_standings(players):
        print("\n--- Classement actuel ---")
        for i, player in enumerate(players, 1):
            print(f"{i}. {player.first_name} {player.last_name} "
                  f"- {player.points} pts")

    @staticmethod
    def show_message(message):
        print(message)