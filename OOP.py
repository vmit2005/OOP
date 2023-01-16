# class Point:
#     """
#     Класс для представления координат точек на плоскости
#     """
#     x=1
#     y=1
#
#
# # print(Point.__doc__)
# # print(Point.__name__)
# # print(dir(Point))
#
#
# p1=Point()
# print(type(p1))
# print(p1.x)
# p1.x=100
# print(p1.x)
# print(Point.x)
# p2=Point()
# p2.x=200
# print(p2.x)
# print(id(p1))
# print(id(p2))
# print(id(Point))
# Point.y=300
# print(id(p1.y))
# print(id(p2.y))
# print(id(Point.y))
#
# class Point:
#     """
#     Класс для представления координат точек на плоскости
#     """
#     x=1
#     y=1
#
# p1=Point()
# print(p1.x,p1.y)
# p1.x=5
# p1.y=10
# print(p1.x,p1.y)
# print(p1.__dict__)
# print(p1.__dir__())
# p1.z=20
# Point.z=50
# print(p1.__dict__)
# print (Point.__dict__)
#
#
# class Point:
#     """
#     Класс для представления координат точек на плоскости
#     """
#     x=1
#     y=1
#
#     def set_coord(self):
#         print("Метод set_coord")
#         print(self.__dict__)
#
#
# p1=Point()
# print(p1.x)
#
# p1.set_coord()
# Point.set_coord(p1)
# p1.x=5
# p1.y=10
# p1.set_coord()
# class Point:
#     """
#      Класс для представления координат точек на плоскости
#      """
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         print("Метод set_coord")
#         print(self.__dict__)
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.set_coord(5, 10)
# print(p1.__dict__)
# p2 = Point()
# p2.set_coord(8, 17)
# print(p2.__dict__)
# print(p2.x)
# Point.set_coord(p2,7,14)
# print(p2.x)
import asyncio
import math


# class Humam:
#     name='name'
#     birthday='day'
#     phone='phone'
#     country='country'
#     city='city'
#     adress='ctreet,house'
#
#
#     def print_info(self):
#         print("пЕПерсональные данные".center(40,"*"))
#         print(f"Имя {self.name}\nДата рождения {self.birthday}\nНомер телефона{self.phone}\nCтрана{self.country}\nГород{self.city}\nАдресс {self.adress}")
#
#
#     def input_info(self,first_name,birthday,phone,country,city,adress):
#         self.name=first_name
#         self.birthday=birthday
#         self.phone=phone
#         self.country=country
#         self.city=city
#         self.adress=adress
#
#     def set_name(self,name):
#         if isinstance(name,str):
#             self.name=name
#
#     def get_name(self):
#         return self.name
#
#     def set_birthday(self,birthday):
#         self.birthday=birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#     def set_phone(self,phone):
#         self.phone=phone
#
#     def get_phone(self):
#         return self.phone
#
#     def set_country(self,country):
#         self.country=country
#
#     def get_country(self):
#         return self.country
#
#     def set_city(self,city):
#         self.city=city
#
#     def get_city(self):
#         return self.city
#
#     def set_adress(self,adress):
#         self.adress=adress
#
#     def get_adress(self):
#         return self.adress
#
#
#
#
# h1=Humam()
# h1.print_info()
# h1.input_info("Юля","23.05.1986","45-46-98","Россия","Москва","Чистопрудный бульвар 6 ")
# h1.print_info()
# h1.set_name("Алевтина")
# h1.print_info()
# print(h1.get_name())
# h1.set_birthday('28:11:1976')
# print(h1.get_birthday())

# class Person:
#     skill=10
#
#     def __init__(self,name,surname):
#         self.name = name
#         self.surname=surname
#
#
#     def print_info(self):
#         print("Данные сотрудника",self.name,self.surname)
#
#     def add_skill(self,k):
#         self.skill+=k
#         print("Rdfkbabrfwbz сотрудника",self.skill,"\n")
#
# p1=Person("Viktor","Reznik")
# p1.print_info()
# p1.add_skill(3)
# p1.add_skill(3)
#
# p2=Person("Anna","Dolgih")
# p2.print_info()
# p2.add_skill(2)

