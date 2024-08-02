from Human import Human
from WeaponMedkit import Weapon, Medkit


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

    def sell_to_trader(self, human: Human, item: Thing):
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
    def steal(self, human: Human, item: Thing):
        if not human.drop(item):
            return

        i = random.randint(0, 10)
        print(i)

        if i < 6:
            print('Украсть не удалось')
            human.pick_up(item)
            return

        if not self.pick_up(item):
            human.pick_up(item)
            return
