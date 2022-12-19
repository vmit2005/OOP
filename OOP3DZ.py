class Triangle:
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
        Triangle.__count += 1
        # print(triangle.__count)

    @staticmethod
    def get_count():
        return Triangle.__count

    # @staticmethod
    # def null_count():
    #     Triangle.__count = 0

    @staticmethod
    def geron(a, b, c):
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        Triangle.plus()

        return s

    @staticmethod
    def square(a, h):
        s = a * h / 2
        Triangle.plus()
        return s

    @staticmethod
    def kvadro(a):
        Triangle.plus()
        return a ** 2

    @staticmethod
    def regtangle(a, b):
        Triangle.plus()
        return a * b


print(Triangle.geron(3, 4, 5))
print(Triangle.square(6, 8))
print(Triangle.kvadro(7))
print(Triangle.regtangle(7, 10))
print("Число вызовов функций- ", Triangle.get_count())
print(Triangle.__doc__)
