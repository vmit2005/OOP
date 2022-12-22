import re


class Auto:
    def __init__(self, name, year, fabrik, power, color, price):
        self.name = name
        self.year = year
        self.fabrik = fabrik
        self.power = power
        self.color = color
        self.price = price

    def print_auto(self):
        print("******* Данные автомобилей *******")
        print(f"Название модели    : {reno.name}")
        print(f"Год выпуска        : {reno.year}")
        print(f"Производитель      : {reno.fabrik}")
        print(f"Мощность двигателя : {reno.power}")
        print(f"Цвет автомобиля    : {reno.color}")
        print(f"Цена               : {reno.price}")
        print("=================================")

    @staticmethod
    def verify_name(name):
        if not isinstance(name, str):
            raise TypeError("Название модели должно быть строкой")

    @staticmethod
    def verify_year(year):
        if re.findall(r"\d{4}", year)[0] != year:
            raise TypeError("Год выпуска должен быть 4 числа, без букв")

    @staticmethod
    def verify_fabrik(fabrik):
        if not isinstance(fabrik, str):
            raise TypeError("Название производителя должно быть строкой")
        if re.findall(r"\w{,20}", fabrik)[0] != fabrik:
            raise TypeError("Число букв не более 20")

    @staticmethod
    def verify_power(power):
        if not isinstance(power, int)or (30 > power or power >1000) : #
            raise TypeError("Мощность должна быть целым числом больше 30 и меньше 1000")

    @staticmethod
    def verify_color(color):
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        if re.findall(r"\w{,16}", color)[0] != color:
            raise TypeError("Число букв не более 16")

    @staticmethod
    def verify_price(price):
        pass
        if not isinstance(price, int) or (10000 > price and price < 100000000):
            raise TypeError("Цена должна быть целым числом больше 10 тыс и меньше 100 млн")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.verify_name(name)
        self.__name = name

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.verify_year(year)
        self.__year = year

    @property
    def fabrik(self):
        return self.__fabrik

    @fabrik.setter
    def fabrik(self, fabrik):
        self.verify_fabrik(fabrik)
        self.__fabrik = fabrik

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        self.verify_power(power)
        self.__power = power

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.verify_color(color)
        self.__color = color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.verify_price(price)
        self.__price = price


reno = Auto("Сандеро Степвей", "2020", "Рено", 113, "white", 200000)
print(reno.name)
print(reno.year)
print(reno.fabrik)
print(reno.power)
print(reno.color)
print(reno.price)
reno.print_auto()

