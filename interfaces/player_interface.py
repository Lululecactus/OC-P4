from abc import ABC, abstractmethod


class PlayerInterface(ABC):

    @abstractmethod
    def prompt_new_player(self):
        pass

    @abstractmethod
    def show_players(self, players):
        pass

    @abstractmethod
    def show_message(self, message):
        pass

    @abstractmethod
    def show_player_menu(self):
        pass
