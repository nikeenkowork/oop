class Product:
    """
    Класс товара.
    """

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.__price = price
        self.description = description
        self.quantity = quantity

    @property
    def price(self):
        """
        Геттер цены.
        """
        return self.__price

    @price.setter
    def price(self, value):
        """
        Сеттер цены с проверкой.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data, products_list):
        """
        Создаёт товар или обновляет существующий.

        :param product_data: словарь с данными товара
        :param products_list: список уже существующих товаров
        :return: объект Product
        """

        new_name = product_data["name"]
        new_price = product_data["price"]
        new_description = product_data["description"]
        new_quantity = product_data["quantity"]

        # 🔍 ищем дубликат
        for product in products_list:
            if product.name == new_name:

                # ➕ складываем количество
                product.quantity += new_quantity

                # ⚖️ выбираем большую цену
                if new_price > product.price:
                    product.price = new_price

                return product

        # ➕ если нет дубликата — создаём новый
        return cls(new_name, new_price, new_description, new_quantity)
