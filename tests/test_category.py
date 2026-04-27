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


# -----------------------------
# ТЕСТЫ НА __str__
# -----------------------------


def test_product_str():
    """Проверка магического метода __str__ у Product"""
    product = Product("iPhone 15", "512GB", 210000, 8)

    expected = "iPhone 15, 210000 руб. (остаток: 8 шт.)"
    assert str(product) == expected


def test_category_str_empty():
    """Проверка __str__ у пустой категории"""
    category = Category("Смартфоны", "Описание", [])

    expected_result = "Смартфоны, количество продуктов: 0 шт."

    assert str(category) == expected_result


def test_category_str_with_products():
    """Проверка __str__ у категории с продуктами"""
    p1 = Product("A", "desc", 100, 2)
    p2 = Product("B", "desc", 200, 3)

    category = Category("Тест", "Описание", [p1, p2])

    expected = "Тест, количество продуктов: 5 шт."
    assert str(category) == expected
