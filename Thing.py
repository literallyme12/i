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


