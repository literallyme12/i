from Thing import Thing
from Human import Human

class Weapon(Thing):
    __damage: int

    def __init__(self, weight: int, volume: int, price: int, name: str, damage: int):
        super().__init__(weight, volume, price, name)
        self.__damage = damage

    @property
    def damage(self):
        return self.__damage

    def give_damage(self, human: Human):
        human.get_damage(self.__damage)


class Medkit(Thing):
    __points: int

    def __init__(self, weight: int, volume: int, price: int, name: str, points: int):
        super().__init__(weight, volume, price, name)
        self.__points = points

    @property
    def points(self):
        return self.__points

    def give_heal(self, human: Human):
        human.get_healed(self.__points)
