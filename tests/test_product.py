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