# class Point:
#     def __new__(cls, *args, **kwargs):
#         print("Конструктор")
#         return super().__new__(cls)
#
#     def __init__(self, x, y):
#         print("Инициализатор")
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print("Удаление экземпляра",self, self.__class__.__name__)
#
#     def print_coords(self):
#         print(f"x={self.x}y={self.y}")
#
#
# p1 = Point(5, 10)
# p1.print_coords()
#
#
# p2 = Point(5, 10)
# p2.print_coords()
# print(id(p1),id(p2))
# p2=0

# /

#
# a=0
# class Point:
#     count=0
#
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         Point.count+=1
#
#
# p1=Point(5,10)
# print(p1.count)
# p2=Point(7,2)
# print(p2.count)
# p3=Point(3,4)
# print(p3.count)
# print(p1.count)
# print(id(p1.count),id(p2.count),id(p3.count))

#
#
# class Robot():
#     k=0
#     def __init__(self,name):
#         self.name=name
#         print(f"Инициализау=ция{self.name}")
#         Robot.k+=1
#         print(f"Число работающих роботов{self.k}")
#
#     def __del__(self):
#         print(self.name,"Выключается")
#         Robot.k-=1
#
#         if Robot.k==0 :
#             print(f"{self.name}был последним")
#         else:
#             print(f"Число работающих роботов осталось {Robot.k}")
#
#     def sey_hi(self):
#         print(f"Привет! Меня зовут{self.name}")
#
#
# droid1=Robot("R2-D2")
# droid1.sey_hi()
# droid2=Robot("C-3PO")
# droid2.sey_hi()
# droid3=Robot("H1-0")
# droid3.sey_hi()
# print("Роботы закончили работу.Давайте их выключим")
# del droid1
# del droid2
# del droid3
# print(f"Число работающих роботов {Robot.k}")4
# import  turtle
# class Point:
#     __slots__ = ["__x","__y","z"]
#         if Point.__check_value(x) and Point.__check_value(y):
#              self.__x=x
#              self.__y=y
#
#     def __check_value(z):
#         if (isinstance(z,int) or isinstance(z,float)):
#             return True
#         return False
#
#     def set_coord(self,x,y):
#         if Point.__check_value(x) and Point.__check_value(y):
#              self.__x=x
#              self.__y=y
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coord_x(self, x, ):
#         if Point.__check_value(x) :
#             self.__x = x
#
#         else:
#             print("Координаты должны быть числами")
#
#     def  set_coord_y(self, y ):
#         if Point.__check_value(y):
#             self.__y = x
#
#         else:
#             print("Координаты должны быть числами")
#
# def get_coord(self):
#         return self.__x, self.__y
#
# p1=Point(5,10)
# p1.z=15
# # print(p1.__x,p1.__y)
# p1.__x=100
# # p1.__y="abc"
# # # print(p1.x,p1.y)
# # # public (self.x)- публичное свойставо
# # # protected(self._x)  -используется при наследовании
# # # private (self.__x)  - закрытые свойства
# # print(p1.__dict__)
# # # print(p1.get_coord())
# # p1.set_coord(2,5.8)
# # # print(p1.get_coord())
# # p1.set_coord_x(11)
# # # print(p1.get_coord())
# print(p1.__dict__)
#
#
# class Point:
#     def __init__(self,x=0,y=0):
#         self.x=x
#         self.y=y
#     def __set_x(self,x):
#         print("ВЫзов  set_x")
#         self.__x=x
#
#     def __get_x(self):
#         print("ВЫзов  get_x")
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # coord_x=property(__get_x, __set_x,__del_x)
# #     x=property(__get_x, __set_x,__del_x)
#
# p1=Point(5,10)
# p1.coord_x=100
# print(p1.__dict__)
# print(p1.coord_x)
# del p1.coord_x

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#
#     @property
#     def x(self, x): #__get_x
#         print("ВЫзов  get_x")
#         return self.__x
#
#
#     @x.setter
#     def x(self, x):
#         print("ВЫзов  set_x")
#         self.__x = x
#
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#
# # coord_x=property(__get_x, __set_x,__del_x)
# # x = property(__get_x, __set_x, __del_x)
#
# p1 = Point(5, 10)
# p1.coord_x = 100
# print(p1.__dict__)
# print(p1.coord_x)
# del p1.coord_x
#
#
# class kGToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print('Килограммы задаются тоько числами')
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = kGToPounds(12)
# print(weight.kg, "Кг=>", end=" ")
# print(weight.to_pounds(), "Фунтов")
# weight.kg = 41
# print(weight.kg, "Кг=>", end=" ")
# print(weight.to_pounds(), "Фунтов")
#
#
# class Person():
#
#     def __init__(self,name,skill):
#         self.__name = name
#         self.__skill=skill
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,name2):
#         self.__name=name2
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def skill(self):
#         return self.__skill
#
#     @skill.setter
#     def skill(self, skill2):
#         self.__skill = skill2
#
#     @skill.deleter
#     def skill(self):
#         del self.__skill
#
#
# p1=Person("Viktor",12)
#
# print(p1.name,p1.skill)
# p1.name="Anna "
# p1.skill=13
# print(p1.name,p1.skill)
# del p1.name
# print(p1)
#
# class Point:
#     __count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point(5, 10)
# p2 = Point(4, 8)
# p3 = Point(2, 17)
# print(Point.get_count())
# print(p1.get_count())
#
#
#
# class Change:
#     @staticmethod
#     def inc(x):
#         return x+1
#
#     @staticmethod
#     def dec(x):
#         return x-1
#
# print(Change.inc(10),Change.dec(10))
#
#
# s=(3,5,7,9)
# class Args:
#     @staticmethod
#     def max(a,b,c,d):
#
#         max=0
#         for i in a,b,c,d:
#             max=(max if i <max else i)
#         return max
#
#     @staticmethod
#     def min(a,b,c,d):
#
#         min=100
#         for i in a,b,c,d:
#             min=(min if i >  min else i)
#         return min
#
#     @staticmethod
#     def arf(a,b,c,d):
#
#         sum=(a+b+c+d)/4
#         return sum
#
#     @staticmethod
#     def factorial(x):
#         first=1
#         for i  in range(1,x+1):
#             first*=i
#         return first
#
# print(Args.max(3,5,7,9))
# print(Args.min(3,5,7,9))
# print(Args.arf(3,5,7,9))
# print(Args.factorial(7))

# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))
#         date1 = cls(day, month, year)
#         return date1
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# string_date = Date.from_string("23.10.2022")
# print(string_date.string_to_db())
# string_date1 = Date.from_string("21.12.2022")
# print(string_date1.string_to_db())
#
#
#
# class Account:
#     suffix = "RUB"
#     suffix_usd = 'USD'
#     suffix_eur = "EUR"
#     rate_usd = 0.013
#     rate_eur = 0.011
#
#     def __init__(self, num, surname, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname}  был открыт")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*"*50)
#         print(f"Cчет #{self.num} принадлежащий {self.surname} ,был закрыт")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете")
#         print("*" * 50)
#         print(f"{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("*" * 50)
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val}{Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val}{Account.suffix_usd}')
#
#     def edit_owner(self,surname):
#         self.surname=surname
#
#     def add_percennts(self):
#         self.value+=self.value*self.percent
#         print('Проценты были начислены')
#         self.print_balance()
#
#     def withdraw_money(self,val):
#         if val>self.value :
#             print(f"К сожалению у Вас нет  {val} {Account.suffix}")
#         else :
#             self.value-=val
#             print(f'{val}{Account.suffix} ,были успешно сняты')
#         self.print_balance()
#
#     def add_money(self,val):
#         self.value+=val
#         print(f'{val}{Account.suffix} ,были успешно добавлены')
#         self.print_balance()
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# acc.add_percennts()
# print()
# acc.withdraw_money(30000)
# acc.withdraw_money(100)
# acc.add_money(5000)
# acc.withdraw_money(3000)
#
#
#
#
# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО не является строкой")
#         f = fio.split()
#         print(f)
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters ="".join(re.findall('[a-zа-яё-]', fio, flags=re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) !=0:
#                 raise TypeError("В ФИО можжно использовать буквы и дефис")
#         print(letters)
#
#
#     @staticmethod
#     def verify_old(old):
#             if not isinstance(old,int) or old<14 or old>120:
#                 raise TypeError("ВОзраст должен быть числом в диапазоне от 14 до 120 лет")
#
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w,float) or w<20:
#             raise TypeError ('Вес ддолжен быть вещественным числом болбше 20')
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps,str):
#             raise TypeError("паспорт должен быть строкой")
#         s=ps.split()
#         if len(s) !=2 or len(s[0])!=4 or len(s[1])!=6:
#             raise TypeError("НЕВерный формт паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("сЕРИФ И НОМЕР ПАСпорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self,fio):
#         self.verify_fio(fio)
#         self.__fio=fio
#
#     @property
#     def old(self):
#         return  self.__old
#
#     @old.setter
#     def old(self,year):
#         self.verify_old(year)
#         self.__old=year
#
#
#     @property
#     def weight(self):
#         return self.__weight
#
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, password):
#         self.verify_password(password)
#         self.__password = password
#
#
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, '1234 567890', 80.8)
# p1.fio="Сидоров Игорь Николаевич"
# print (p1.fio)
# print (p1.__dict__)
#
#
# Hacleдование
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"Точка с коорд:({self.__x},{self.__y})"
#
#
# print(issubclass(Point, object))
# print(dir(Point))
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         print("Инициализатор Prop")
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#
#     def __init__(self, *args):
#         print("Переопределенный инициализатор")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self) -> str:
#         return f"Рисование линии: {self._sp},{self._ep},{self._color},{self.get_width()}"
#
#
# class Rect(Prop):
#     def __init__(self, sp, ep, color, width, bg="yellow"):
#         super().__init__(sp, ep, color, width)
#         self._background = bg
#
#     def draw_rect(self) -> str:
#         return f"Рисование прямоугольника: {self._sp},{self._ep},{self._color},{self.get_width()},{self._background}"
#
#
# line = Line(Point(1, 2), Point(10, 20))
# print(line.draw_line())
# print(line._color)
# rect = Rect(Point(30, 40), Point(70, 80), "red",1)
# print(rect.draw_rect())
#
#
#
# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     def __str__(self):
#         return f"{self.__color}"
#
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Regtangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     def __str__(self):
#         return f"{self.__width},{self.__height},{self.color}"
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self,w):
#         if w>0:
#             self.__width=w
#         else:
#             raise ValueError("Ширина должна быть положительным числом")
#
#     def area(self):
#         return self.width*self.height
#
#
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#                 self.__width = h
#         else:
#             raise ValueError("dscjnf должна быть положительным числом")
#
#
# rect = Regtangle(10, 20, "green")
# print(rect)
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.color="red"
# print(rect)
# rect.width=5
# rect.height=6
# print(rect.area())
#
#
#
# class Rect:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\n Ширина {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self,width,height,background):
#         self.fon=background
#         super().__init__(width,height)
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:",self.fon)
#

