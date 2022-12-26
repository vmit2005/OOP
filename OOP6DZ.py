import math


class Table:

    @staticmethod
    def user_input1():
        print("ВВедите размеры стола в метрах")
        print("Для прямоугольного стола введите длину и ширину")
        print("для квадратного стола достаточно одного размера стороны")
        print("Чтобы задать размеры круглого размеры ")
        s = str(input("Введите R [радиус стола]"))
        return s.split()


class Table_rectangle(Table):
    def __init__(self, w, l):
        self.w = w
        self.l = l

    def square(self):
        return float(self.w) * float(self.l)


class Table_circle(Table):
    def __init__(self, r):
        self.r = r

    def sguare(self):
        return math.pi * float(self.r) ** 2


s = Table.user_input1()
if s[0] == "R":
    t1 = Table_circle(s[1])
    print(t1.sguare())

else:
    if len(s) == 2:
        t2 = Table_rectangle(s[0], s[1])
        print(t2.square())
    elif len(s) == 1:
        t2 = Table_rectangle(s[0], s[0])
        print(t2.square())
    else:
        print("Какой-то непонятный тип данных")
