from enum import Enum


class CharacterClass(Enum):
    Amazon = 0
    Sorceress = 1
    Necromancer = 2
    Paladin = 3
    Barbarian = 4
    Druid = 5
    Assassin = 6
    Warlock = 7

    def __str__(self):
        return self.name

    @classmethod
    def from_id(cls, id):
        try:
            return cls(id)
        except ValueError:
            return None
