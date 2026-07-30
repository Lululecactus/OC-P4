from models.tournament import Tournament
from models.round import Round
from models.match import Match
from models.tournament_storage import TournamentStorage
from models.player_storage import PlayerStorage
from interfaces.tournament_interface import TournamentInterface
from constants import (
    TOURNAMENT_CREATE,
    TOURNAMENT_LOAD,
    TOURNAMENT_ADD_PLAYERS,
    TOURNAMENT_START_ROUND,
    TOURNAMENT_RECORD_RESULTS,
    TOURNAMENT_STANDINGS,
    TOURNAMENT_BACK,
)
from utils import clear_screen
from datetime import datetime


def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


class TournamentController:

    def __init__(self, view: TournamentInterface):
        self.view = view
        self.storage = TournamentStorage()
        self.player_storage = PlayerStorage()
        self.current_tournament = None

    def _get_players_dict(self):
        players = self.player_storage.load()
        return {p.chess_id: p for p in players}

    def create_tournament(self):
        (name, location, start_date, end_date,
         number_of_rounds, description) = self.view.prompt_new_tournament()

        if not is_valid_date(start_date):
            self.view.show_message(
                "Date de début invalide. Format attendu : AAAA-MM-JJ."
            )
            return

        if not is_valid_date(end_date):
            self.view.show_message(
                "Date de fin invalide. Format attendu : AAAA-MM-JJ."
            )
            return

        rounds = int(number_of_rounds) if number_of_rounds.isdigit() else 4

        tournament = Tournament(
            name=name,
            location=location,
            start_date=start_date,
            end_date=end_date,
            number_of_rounds=rounds,
            description=description,
        )
        self.storage.save(tournament)
        self.current_tournament = tournament
        self.view.show_message(
            f"Tournoi '{name}' créé et sauvegardé avec succès."
        )

    def add_players_to_tournament(self):
        if not self.current_tournament:
            self.view.show_message(
                "Aucun tournoi sélectionné. "
                "Créez ou chargez un tournoi d'abord."
            )
            return

        players_dict = self._get_players_dict()
        already_in = [p.chess_id for p in self.current_tournament.players]
        available = [
            p for p in players_dict.values()
            if p.chess_id not in already_in
        ]

        while True:
            chess_id = self.view.prompt_add_player(available)
            if chess_id is None:
                break
            player = players_dict[chess_id]
            self.current_tournament.add_player(player)
            available = [p for p in available if p.chess_id != chess_id]
            self.storage.save(self.current_tournament)
            self.view.show_message(
                f"{player.first_name} {player.last_name} inscrit(e)."
            )

    def start_next_round(self):
        if not self.current_tournament:
            self.view.show_message("Aucun tournoi sélectionné.")
            return

        t = self.current_tournament

        if t.is_finished():
            self.view.show_message(
                "Ce tournoi est terminé. Tous les tours ont été joués."
            )
            return

        if len(t.players) < 2:
            self.view.show_message(
                "Il faut au moins 2 joueurs pour lancer un tour."
            )
            return

        t.current_round += 1
        round_name = f"Round {t.current_round}"
        round_obj = Round(round_name)

        if t.current_round == 1:
            pairs = t.generate_round_pairs_random()
        else:
            pairs = self._generate_pairs_by_score(t)

        for p1, p2 in pairs:
            match = Match(p1, p2)
            round_obj.add_match(match)

        t.rounds.append(round_obj)
        self.storage.save(t)
        self.view.show_message(f"\n{round_name} lancé !")
        self.view.show_round(round_obj)

    def _generate_pairs_by_score(self, tournament):
        played = set()
        for round_obj in tournament.rounds:
            for match in round_obj.matches:
                id1 = match.data[0][0].chess_id
                id2 = match.data[1][0].chess_id
                played.add(tuple(sorted([id1, id2])))

        sorted_players = sorted(
            tournament.players,
            key=lambda p: p.points,
            reverse=True
        )

        pairs = []
        remaining = sorted_players.copy()

        while len(remaining) >= 2:
            player1 = remaining.pop(0)
            opponent = None

            for candidate in remaining:
                pair_key = tuple(sorted(
                    [player1.chess_id, candidate.chess_id]
                ))
                if pair_key not in played:
                    opponent = candidate
                    break

            if opponent is None:
                opponent = remaining[0]

            remaining.remove(opponent)
            pairs.append((player1, opponent))

        return pairs

    def record_round_results(self):
        if not self.current_tournament:
            self.view.show_message("Aucun tournoi sélectionné.")
            return

        t = self.current_tournament

        if not t.rounds:
            self.view.show_message(
                "Aucun tour lancé. Lancez un tour d'abord."
            )
            return

        current_round = t.rounds[-1]

        if current_round.end_datetime is not None:
            self.view.show_message(
                "Les résultats de ce tour ont déjà été enregistrés."
            )
            return

        for i, match in enumerate(current_round.matches, 1):
            result = self.view.prompt_match_result(match, i)
            match.set_result(result)

        current_round.close()
        self.storage.save(t)
        self.view.show_standings(
            sorted(t.players, key=lambda p: p.points, reverse=True)
        )
        self.view.show_message("\nTour terminé et sauvegardé.")

    def load_existing_tournament(self):
        tournaments_data = self.storage.load_all()
        name = self.view.prompt_select_tournament(tournaments_data)

        if name is None:
            return

        players_dict = self._get_players_dict()
        tournament = self.storage.load(name, players_dict)

        if tournament:
            self.current_tournament = tournament
            self.view.show_message(
                f"Tournoi '{name}' chargé. "
                f"Tour actuel : {tournament.current_round}/"
                f"{tournament.number_of_rounds}"
            )
        else:
            self.view.show_message("Tournoi introuvable.")

    def show_current_standings(self):
        if not self.current_tournament:
            self.view.show_message("Aucun tournoi sélectionné.")
            return

        ranked = sorted(
            self.current_tournament.players,
            key=lambda p: p.points,
            reverse=True
        )
        self.view.show_standings(ranked)

    def tournament_menu(self):
        while True:
            clear_screen()
            choice = self.view.show_tournament_menu(self.current_tournament)

            if choice == TOURNAMENT_CREATE:
                self.create_tournament()
            elif choice == TOURNAMENT_LOAD:
                self.load_existing_tournament()
            elif choice == TOURNAMENT_ADD_PLAYERS:
                self.add_players_to_tournament()
            elif choice == TOURNAMENT_START_ROUND:
                self.start_next_round()
            elif choice == TOURNAMENT_RECORD_RESULTS:
                self.record_round_results()
            elif choice == TOURNAMENT_STANDINGS:
                self.show_current_standings()
            elif choice == TOURNAMENT_BACK:
                break
            else:
                self.view.show_message("Choix invalide.")
