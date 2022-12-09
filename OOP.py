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
import  turtle
class Point:
    def __init__(self,x,y):
        if Point.__check_value(x) and Point.__check_value(y):
             self.__x=x
             self.__y=y

    def __check_value(z):
        if (isinstance(z,int) or isinstance(z,float)):
            return True
        return False

    def set_coord(self,x,y):
        if Point.__check_value(x) and Point.__check_value(y):
             self.__x=x
             self.__y=y
        else:
            print("Координаты должны быть числами")

    def set_coord_x(self, x, ):
        if Point.__check_value(x) :
            self.__x = x

        else:
            print("Координаты должны быть числами")

    def  set_coord_y(self, y ):
        if Point.__check_value(y):
            self.__y = x

        else:
            print("Координаты должны быть числами")

def get_coord(self):
        return self.__x, self.__y

p1=Point(5,10)
# print(p1.__x,p1.__y)
p1.__x=100
p1.__y="abc"
# print(p1.x,p1.y)
# public (self.x)- публичное свойставо
# protected(self._x)  -используется при наследовании
# private (self.__x)  - закрытые свойства
print(p1.__dict__)
# print(p1.get_coord())
p1.set_coord(2,5.8)
# print(p1.get_coord())
p1.set_coord_x(11)
# print(p1.get_coord())