import random


class Thing:
    __weight: int
    __volume: int
    __price: int
    __name: str

    def __init__(self, weight: int, volume: int, price: int, name: str):
        self.__weight = weight
        self.__price = price
        self.__volume = volume
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def volume(self):
        return self.__volume

    @property
    def weight(self):
        return self.__weight


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


class Warrior(Human):
    __weapon: Weapon | None

    @property
    def weapon(self):
        return self.__weapon

    def __init__(self, max_hp: int):
        super().__init__(max_hp)
        self.__weapon = None

    def pick_best_weapon(self):
        for i in range(len(self.inventory)):
            if isinstance(self.inventory[i], Weapon):
                if self.__weapon is None or self.__weapon.damage < self.inventory[i].damage:
                    self.__weapon = self.inventory[i]

    def give_damage(self, human: Human):
        if self.__weapon is not None:
            self.__weapon.give_damage(human)


class Healer(Human):
    __medkit: Medkit | None

    @property
    def medkit(self):
        return self.__medkit

    def __init__(self, max_hp: int):
        super().__init__(max_hp)
        self.__medkit = None

    def pick_best_weapon(self):
        for i in range(len(self.inventory)):
            if isinstance(self.inventory[i], Weapon):
                if self.__medkit is None or self.__medkit.points < self.inventory[i].points:
                    self.__medkit = self.inventory[i]

    def give_damage(self, human: Human):
        if self.__medkit is not None:
            self.__medkit.give_heal(human)


class Trader(Human):
    def __init__(self, max_hp: int):
        super().__init__(max_hp)
        self.__trading_store = []

    def show_trading_store(self):
        for i in self.__trading_store:
            print(i)

    def add_to_trading_list(self, item: Thing):
        if item in self.inventory:
            self.__trading_store.append(item)

    def delete_from_trading_store(self, item: Thing):
        if item in self.__trading_store:
            self.__trading_store.remove(item)

    def buy_in_trading_store(self, human: Human, item: Thing):
        if item not in self.__trading_store:
            return

        if human.cash < item.price:
            return

        if not self.drop(item):
            return

        if not human.pick_up(item):
            self.pick_up(item)
            return


        self.__trading_store.remove(item)
        self.cash += item.price
        human.cash -= item.price

    def sell_to_trader(self, human: Human, item:Thing):
        if self.cash < item.price:
            return

        if not human.drop(item):
            return

        if not self.pick_up(item):
            human.pick_up(item)
            return

        self.cash -= item.price
        human.cash += item.price


class Thief(Human):
    def steal(self, human: Human, item:Thing):
        if not human.drop(item):
            return

        i = random.randint(0,10)
        print(i)

        if i < 6:
            print('Украсть не удалось')
            human.pick_up(item)
            return

        if not self.pick_up(item):
            human.pick_up(item)
            return




























