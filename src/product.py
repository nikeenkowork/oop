class Product:
    """
    Класс товара.
    """

    def __init__(self, name, description, price, quantity):
        """
        Инициализация товара.

        :param name: Название товара
        :param description: Описание товара
        :param price: Цена
        :param quantity: Количество на складе
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
