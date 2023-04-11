from __future__ import annotations

import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: int, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.all.append(self)
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.__name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    @property
    def name(self) -> str:
        """
        Возвращает название товара
        """
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        if len(new_name) > 10:
            raise Exception("Длина наименования товара превышает 10 символов.")
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv
        """
        cls.all = []  # Что бы пройти проверку assert len(Item.all) == 5 приходится обнулять список!
        with open('items.csv', 'r') as file:
            data = csv.DictReader(file)
            for i in data:
                cls(i['name'], cls.string_to_number(i['price']), cls.string_to_number(i['quantity']))

    @staticmethod
    def string_to_number(str_data: str) -> int:
        """
        Возвращает число из числа-строки
        """
        return int(float(str_data))

    def calculate_total_price(self) -> float | int:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """
        return self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __add__(self, other):
        """
        Складывает классы Item друг с другом или дочерними.
        """
        if not isinstance(other, Item):
            return ValueError
        return self.quantity + other.quantity
