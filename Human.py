from Thing import Thing


class Human:
    __hp: int
    __cash: int = 0
    __inventory: list[Thing]
    __max_hp: int
    __max_weight: int
    __max_inventory_size: int

    def __init__(self, max_hp: int):
        self.__hp = max_hp
        self.__inventory = []

    @property
    def inventory(self):
        return self.__inventory.copy()

    @property
    def hp(self):
        return self.__hp

    @property
    def weight(self):
        w = 0
        for i in range(len(self.__inventory)):
            w += self.__inventory[i].weight

        return w

    @property
    def cash(self):
        return self.__cash

    @cash.setter
    def cash(self, value):
        self.__cash = value

    def get_healed(self, points):
        self.__hp += points

    def get_damage(self, points):
        self.__hp -= points

    def pick_up(self, item: Thing):
        if item.weight + self.weight > self.__max_weight:
            return False

        self.__inventory.append(item)
        return True

    def drop(self, item: Thing):
        if item in self.__inventory:
            self.__inventory.remove(item)
            return True
        return False