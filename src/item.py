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

    @property
    def name(self) -> str:
        """
        Возвращает название товара
        """
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        if len(new_name) > 10:
            print('Длина наименования товара превышает 10 символов')
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv
        """
        cls.all = []  # Что бы пройти проверку assert len(Item.all) == 5 приходится обнулять список!
        with open('../src/items.csv', 'r') as file:
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
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
