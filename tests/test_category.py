from src.category_private import Category  # замени на свой модуль


class Product:
    """
    Простой тестовый класс товара.
    Используется только для проверки Category.
    """

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


def test_add_products_and_output():
    """
    Проверяет, что метод add_product добавляет товары,
    а property products возвращает корректную строку.
    """
    category = Category("Смартфоны", "Мобильные устройства")

    product1 = Product("iPhone", 1000, 5)
    product2 = Product("Samsung", 800, 3)

    category.add_product(product1)
    category.add_product(product2)

    expected = "iPhone | 1000 руб. | 5 шт.\n" "Samsung | 800 руб. | 3 шт."

    assert category.products == expected


def test_empty_category():
    """
    Проверяет поведение property products,
    когда в категории нет товаров.
    """
    category = Category("Тест", "Пустая категория")

    assert category.products == "В категории нет товаров"


def test_category_count():
    """
    Проверяет корректное увеличение счётчика категорий.
    """
    start = Category.category_count

    Category("A", "desc")
    Category("B", "desc")

    assert Category.category_count == start + 2


def test_product_count():
    """
    Проверяет корректное увеличение счётчика товаров
    при добавлении продуктов в категории.
    """
    start = Category.product_count

    category = Category("Категория", "Описание")

    category.add_product(Product("Test1", 10, 1))
    category.add_product(Product("Test2", 20, 2))

    assert Category.product_count == start + 2
