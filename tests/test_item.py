"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item('phone_test', 10000, 3)


def test_init(item1):
    assert item1.name == 'phone_test'
    assert item1.price == 10000
    assert item1.quantity == 3


def test_calculate_total_price(item1):
    item1.calculate_total_price()
    assert item1.price == 10000


def test_apply_discount(item1):
    item1.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000


def test_item_name(item1):
    item1.name = 'test_very_long_text'
    assert item1.name != 'test_very_long_text'
    item1.name = 'test_text'
    assert item1.name == 'test_text'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('123') == 123
    assert Item.string_to_number('12.3') == 12

# pytest --cov --cov-report=html
