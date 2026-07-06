from abc import ABC, abstractmethod


class ReportInterface(ABC):

    @abstractmethod
    def show_all_players_alpha(self, players):
        pass

    @abstractmethod
    def show_all_tournaments(self, tournaments_data):
        pass

    @abstractmethod
    def show_tournament_info(self, tournament):
        pass

    @abstractmethod
    def show_tournament_players_alpha(self, tournament):
        pass

    @abstractmethod
    def show_tournament_rounds_and_matches(self, tournament):
        pass

    @abstractmethod
    def prompt_select_tournament(self, tournaments_data):
        pass

    @abstractmethod
    def show_message(self, message):
        pass