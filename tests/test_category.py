from src.category import Category
from src.product import Product


def test_category_init():
    """
    Проверяет корректную инициализацию категории
    и обновление счётчиков.
    """
    Category.category_count = 0
    Category.product_count = 0

    products = [Product("A", "desc", 100, 2), Product("B", "desc", 200, 3)]

    category = Category("Phones", "Smartphones", products)

    assert category.name == "Phones"
    assert category.description == "Smartphones"
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_add_product():
    """
    Проверяет добавление товара в категорию
    и обновление общего счётчика товаров.
    """
    Category.product_count = 0

    category = Category("Phones", "Smartphones", [])

    product = Product("Test", "desc", 100, 1)

    category.add_product(product)

    assert Category.product_count == 1
    assert category.products == "Test, 100 руб. Остаток: 1 шт."


def test_products_property():
    """
    Проверяет корректный вывод списка товаров
    через property products.
    """
    products = [Product("A", "desc", 100, 2), Product("B", "desc", 200, 3)]

    category = Category("Phones", "Smartphones", products)

    result = category.products

    assert "A, 100 руб. Остаток: 2 шт." in result
    assert "B, 200 руб. Остаток: 3 шт." in result


def test_empty_category_products():
    """
    Проверяет поведение property products
    для пустой категории.
    """
    category = Category("Empty", "No products", [])

    assert category.products == ""
