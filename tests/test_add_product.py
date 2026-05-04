import pytest

from src.product import LawnGrass, Product, Smartphone


def test_smartphone_fields():
    """
    Проверяет корректность инициализации всех полей класса Smartphone,
    включая поля родительского класса Product и собственные атрибуты.
    """
    s = Smartphone(
        name="iPhone",
        description="Apple phone",
        price=1000,
        quantity=5,
        efficiency="A16",
        model="15 Pro",
        memory=256,
        color="black",
    )

    assert s.name == "iPhone"
    assert s.description == "Apple phone"
    assert s.price == 1000
    assert s.quantity == 5

    assert s.efficiency == "A16"
    assert s.model == "15 Pro"
    assert s.memory == 256
    assert s.color == "black"


def test_lawn_grass_fields():
    """
    Проверяет корректность инициализации всех полей класса LawnGrass,
    включая атрибуты родительского класса Product и специфичные поля.
    """
    g = LawnGrass(
        name="Green Grass",
        description="Soft lawn grass",
        price=50,
        quantity=10,
        country="Netherlands",
        germination_period="7 days",
        color="green",
    )

    assert g.name == "Green Grass"
    assert g.description == "Soft lawn grass"
    assert g.price == 50
    assert g.quantity == 10

    assert g.country == "Netherlands"
    assert g.germination_period == "7 days"
    assert g.color == "green"


def test_add_different_classes_product_smartphone():
    """
    Проверяет, что нельзя складывать объекты разных классов.

    Ожидается исключение TypeError.
    """
    p = Product("A", "desc", 100, 2)
    s = Smartphone("Phone", "desc", 1000, 1, 90, "X", 128, "black")

    with pytest.raises(TypeError):
        p + s


def test_add_different_classes_smartphone_grass():
    """
    Проверяет запрет сложения Smartphone и LawnGrass.

    Метод __add__ должен выбрасывать TypeError.
    """
    s = Smartphone("Phone", "desc", 1000, 1, 90, "X", 128, "black")
    g = LawnGrass("Grass", "desc", 50, 10, "USA", "7 days", "green")

    with pytest.raises(TypeError):
        s + g


def test_add_with_subclass_fails():
    """
    Проверяет, что наследники считаются разными классами.

    Используется строгое сравнение type(), поэтому
    даже наследник Smartphone не должен складываться.
    """

    class MySmartphone(Smartphone):
        pass

    s1 = Smartphone("Phone", "desc", 1000, 1, 90, "X", 128, "black")
    s2 = MySmartphone("Phone2", "desc", 1000, 1, 90, "Y", 128, "black")

    with pytest.raises(TypeError):
        s1 + s2
