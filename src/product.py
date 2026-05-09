from abc import ABC, abstractmethod


class PrintMixin:
    """
    Миксин для вывода информации о созданном объекте.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self):
        """
        Возвращает информацию о классе и параметрах объекта.
        """
        return f"{self.__class__.__name__}(" f"{self.__dict__}" f")"


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для всех товаров.
    """

    @property
    @abstractmethod
    def price(self):
        """
        Возвращает цену товара.
        """
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        """
        Устанавливает цену товара.
        """
        pass

    @abstractmethod
    def __str__(self):
        """
        Возвращает строковое представление товара.
        """
        pass

    @abstractmethod
    def __add__(self, other):
        """
        Складывает стоимость товаров.
        """
        pass


class Product(PrintMixin, BaseProduct):
    """
    Базовый класс для представления товара.
    """

    def __init__(self, name, description, price, quantity):
        """
        Инициализирует объект товара.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        super().__init__()

    @property
    def price(self):
        """
        Возвращает цену товара.
        """
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Устанавливает новую цену товара.
        """
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __str__(self):
        """
        Возвращает строковое представление товара.
        """
        return f"{self.name}, {self.price} руб. (остаток: {self.quantity} шт.)"

    def __add__(self, other):
        """
        Складывает два товара по общей стоимости на складе.
        """
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")

        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """
    Класс для представления смартфона.
    """

    def __init__(
        self,
        name,
        description,
        price,
        quantity,
        efficiency,
        model,
        memory,
        color,
    ):
        """
        Инициализирует объект смартфона.
        """
        super().__init__(name, description, price, quantity)

        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """
    Класс для представления газонной травы.
    """

    def __init__(
        self,
        name,
        description,
        price,
        quantity,
        country,
        germination_period,
        color,
    ):
        """
        Инициализирует объект газонной травы.
        """
        super().__init__(name, description, price, quantity)

        self.country = country
        self.germination_period = germination_period
        self.color = color
