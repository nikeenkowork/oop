class Category:
    """
    Класс категории товаров.
    """

    category_count = 0  # общее количество категорий
    product_count = 0  # общее количество товаров

    def __init__(self, name, description, products):
        """
        Инициализация категории.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список товаров (объекты Product)
        """
        self.name = name
        self.description = description
        self.products = products

        # увеличиваем количество категорий
        Category.category_count += 1

        # увеличиваем общее количество товаров
        Category.product_count += len(products)
