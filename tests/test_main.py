from app.main import Product, Category


def test_products_attributes():
    """
    Проверяет создание объектов Product и корректность их атрибутов.
    """
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5

    assert product2.name == "Iphone 15"
    assert product2.price == 210000.0
    assert product2.quantity == 8

    assert product3.name == "Xiaomi Redmi Note 11"
    assert product3.price == 31000.0
    assert product3.quantity == 14


def test_category1():
    """
    Проверяет первую категорию: создание, состав товаров и счётчики.
    """
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    assert category1.name == "Смартфоны"
    assert category1.description.startswith("Смартфоны")
    assert len(category1.products) == 3
    assert category1.category_count == 1
    assert category1.product_count == 3


def test_category2():
    """
    Проверяет вторую категорию и глобальные счётчики Category.
    """
    Category.category_count = 0
    Category.product_count = 0

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)

    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4]
    )

    assert category2.name == "Телевизоры"
    assert len(category2.products) == 1
    assert category2.products[0] == product4

    assert Category.category_count == 1
    assert Category.product_count == 1