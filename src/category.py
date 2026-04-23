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

        :param product: Объект класса Product
        :type product: Product
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """
        Возвращает список товаров категории в виде форматированной строки.

        Каждый товар выводится в формате:
        Название продукта, цена руб. Остаток: количество шт.

        :return: Строка со списком товаров
        :rtype: str
        """
        result = []
        for product in self.__products:
            result.append(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            )
        return "\n".join(result)
