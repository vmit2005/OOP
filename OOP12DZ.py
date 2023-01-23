class Segment:
    @staticmethod
    def verify_dimension(dim):
        if dim < 0 or not isinstance(dim, int):
            raise TypeError(f'Все стороны треугольника  должны быть целыми и больше 0')

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        self.verify_dimension(value)
        instance.__dict__[self.name] = value
        # return getattr(instance, self.name)

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Triangle:
    a = Segment()
    b = Segment()
    c = Segment()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_trian(self):
        return f"Треугольник со сторонами({self.a}, {self.b}, {self.c}) "

    def triangle_validate(self):
        a = self.a
        b = self.b
        c = self.c
        if a < b + c and b < a + c and c < a + b:
            return "Существует"
        return "Не существует"


t1 = Triangle(8, 5, 4)
print(t1.get_trian(), t1.triangle_validate())
t1 = Triangle(8, 3, 4)
print(t1.get_trian(), t1.triangle_validate())
t1 = Triangle(6, 6, 4)
print(t1.get_trian(), t1.triangle_validate())
