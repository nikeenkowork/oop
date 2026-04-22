from src.product import Product  # ✔ ОБЯЗАТЕЛЬНЫЙ импорт


def test_product_price_getter():
    """
    Проверка получения цены через property.
    """
    product = Product("Телефон", 1000, "desc", 5)

    assert product.price == 1000


def test_product_price_setter_valid():
    """
    Проверка установки корректной цены.
    """
    product = Product("Телефон", 1000, "desc", 5)

    product.price = 2000

    assert product.price == 2000


def test_product_price_setter_invalid():
    """
    Проверка, что отрицательная цена не изменяет значение.
    """
    product = Product("Телефон", 1000, "desc", 5)

    product.price = -500

    # цена должна остаться прежней
    assert product.price == 1000


def test_new_product_create():
    """
    Проверка создания нового товара через new_product.
    """
    products_list = []

    data = {"name": "Samsung", "price": 50000, "description": "Phone", "quantity": 3}

    product = Product.new_product(data, products_list)

    assert product.name == "Samsung"
    assert product.price == 50000
    assert product.quantity == 3


def test_new_product_update_existing():
    """
    Проверка обновления существующего товара (дубликат).
    """
    existing = Product("Samsung", 50000, "Phone", 3)
    products_list = [existing]

    data = {
        "name": "Samsung",
        "price": 60000,
        "description": "Phone updated",
        "quantity": 2,
    }

    product = Product.new_product(data, products_list)

    assert product.quantity == 5
    assert product.price == 60000
    assert product is existing
