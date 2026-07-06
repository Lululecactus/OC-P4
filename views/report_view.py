class ReportView:

    @staticmethod
    def show_all_players_alpha(players):
        print("\n=== Rapport : tous les joueurs ===")
        if not players:
            print("Aucun joueur enregistré.")
            return
        for player in sorted(players, key=lambda p: p.last_name):
            print(f"{player.last_name} {player.first_name} "
                  f"- {player.chess_id}")

    @staticmethod
    def show_all_tournaments(tournaments_data):
        print("\n=== Rapport : tous les tournois ===")
        if not tournaments_data:
            print("Aucun tournoi enregistré.")
            return
        for t in tournaments_data:
            print(f"{t['name']} - {t['location']} "
                  f"({t['start_date']} -> {t['end_date']})")

    @staticmethod
    def show_tournament_info(tournament):
        print("\n=== Rapport : informations du tournoi ===")
        print(f"Nom      : {tournament.name}")
        print(f"Lieu     : {tournament.location}")
        print(f"Début    : {tournament.start_date}")
        print(f"Fin      : {tournament.end_date}")
        print(f"Tours    : {tournament.current_round}/"
              f"{tournament.number_of_rounds}")
        print(f"Description : {tournament.description}")

    @staticmethod
    def show_tournament_players_alpha(tournament):
        print(f"\n=== Rapport : joueurs de '{tournament.name}' ===")
        if not tournament.players:
            print("Aucun joueur inscrit.")
            return
        for player in sorted(tournament.players, key=lambda p: p.last_name):
            print(f"{player.last_name} {player.first_name} "
                  f"- {player.chess_id} - {player.points} pts")

    @staticmethod
    def show_tournament_rounds_and_matches(tournament):
        print(f"\n=== Rapport : tours et matchs de '{tournament.name}' ===")
        if not tournament.rounds:
            print("Aucun tour joué.")
            return
        for round_obj in tournament.rounds:
            print(f"\n{round_obj.name}")
            print(f"  Début : {round_obj.start_datetime}")
            print(f"  Fin   : {round_obj.end_datetime}")
            for match in round_obj.matches:
                p1, s1 = match.data[0]
                p2, s2 = match.data[1]
                print(f"  {p1.first_name} {p1.last_name} ({s1}) "
                      f"vs {p2.first_name} {p2.last_name} ({s2})")

    @staticmethod
    def prompt_select_tournament(tournaments_data):
        if not tournaments_data:
            print("Aucun tournoi disponible.")
            return None

        print("\nChoisir un tournoi :")
        for i, t in enumerate(tournaments_data, 1):
            print(f"{i}. {t['name']}")

        choice = input("Numéro (0 pour annuler) : ")
        if choice == "0" or not choice.isdigit():
            return None

        index = int(choice) - 1
        if 0 <= index < len(tournaments_data):
            return tournaments_data[index]["name"]
        return None

    @staticmethod
    def show_message(message):
        print(message)