from re import findall
from math import pi


class Table:
    def __init__(self):
        self.table_type = Table.table_type_validator(input("Прямоугольный или квадратный L / круглый R"))

    def square(self):
        return float(self.w) * float(self.l)

    def user_input(self):
        self.zakaz_number = Table.zakaz_number_validator( input("Номер заказа"))
        self.zakaz_date = Table.date_validator(input("Дата заказа"))
        self.zakaz_deadline =Table.date_validator(input("Крайний срок сдачи  заказа"))

    @staticmethod
    def table_type_validator(s):
        if not isinstance(s, str) or len(s) != 1:
            raise TypeError("Должна быть одна буква L или R")
        return s

    @staticmethod
    def zakaz_number_validator(s):
        if (findall(r'\d{1,8}', s))[0] != s:
            raise TypeError("Должно быть от одной до 8 цифр")
        else:
            return s

    @staticmethod
    def date_validator(s):
        if (findall(r'\d{2}.\d{2}.\d{4}', s))[0] != s:
            raise TypeError("Дата должна быть в формате дд.мм.гггг")
        else:
            return s

class Table_rectangle(Table):
    def __init__(self):
        self.user_input()
        self.w = input("Введите Ширину стола")
        self.l = input("Введите длину cтола или [enter] если стол кавдратный")
        if self.l == "":
            self.l = self.w
            print(f"Стол квадратный {self.w}x{self.w}м")
        else:
            print(f"Стол прямоугольный {self.w}x{self.l}м")


class Table_circle(Table):

    def __init__(self):
        self.user_input()
        self.w = input("радиус круглого стола")
        self.l = float(self.w) * pi
        print(f"Стол круглый, радиус {self.w}м")


t = Table()
if t.table_type == "L" or t.table_type == "l":
    t = Table_rectangle()
    print("Площадь стола", t.square())
elif t.table_type == "R" or t.table_type == "r":
    t = Table_circle()
    print("Площадь стола", t.square())
else:
    print("Введено неверное значение")
