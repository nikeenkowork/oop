class Category:
    """
    Класс категории товаров.
    Хранит список продуктов и статистику по категориям и товарам.
    """

    category_count = 0  # общее количество категорий
    product_count = 0  # общее количество товаров

    def __init__(self, name, description):
        """
        Инициализация категории.

        :param name: название категории
        :param description: описание категории
        """
        self.name = name
        self.description = description

        # 🔒 приватный список товаров
        self.__products = []

        Category.category_count += 1

    def add_product(self, product):
        """
        Добавляет объект Product в категорию.
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """
        Возвращает список товаров в виде строки.
        """
        if not self.__products:
            return "В категории нет товаров"

        result = ""
        for product in self.__products:
            result += (
                f"{product.name} | {product.price} руб. | {product.quantity} шт.\n"
            )

        return result.strip()
