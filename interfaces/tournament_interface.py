from abc import ABC, abstractmethod


class TournamentInterface(ABC):

    @abstractmethod
    def prompt_new_tournament(self):
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
        pass

    @abstractmethod
    def show_standings(self, players):

        pass

    @abstractmethod
    def show_message(self, message):
        pass

    @abstractmethod
    def show_tournament_menu(self, current_tournament):
        pass

    @abstractmethod
    def wait_for_enter(self):
        pass