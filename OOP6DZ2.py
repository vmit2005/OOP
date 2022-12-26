import re
from math import pi

class Table:
    def __init__(self):
        self.zakaz_number=input("Номер заказа")
        self.zakaz_date = input("Дата заказа")
        self.zakaz_deadline = input("Крайний срок сдачи  заказа")
        self.table_type=input("Прямоугольный L / круглый R")

    def square(self):
        return float(self.w) * float(self.l)




class Table_rectangle():
    # def __init__(self,zakaz_number,zakaz_date,zakaz_deadline,table_type):
    def __init__(self):
        # self.zakaz_number=zakaz_number
        # self.zakaz_date=zakaz_date
        # self.zakaz_deadline=zakaz_deadline
        # self.table_type=table_type
        self.w = input("Ширина стола")
        self.l=input("Длина тола")


def square(self):
        return float(self.w)*float(self.l)

class Table_circle(Table):
    def __init__(self,n,d1,d2):
        self.zakaz_number = n
        self.zakaz_date = d1
        self.zakaz_deadline = d2
        self.r = input("радиус круглого стола")



    def sguare(self):
        return pi*float(self.r)**2




t1=Table()
t1=Table_rectangle()
print(t1.table_type)

