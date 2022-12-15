class triangle:
    """
    plus
    get_count
    null_count - функции работы с коунд
    geron - площадь треугольника по Герону
    sqare - площадь треугольника по основанию и высоте
    rvadro - площадь квадрата
    regtangle- площадь треугольника

    """
    __count = 0

    @staticmethod
    def plus():
        triangle.__count += 1
        # print(triangle.__count)

    @staticmethod
    def get_count():
        return triangle.__count

    @staticmethod
    def null_count():
        triangle.__count = 0

    @staticmethod
    def geron(a, b, c):
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        triangle.plus()
        return s

    @staticmethod
    def square(a, h):
        s = a * h / 2
        triangle.plus()
        return s

    @staticmethod
    def kvadro(a):
        triangle.plus()
        return a ** 2

    @staticmethod
    def regtangle(a, b):
        triangle.plus()
        return a * b


print(triangle.geron(3, 4, 5))
print(triangle.square(6, 8))
print(triangle.kvadro(7))
print(triangle.regtangle(7, 10))
print("Число вызовов функций- ", triangle.get_count())
print(triangle.__doc__)
