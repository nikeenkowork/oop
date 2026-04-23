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
    def new_product(cls, product_data: dict, products_list: list):
        """
        Создаёт новый товар или обновляет существующий.

        Проверяет наличие товара с таким же названием
        в списке products_list:
        - если найден, увеличивает количество
          и устанавливает максимальную цену
        - если не найден, создаёт новый объект Product

        :param product_data: словарь с данными товара
        :param products_list: список существующих товаров
        :return: объект Product (новый или обновлённый)
        """

        # 🔍 поиск товара по имени
        for product in products_list:
            if product.name == product_data["name"]:
                # обновляем количество
                product.quantity += product_data["quantity"]

                # обновляем цену (берём максимальную)
                product.price = max(product.price, product_data["price"])

                return product

        # ❌ если товар не найден — создаём новый
        new_product = cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )

        return new_product
