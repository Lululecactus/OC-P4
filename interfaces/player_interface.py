from abc import ABC, abstractmethod


class PlayerInterface(ABC):

    @abstractmethod
    def prompt_new_player(self):
        """Renvoie (last_name, first_name, birth_date, chess_id)."""
        pass

    @abstractmethod
    def show_players(self, players):
        pass

    @abstractmethod
    def show_message(self, message):
        pass