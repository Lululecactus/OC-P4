from abc import ABC, abstractmethod


class TournamentInterface(ABC):

    @abstractmethod
    def prompt_new_tournament(self):
        """Renvoie (name, location, start_date, end_date,number_of_rounds, description)."""
        pass

    @abstractmethod
    def show_tournaments(self, tournaments_data):
        pass

    @abstractmethod
    def prompt_select_tournament(self, tournaments_data):
        pass

    @abstractmethod
    def prompt_add_player(self, players):
        pass

    @abstractmethod
    def show_round(self, round_obj):
        pass

    @abstractmethod
    def prompt_match_result(self, match, match_number):
        """Renvoie 0, 1 ou 2."""
        pass

    @abstractmethod
    def show_standings(self, players):

        pass

    @abstractmethod
    def show_message(self, message):
        pass