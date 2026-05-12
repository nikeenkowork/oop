import pytest

from src.product import Product


def test_product_zero_quantity():
    """
    Тест: при количестве 0 должно возникать исключение.
    """
    with pytest.raises(ValueError):
        Product("iPhone 15", "Смартфон Apple", 120000, 0)


def test_product_negative_quantity():
    """
    Тест: при отрицательном количестве должно возникать исключение.
    """
    with pytest.raises(ValueError):
        Product("Xiaomi", "Смартфон Xiaomi", 40000, -1)
