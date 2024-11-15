from pokemon import AbstractPokemon


class Pikachu(AbstractPokemon):
    def __init__(self, name, type1, type2, hp):
        self._name = name
        self._type1 = type1
        self._type2 = type2
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def type1(self):
        return self._type1

    @property
    def type2(self):
        return self._type2

    @property
    def hp(self):
        return self._hp

    def attack(self):
        return f"{self.name}の10万ボルト！"