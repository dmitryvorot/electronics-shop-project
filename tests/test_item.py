"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item('fixture_test', 10000, 3)


def test_init(item1):
    assert item1.name == 'fixture_test'
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
    with pytest.raises(Exception):
        item1.name = 'test_very_long_text'

    item1.name = 'test_text'
    assert item1.name == 'test_text'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('123') == 123
    assert Item.string_to_number('12.3') == 12


def test_repr(item1):
    assert item1.__repr__() == "Item('fixture_test', 10000, 3)"


def test_str(item1):
    assert item1.__str__() == "fixture_test"


def test_add(item1):
    data_int = 1000
    assert item1 + data_int == ValueError
    assert item1 + item1 == 6

# pytest --cov --cov-report=html
