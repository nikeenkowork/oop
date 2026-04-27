class Category:
    """
    Класс категории товаров.

    Содержит список товаров и методы для работы с ними.
    """

    category_count = 0  # общее количество категорий
    product_count = 0  # общее количество товаров

    def __init__(self, name, description, products):
        """
        Инициализация объекта категории.

        :param name: Название категории
        :type name: str
        :param description: Описание категории
        :type description: str
        :param products: Список товаров (объекты Product)
        :type products: list
        """
        self.name = name
        self.description = description

        # приватный список товаров
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """
        Добавляет товар в категорию и обновляет общий счётчик товаров.
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """
        Возвращает список товаров категории в виде строки.
        Формат:
        Название, цена руб. Остаток: количество шт.
        """
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

    def __str__(self):
        """
        Возвращает строковое представление категории.

        Формат:
        Название категории, количество продуктов: X шт.

        Где X — общее количество единиц товаров (quantity всех продуктов).
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