# class RectBorder(Rect):
#     def __init__(self,width,height, border):
#         self.border=border
#         super().__init__(width,height)
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка :",self.border)

# class RectFonBorder(RectFon):
#     def __init__(self,width,heicht,background,border):
#         super().__init__(width,heicht,background)
#         self.border=border
#
#     def show_rect(self):
#         super().show_rect()
#         print("rРамка ", self.border)
#
#
# shape=Rect(100,200)
# shape.show_rect()
#
# shape1=RectFon(400,300,"yellow")
# shape1.show_rect()
#
# # shape2=RectBorder(600,500,'1px solid red')
# # shape2.show_rect()
#
# shape3=RectFonBorder(400,400,"black",'1px solid red')
# shape3.show_rect()
#
# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str,self))
#
# v=Vector([1,2,3,[2,3]])
# print(v)
# print(type(v))
# class Thislo(int):
#     def __init__(self,t):
#         self.tt=t
#
#
# a=Thislo(4)
# print(a.tt)
# print(type(a))
#
#
#
# Перегрузка методов

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_int(self):
#         if not isinstance(self.__x,int)or not isinstance(self.__y,int):
#             print("координаты должны быть целыми")
#             return False
#         return True
#
#
#
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self,sp,ep=None):
#
#         if ep is None:
#             if sp.is_int():
#                 self.sp=sp
#         else:
#               if sp.is_int() and ep.is_int():
#                   self._sp=sp
#                   self._ep=ep
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# # line.draw_line()
# # line.set_coords(Point(20,40),Point(60,50))
# # line.draw_line()
# # line.set_coords(Point(111,40),Point(60,50))
# # line.draw_line()
#
# #
# #
# #
# # Абстрактные методы
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленными")
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе  должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#     pass
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
#
# Абстрактный метод объявлен но не реализован.
# =====================================================================
# Задача  Table
# from math import pi
# class Table:
#     def __init__(self,width=None,length=None,radius=None):
#         if radius is None:
#             self._width=width
#             self._length=(width if length is None else length)
#         else:
#             self._radius=radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть опеределен метод Calc_area()")
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width*self._length
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi*
#                      self._radius**2, 2)
#
# t=SqTable(20,10)
# print(t.__dict__)
# print(t.calc_area())
# t1=RoundTable(radius=20)
# print(t1.__dict__)
# print(t1.calc_area())
# t2=SqTable(20)
# print(t2.__dict__)
# print(t2.calc_area())
# =========================================================
# =========================================================
#
# from abc import ABC, abstractmethod
# class Chess(ABC):
#     def draw(self):
#         print("Yfhbcjdfk шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print("Переместил шахматную")
#         pass
# class Queen(shess)
#     pass
#
# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     # @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub =80.11
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# print("*" * 50)
# for elem in d:
#     elem.print_value()
#     print(f' - {elem.convert_to_rub():.2f}RUB')
#
#
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print("*" * 50)
# for elem in e:
#     elem.print_value()
#     print(f' - {elem.convert_to_rub():.2f}RUB')
#
#
# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#
#     @abstractmethod
#     def display(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display(self):
#         print("дочерний класс")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("Внучатый класс")
#
#
# gc = GrandChild()
# gc.display2()
#
#
#
# class MyGuter:
#     age=18
#     def __init__(self,name):
#         self.name=name
#
#     @staticmethod
#     def outer_class_metod():
#         print("Я метод внешнего класса")
#
#     def outer_obj_method(self):
#         print("Связующий метод")
#
#     class MyInner:
#         def __init__(self,inner_mame):
#             self.inner_name=inner_mame
#
#         def inner_metod(self):
#             print("Я метод вложенного класс")
#             MyGuter.outer_class_metod()
#
# out = MyGuter('Внешний')
# inner=out.MyInner("внутренний")
# print(inner.inner_name)
# inner.inner_metod()
#
#
# #
# class Color:
#         def __init__(self):
#             self.name="Green"
#             self.lg=self.LightGreen()
#
#         def show(self):
#             print("Name:",self.name)
#
#         class LightGreen:
#             def __init__(self):
#                 self.name="Light green"
#                 self.code="024avc"
#
#             def display(self):
#                 print("Name:",self.name)
#                 print("Code",self.code)
#
#
# outer=Color()
# outer.show()
# g=outer.lg
# g.display()
# g.name="Red"
# g.display()
# f=outer.lg
# f.display()
# class Intern:
#     def __init__(self):
#         self.name = "Smith"
#         self.id = '765'
#
#     def display(self):
#         print("Name", self.name)
#         print(self.id)
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Name", self.name)
#
#
#     class Head:
#
#         def __init__(self):
#             self.name = "Alba"
#             self.id = '007'
#
#         def display(self):
#             print("Name", self.name)
#             print("Id", self.id)
#
#
# outer = Employee()
# outer.show()
# d1 = outer.intern
# print()
# d1.display()
#
# d2 = outer.head
# d2.display()


