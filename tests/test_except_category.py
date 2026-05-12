from src.category import Category
from src.product import Product


def test_average_price():
    """
    Тест подсчёта средней цены товаров.
    """
    product1 = Product("Samsung", "Смартфон", 50000, 5)
    product2 = Product("iPhone", "Телефон", 100000, 3)

    category = Category("Смартфоны", "Мобильные телефоны", [product1, product2])

    assert category.average_price() == 75000


def test_average_price_empty_category():
    """
    Тест: если товаров нет, метод возвращает 0.
    """
    category = Category("Пустая категория", "Нет товаров", [])

    assert category.average_price() == 0
