from name_service import NameService
from abc import ABC, abstractmethod


class AbstractPokemon(NameService):
    def __init__(self):
        self._name = ""

    @property
    @abstractmethod
    def type1(self):
        pass

    @property
    @abstractmethod
    def type2(self):
        pass

    @property
    @abstractmethod
    def hp(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    def change_name(self, new_name):
        if new_name == "うんこ":
            print("不適切な名前です")
            return
        self._name = new_name
        
    def get_name(self):
        return self._name