"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item('phone_test', 10000, 3)


def test_item_init(item1):
    assert item1.name == 'phone_test'
    assert item1.price == 10000
    assert item1.quantity == 3


def test_item_calculate_total_price(item1):
    assert item1.price == 10000

def test_item_apply_discount(item1):
    item1.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000