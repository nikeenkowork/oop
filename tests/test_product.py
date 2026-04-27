import pytest

from src.product import Product


def test_product_initialization():
    """Проверяет корректную инициализацию объекта Product."""
    product = Product("Phone", "Smartphone", 1000, 5)

    assert product.name == "Phone"
    assert product.description == "Smartphone"
    assert product.price == 1000
    assert product.quantity == 5


def test_price_getter():
    """Проверяет корректную работу геттера price."""
    product = Product("Phone", "Smartphone", 1000, 5)

    assert product.price == 1000


def test_price_setter_valid():
    """Проверяет изменение цены на корректное значение через сеттер."""
    product = Product("Phone", "Smartphone", 1000, 5)

    product.price = 1500

    assert product.price == 1500


def test_price_setter_invalid(capsys):
    """
    Проверяет, что при установке некорректной цены:
    - выводится сообщение об ошибке
    - значение цены не изменяется
    """
    product = Product("Phone", "Smartphone", 1000, 5)

    product.price = -10

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 1000


def test_product_str():
    """
    Проверка магического метода __str__.

    Метод должен возвращать строку в формате:
    'Название, цена руб. Остаток: количество шт.'
    """
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    expected_result = "Iphone 15, 210000.0 руб. (остаток: 8 шт.)"

    assert str(product) == expected_result


def test_product_add():
    """
    Проверка магического метода __add__.

    Метод должен возвращать суммарную стоимость
    двух товаров на складе:
    price * quantity + price * quantity
    """
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB", 210000.0, 8)

    expected_result = (180000.0 * 5) + (210000.0 * 8)

    assert product1 + product2 == expected_result


def test_product_add_with_another_product():
    """
    Проверка __add__ на другой паре товаров.

    Тест подтверждает, что метод корректно работает
    независимо от конкретных значений объектов.
    """
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB", 31000.0, 14)

    expected_result = (180000.0 * 5) + (31000.0 * 14)

    assert product1 + product3 == expected_result


def test_product_add_invalid_type():
    """
    Проверка __add__ при передаче объекта неверного типа.

    Ожидается, что Python выбросит TypeError,
    так как метод возвращает NotImplemented.
    """
    product = Product("Iphone 15", "512GB", 210000.0, 8)

    with pytest.raises(TypeError):
        product + 100
