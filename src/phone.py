from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim: int):
        super().__init__(name, price, quantity)
        if not number_of_sim > 0 or isinstance(number_of_sim, float):
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        """
        Сеттер для проверки корректности количества SIM-карт.
        """
        if not new_number_of_sim > 0 or isinstance(new_number_of_sim, float):
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = new_number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other: Item):
        """
        Метод для сложения классов Phone и Item.
        """
        if not isinstance(other, Item):
            raise ValueError
        return self.quantity + other.quantity
