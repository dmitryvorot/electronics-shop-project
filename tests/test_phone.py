import pytest

from src.phone import Phone


@pytest.fixture
def phone1():
    return Phone('Xiaomi', 15000, 3, 2)


def test_init(phone1):
    assert phone1.name == 'Xiaomi'
    assert phone1.price == 15000
    assert phone1.quantity == 3
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        Phone('Xiaomi', 15000, 3, 0)


def test_setter_number_of_sim(phone1):
    phone1.number_of_sim = 10
    assert phone1.number_of_sim == 10
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


def test_repr(phone1):
    assert phone1.__repr__() == "Phone('Xiaomi', 15000, 3, 2)"


def test_add(phone1):
    phone2 = Phone('Xiaomi', 15000, 5, 2)
    assert phone1 + phone2 == 8
    with pytest.raises(ValueError):
        phone1 + "Экземпляр класса str"

# pytest --cov --cov-report=html
