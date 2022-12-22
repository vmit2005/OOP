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
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"Точка с коорд:({self.__x},{self.__y})"


print(issubclass(Point, object))
print(dir(Point))


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
        print("Инициализатор Prop")
        self._sp = sp
        self._ep = ep
        self._color = color
        self.__width = width

    def get_width(self):
        return self.__width


class Line(Prop):

    def __init__(self, *args):
        print("Переопределенный инициализатор")
        # Prop.__init__(self, *args)
        super().__init__(*args)

    def draw_line(self) -> str:
        return f"Рисование линии: {self._sp},{self._ep},{self._color},{self.get_width()}"


class Rect(Prop):
    def __init__(self, sp, ep, color, width, bg="yellow"):
        super().__init__(sp, ep, color, width)
        self._background = bg

    def draw_rect(self) -> str:
        return f"Рисование прямоугольника: {self._sp},{self._ep},{self._color},{self.get_width()},{self._background}"


line = Line(Point(1, 2), Point(10, 20))
print(line.draw_line())
print(line._color)
rect = Rect(Point(30, 40), Point(70, 80), "red",1)
print(rect.draw_rect())