#
# \
# class Computer:
#     def __init__(self,name,os1,):
#         self.mane=name
#         self.os=self.OS(title=os1)
#         self.cpu=self.CPU(brand,model)
#
#     class OS:
#         def __init__(self,title):
#             self.title=title
#
#         def system(self):
#             return "Win 10"
#
#     class CPU:
#         def __init__(self,brand,model):
#             self.brand=brand
#             self.model=model
#
#         def make(self):
#             return "Intel"
#
#         def model(self,model):
#             return model
#
# comp=Computer("sis1","вит","Intel","core-i7")
# my_os=comp.os
# my_cpu=comp.cpu
#
# print(comp.mane)
# print(comp.os.system())
# print(comp.cpu.make())
# print(comp.cpu.model("Core -i5"))

# class Base:
#     def __init__(self):
#         self.db=self.Inner()
#
#     def display(self):
#         print("in Base clas")
#
#     class Inner:
#         def display1(self):
#             print("Inner of Base Class")
#
# class Subclass(Base):
#     def __init__(self):
#         print ("iN subclass")
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print("Inner ofs sub Class")
#
# a=Subclass()
# a.display()
#
# b=a.db
# b.display1()
# b.display2()

#
#
#
#
# Множественное наследование
# class Creature:
#     def __init__(self,name):
#         self.name = name
#
#
# class Animal:
#     def sleep(self):
#         print(self.name + "is slip")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + "isplayeng")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + "is barkinng")
#
#
# beast = Dog("Buddy")
# beast.bark()
# beast.play()
# beast.sleep()

# class A:
#     def __init__(self):
#         print("A")
#
#
# class B(A):
#     def __init__(self):
#
#         print("B")
#
#     def hi(self):
#         print('B,Hi')
#
#
# class C(A):
#     def __init__(self):
#         print("C")
#
#     def hi(self):
#         print('C,Hi')
#
#
# class D(B,C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#
#         print("D")
#
#     def hi(self):
#         C.hi(self)
#         print("D,Hi")
#
#
#
# d = D()
# d.hi()
# print(D.mro())


#
# class B():
#     def __init__(self):
#
#         print("B")
#
#     def hi(self):
#         print('B,Hi')
#
#
# class C():
#     def __init__(self):
#         print("C")
#
#     def hi(self):
#         print('C,Hi')
#
#
# class D(B,C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#
#         print("D")
# #
# #     def hi(self):
# #         C.hi(self)
# #         print("D,Hi")
# #
# #
# #
# # d = D()
# # d.hi()
# # print(D.mro())
#
# class AA():
#     pass
#
# class A(AA):
#     pass
#
# class Point(A):
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x},{self.y})"
#
#
# class Style:
#     def __init__(self, color="red", width=1):
#         print("Иницифлизатор Style")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, * args):
#         print("Инициализатор pos")
#         self._sp = sp
#         self.ep = ep
#         super().__init__(*args)
#
#
# class Line(Pos, Style):
#     # def __init__(self, sp: Point, ep: Point, color="red", width=1):
#     #     Pos.__init__(self, sp, ep)
#     #     Style.__init__(self, color, width)
#
#     def draw(self):
#         print(f"Рисование линии {self._sp},{self.ep},{self._color},{self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()
# print(Line.__mro__)
# print(Point.mro())
#
#
# Миксины (примеси)
#
#
# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class Loggermexin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(Loggermexin, Displayer):
#     def log(selfself, message, filename=""):
#         super().log(message, filename="subclass.txt")
#
#
# sub = MySubClass()
# sub.display("Cтрока будет отоброжаться и регистрироваться в файле ")
# print(MySubClass.mro())
#
#
#
#
# class Goods:
#     def __init__(self, name, weight,price):
#         super().__init__()
#         print("Inut GOODs")
#         self.name=name
#         self.weight=weight
#         self.price=price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
# class MixinLog:
#     ID=0
#     def __init__(self):
#         print("init Mixinlog")
#         self.ID+=1
#         self.id=self.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}:товар был продан 00:00 часов ")
#
# class Notebook(Goods,MixinLog):
#     pass
#
#
# n=Notebook('Hp',1.5,35000)
# n1=Notebook('Hp',1.5,35000)
# n.print_info()
# n.save_sell_log()
# n1=Notebook("Lg",2,40000)
# n1.print_info()
# n1.save_sell_log()
#
#
#
# Перегрузка операторов
# 24*60*60=86400(

# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return (str(x) if x > 9 else "0" + str(x))
#
#     def __add__(self, other):
#
#         if not isinstance(other,Clock):
#             raise ArithmeticError("Операнды должны быть типа Clock")
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Операнды должны быть типа Clock")
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#
#         if not isinstance(other,Clock):
#             raise ArithmeticError("Операнды должны быть типа Clock")
#         return Clock(self.sec * other.sec)
#
#     def __iadd__(self, other):
#
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Операнды должны быть типа Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         # if self.sec==other.sec:
#         #     return True
#         # return False
#         return self.sec==other.sec
#
#     def __gt__(self, other):
#         #     return True
#         # return False
#         return self.sec>other.sec
#
#
# c1 = Clock(300)
# print(c1.get_format_time())
# c2 = Clock(200)
# c4 = Clock(300)
# print(c2.get_format_time())
# c3 = c2 - c1
#
#
# print(c1.get_format_time())
# print(c2.get_format_time())
# print(c3.get_format_time())
# if c1>c2:
#     print("Первый больше")
# else:
#     print("Второй больше")

#
#
#
# class Student:
#     def __init__(self,name, *marks):
#         self.name=name
#         self.marks=list(marks)
#
#
#     def __getitem__(self, item):
#         if 0<=item<len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError('Неверный индекс')
#
#     def __setitem__(self, key, value):
#         if 0 <= key < len(self.marks) and isinstance(key,int):
#             self.marks[key]=value
#         elif key>=len(self.marks):
#             off=key+1-len(self.marks)
#             self.marks.extend([0]*off)
#         else:
#             raise IndexError('Неверный индекс')
#
#     def __delitem__(self, key, value):
#         if not isinstance(key,int):
#             reise
#
#         else:
#             raise IndexError('Неверный индекс')
#
#
# s1=Student("Сергей",5,5,5,3,4,5)
# print(s1[4])
# s1[7]=5
# del s1[2]
# print(s1.marks,s1[2])

# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return (str(x) if x > 9 else "0" + str(x))
#
#     def __getitem__(self, item):
#         if not isinstance(item,str):
#             raise ValueError("Ключ должен быть строкеой")
#
#         if item=="hour":
#             return(self.sec//3600)%24
#         elif  item=="min":
#             return(self.sec//60)%60
#         elif item == "sec":
#                 return (self.sec%60)
#         return "Htdthysq rk.x"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if not isinstance(value, int):
#             raise ValueError("Зрфчение должно быть целым числом")
#
#         h=self.sec%60
#         m=(self.sec//60)%60
#         s=(self.sec//3600)%24
#         if key=="hour":
#             self.sec=s+60*m+value*3600
#         if key=="min":
#             self.sec=s+60*value+h*3600
#         if key=="sec":
#             self.sec=value+60*m+h*3600
#
#
#
#
# c1=Clock(80000)
# print(c1.get_format_time())
# c1["hour"]=10
# c1["min"]=37
# c1["sec"]=15
#
# print(c1["hour"],":",c1['min'],":",c1['sec'])
#
#
#
# Полиморфизм
#
# class Rectangle:
#     def __init__(self,w,h):
#         self.w=w
#         self.h=h
#
#     def get_perimetr(self):
#         return 2*(self.w+self.h)
#
# class Square:
#     def __init__(self,a):
#         self.a=a
#
#
#     def get_perimetr(self):
#
#         return 4*self.a
#
# class Triangle:
#         def __init__(self, a,b,c):
#             self.a = a
#             self.b = b
#             self.c = c
#
#         def get_perimetr(self):
#             return self.a+self.b+self.c
#
#
# r1=Rectangle(1,2)
# r2=Rectangle(3,4)
#
# s1=Square(1)
# s2=Square(2)
# t2=Triangle(3,4,5)
# shape=[r1,r2,s1,s2,t2]
# shape=[Triangle(3,4,5),Rectangle(1,2),Rectangle(3,4),s1,s2]
# for  g in shape:
#     print(g.get_perimetr())
#
# class Number:
#     def __init__(self,value):
#         self.value=value
#
#     def total(self,a):
#         return self.value+int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return (str(self.value) + str(a))
#
# t1=Number(10)
# t2=Text(10)
# print(t1.total(35))  #45
# print(t2.total(35))  #1035
#
# class Cat:
#     def __init__(self,name, alt):
#         self.name=name
#         self.alt=alt
#     def info(self):
#         return f"Я кот . Меня зовут {self.name}.Мне {self.alt} лет "
#
#     def sound(self):
#         return f"Я кот . Меня зовут {self.name}.Я мяукаю "
#
#
# class Dog:
#     def __init__(self, name, alt):
#         self.name = name
#         self.alt = alt
#
#     def info(self):
#         return f"Я пес . Меня зовут {self.name}.Мне {self.alt} лет "
#
#     def sound(self):
#         return f"Я пес . Меня зовут {self.name}.Я громко гавкая "
#
# a1=Cat("Пират", "2.5")
# print(a1.info())
# print(a1.sound())
# a2=Dog("Шарик","3")
# a2.info()
# a2.sound()

# class Human:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f'{self.surname} {self.name} {self.age}'
#
#
# class Student(Human):
#     def __init__(self, surname, name, age, v1, group, ball):
#         self.v1 = v1
#         self.group = group
#         self.ball = ball
#         super().__init__(surname, name, age)
#
#     def info(self):
#         return f'{super().info()} {self.v1} {self.group} {self.ball}'
#
#
# class Teacher(Human):
#     def __init__(self, surname, name, age, sub, rating):
#         self.sub = sub
#         self.rating = rating
#         super().__init__(surname, name, age)
#
#     def info(self):
#         return f'{super().info()} {self.sub} {self.rating}'
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, v1, group, ball, top):
#         self.top = top
#         super().__init__(surname, name, age, v1, group, ball)
#
#     def info(self):
#
#         return f'{super().info()} {self.top}'
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in group:
#     print(i.info())
#
#
#
#
# class Cat:
#     def __init__(self,name):
#         self.name=name
#
#     def __repr__(self):
#         return f"{self.__class__}:{self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
# cat=Cat("Пушок")
# print(cat)
#
# #
# class Point:
#     def __init__(self,*args):
#         print(args)
#         self.__coord=args
#
#     def __len_(self):
#         return len(self.__coord)
#
# p=Point(5,7,8)
# print(len(p))

# class Point:
#     __slots__ = ('x','y','__length')
#
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         self.length=math.sqrt(x*x+y*y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self,value):
#         self.__length=value
#
#
#
# pt=Point(1,2)
# # pt.z=3
# #
# # print(pt.__dict__)
# print(pt.length)
# class Point:
#     __slots__ = ('x','y')
#
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#
# class Point3D(Point):
#     __slots__ = ("z",)
#     def __init__(self,x,y,z):
#         super().__init__(x,y)
#         self.z=z
#
# pt=Point(1,2)
# pt3=Point3D(10,20,30)
# pt3.z=30
#
# a=3
# print(type(pt3))
#
#
# Функторы
# class Counter:
#     def __init__(self):
#         self.__counter=0
#
#     def  __call__(self, *args, **kwargs):
#         self.__counter+=1
#         print(self.__counter)
#
# c1=Counter()
# c1()
# c1()
# c1()
# c2=Counter()
# c2()
# c2()
# c2()
# c2()
#
#
class StripChars:
    def __init__(self,chars):
        self.charc=chars
    def __call_(self,*args, **kwargs):
        if not isinstance(args[0],str):
            raise ValueError("Arгумент дложен быть строко")
        print(kwargs)
        return  args[0].strip(self.__chars)

s1=StripChars("?:!.: ")
print(s1('Hello'))

def strip_chars(chars):
    def wrap(*args,**Kwargs):
        if not isistance(args[0], str):
            raise ValueError("Aргументы должны быть строкой")
        return