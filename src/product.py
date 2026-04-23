class Product:
    """
    Класс товара.
    """

    def __init__(self, name, description, price, quantity):
        """
        Инициализация товара.

        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество на складе
        """
        self.name = name
        self.description = description
        self.__price = price  # приватный атрибут цены
        self.quantity = quantity

    @property
    def price(self):
        """
        Геттер цены товара.

        :return: текущая цена товара
        """
        return self.__price

    @price.setter
    def price(self, value):
        """
        Сеттер цены товара с проверкой.

        Если цена меньше или равна нулю,
        выводит сообщение и не изменяет значение.

        :param value: новая цена
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data):
        """
        Создаёт объект Product из словаря.
        """

        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )
