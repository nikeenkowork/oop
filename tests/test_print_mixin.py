from abc import ABC

import pytest

from src.product import BaseProduct, Product


def test_print_mixin_repr():
    """
    Проверка метода __repr__ у PrintMixin через Product.

    Убеждаемся, что строковое представление объекта
    содержит имя класса и его словарь атрибутов.
    """
    product = Product("Телефон", "Описание", 1000, 2)

    result = repr(product)

    assert "Product(" in result
    assert "Телефон" in result
    assert "quantity" in result


def test_print_mixin_output(capsys):
    """
    Проверка вывода PrintMixin при создании объекта.

    При инициализации Product должен выводиться repr объекта в консоль.
    """
    Product("Телефон", "Описание", 1000, 2)

    captured = capsys.readouterr()

    assert "Product(" in captured.out
    assert "Телефон" in captured.out


def test_base_product_is_abstract():
    """
    Проверка, что BaseProduct является абстрактным классом.
    """
    assert issubclass(BaseProduct, ABC)


def test_base_product_has_abstract_methods():
    """
    Проверка наличия обязательных абстрактных методов в BaseProduct.
    """
    methods = BaseProduct.__abstractmethods__

    assert "price" in methods
    assert "__str__" in methods
    assert "__add__" in methods


def test_product_inherits_base_product():
    """
    Проверка наследования Product от BaseProduct.
    """
    product = Product("Телефон", "Описание", 1000, 2)

    assert isinstance(product, BaseProduct)


def test_product_price_property():
    """
    Проверка работы property price.
    """
    product = Product("Телефон", "Описание", 1000, 2)

    assert product.price == 1000


def test_product_price_setter():
    """
    Проверка установки новой цены через setter.
    """
    product = Product("Телефон", "Описание", 1000, 2)

    product.price = 2000

    assert product.price == 2000


def test_product_price_negative(capsys):
    """
    Проверка обработки некорректной цены.

    При установке отрицательной цены выводится сообщение,
    а значение не изменяется.
    """
    product = Product("Телефон", "Описание", 1000, 2)

    product.price = -10
    captured = capsys.readouterr()

    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 1000


def test_product_str():
    """
    Проверка строкового представления Product.
    """
    product = Product("Телефон", "Описание", 1000, 2)

    result = str(product)

    assert "Телефон" in result
    assert "1000" in result
    assert "2" in result


def test_product_add():
    """
    Проверка сложения стоимости товаров одного класса.
    """
    p1 = Product("Телефон", "Описание", 1000, 2)
    p2 = Product("Телефон", "Описание", 500, 3)

    result = p1 + p2

    assert result == (1000 * 2 + 500 * 3)


def test_product_add_different_classes():
    """
    Проверка запрета сложения объектов разных классов.
    """

    class FakeProduct(Product):
        pass

    p1 = Product("Телефон", "Описание", 1000, 2)
    p2 = FakeProduct("Телефон", "Описание", 1000, 2)

    with pytest.raises(TypeError):
        p1 + p2
