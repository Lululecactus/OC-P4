from abc import ABC, abstractmethod


class MenuInterface(ABC):

    @abstractmethod
    def show_main_menu(self):
        pass    

    @abstractmethod
    def show_message(self, message):
        pass