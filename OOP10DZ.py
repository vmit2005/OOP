from abc import ABC, abstractmethod
from math import sqrt


class Chare:
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def print_info(self):
        pass

    @abstractmethod
    def painting(self):
        pass


class Square(Chare):
    def __init__(self, color, a):
        super().__init__(color)
        self.a = a

    def perimeter(self):
        return 4 * self.a

    def area(self):
        return self.a ** 2

    def print_info(self):
        print("Квадрат")
        print(f"Цвет {self.color}")
        print(f"Сторона квадрата {self.a} мм")
        a = self.area()
        p = self.perimeter()
        print(f"Периметр квадрата {p}мм")
        print(f"Площадь квадрата {round(a,2)}кв мм")

    def painting(self):
        a = self.a
        t = True
        while t:  # Определяем масштаб
            if a > 10:
                a = a / 10
            else:
                t = False
        a = int(round(a, 0))
        for i in range(a):
            print('*' * a)


# s1=Square("Red",9)
# s1.print_info()
# s1.painting()

class Rectangle(Chare):
    def __init__(self, color, w, h):
        super().__init__(color)
        self.w = w
        self.h = h

    def perimeter(self):
        return 2 * (self.w + self.h)

    def area(self):
        return self.w * self.h

    def print_info(self):
        print("Прямоугольник")
        print(f"Цвет прямоугольника {self.color}")
        print(f"Стороны прямоугольника,мм {self.w}, {self.h}")
        a = self.area()
        p = self.perimeter()
        print(f"Периметр прямоугольника {p}мм")
        print(f"Площадь прямоугольника {round(a,2)}кв. мм")

    def painting(self):
        w = self.w
        h = self.h
        t = True
        while t:  # Определяем масштаб
            if w > 10:
                w = w / 10
                h = h / 10
            else:
                t = False
        w = int(round(w, 0))
        h = int(round(h, 0))
        for i in range(w):
            print('*' * h)


# r1=Rectangle("RAL 5031",380,221)
# r1.print_info()
# r1.painting()

class Triangle(Chare):
    def __init__(self, color, a, b, c):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = (self.perimeter() / 2)

        s = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return s

    def print_info(self):
        print("Треугольник")
        print(f"Цвет треугольника", self.color)
        print(f"Стороны треугольника,мм {self.a}, {self.b}, {self.c}")
        a = self.area()
        p = self.perimeter()
        print(f"Периметр треугольника {p}мм")
        print(f"Площадь треугольника {round(a,2)}кв. мм")

    def painting(self):
        a = self.a
        b = self.b
        c = self.c
        a, b, c = sorted((a, b, c), reverse=True)  # Сортровка сторон
        m = 20 / a  # масштаб
        a, b, c = (round(a * m, 0), round(b * m, 0), round(c * m, 0))
        """
        a- самая длинная сторона треугольника. Будет подошвой. Размер 20 знаков. float
        а1- координата высоты на стороне а.До целого. float
        h- высота треугольника.До целого. float
        i- номер строки
        a11 -позиция первого знака в строке
        """
        a1 = round((a / (b + c)) * b, 0)
        print(a1)
        h = round(sqrt(b * b - a1 * a1), 0)
        for i in range(int(h)):
            a11 = int(round(a1 * (h - i) / h, 0))
            a31 = int(round((a - (a - a1) * (h - i) / h), 0))
            s = ""
            for j in range(40):
                if a11 <= j <= a31:
                    s += "* "
                else:
                    s += "  "
            print(s)



q = [Square("red", 88), Rectangle("rgb", 38, 92), Triangle("RAL 1031", 4, 5, 8), Triangle("RAL 1031", 9, 7, 7)]
for i in q:
    i.print_info()
    i.painting()
