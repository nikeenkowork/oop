class Product:
    """
    Базовый класс для представления товара.
    """

    def __init__(self, name, description, price, quantity):
        """
        Инициализирует объект товара.

        :param name: Название товара.
        :param description: Описание товара.
        :param price: Цена товара.
        :param quantity: Количество товара на складе.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """
        Возвращает цену товара.

        :return: Цена товара.
        """
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Устанавливает новую цену товара.

        :param new_price: Новое значение цены.
        """
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __str__(self):
        """
        Возвращает строковое представление товара.

        Формат:
        Название, X руб. (остаток: Y шт.)

        :return: Строковое представление товара.
        """
        return f"{self.name}, {self.price} руб. (остаток: {self.quantity} шт.)"

    def __add__(self, other):
        """
        Складывает два товара по общей стоимости на складе.

        Сложение возможно только для объектов одного класса.

        :param other: Второй товар
        :return: Общая стоимость
        :raises TypeError: если классы разные
        """
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")

        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """
    Класс для представления смартфона.
    Наследуется от класса Product.
    """

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        """
        Инициализирует объект смартфона.

        :param name: Название смартфона.
        :param description: Описание смартфона.
        :param price: Цена смартфона.
        :param quantity: Количество смартфонов на складе.
        :param efficiency: Производительность смартфона.
        :param model: Модель смартфона.
        :param memory: Объем встроенной памяти.
        :param color: Цвет смартфона.
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """
    Класс для представления газонной травы.
    Наследуется от класса Product.
    """

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        """
        Инициализирует объект газонной травы.

        :param name: Название травы.
        :param description: Описание травы.
        :param price: Цена травы.
        :param quantity: Количество упаковок на складе.
        :param country: Страна-производитель.
        :param germination_period: Срок прорастания.
        :param color: Цвет травы.
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
