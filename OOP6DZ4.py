from math import pi



class Table:

    def __init__(self):
        print("ВВедите размеры стола в метрах")
        print("Для прямоугольного стола введите длину и ширину")
        print("для квадратного стола достаточно одного размера стороны")
        print("Чтобы задать размеры круглого размеры ")
        self.s= str(input("Введите R [радиус стола]")).split()
        print(len(self.s))


    def square(self):
        if self.s[0] == "R" and len(self.s)==2:

            sq = pi*(float(self.s[1]))**2
            print("Стол круглый")
            return sq

        elif len(self.s) == 2:
            sq= float(self.s[0] )*(float(self.s[1]))
            print("Стол прямоугольный")
            return sq

        elif len(self.s)==1:
            sq=(float(self.s[0]))**2
            print("Стол квадратный")
            return sq
        else:
            print("Какой-то непонятный тип данных")

t=Table()
print("Площадь стола ",t.square())