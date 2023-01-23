from random import choice
from random import randint


class Cat:
    n = 51

    def __init__(self, number: int, name: str, gender: str):
        self.number = number
        self.name = name
        self.gender = gender

    @staticmethod
    def n_plus():
        Cat.n += 1
        return int(Cat.n)

    def get_cat(self):
        return ("Списочный номер-" + str(self.number) + " Имя-" + str(self.name) + " Пол-" + str(self.gender))

    def __add__(self, other):
        if self.gender == other.gender:
            raise ValueError('Пол партнеров должен быть одинаковый')
        else:
            s1 = []
            for i in range(randint(1, 6)):
                c = Cat(Cat.n_plus(), " ", Cat.M_F(self))
                # print(c.get_cat())
                s1.append(c)
        return s1

    def M_F(self):
        choice(["M"])
        if randint(1, 2) == 1:
            return "M"
        else:
            return "F"

    def sex_validate(self, other):
        """
        Валидатор случки
        """
        if self.gender != other.gender:
            return True
        else:
            return False

    def add_name(self, name):
        self.name = name

    def get_number(self):
        return self.number


c1 = Cat(1, "Murka", "F")
c2 = Cat(2, "Barsik", "M")
c3 = Cat(3, "Linda", "F")
c4 = Cat(4, "Bandit", "M")

base = [c1, c2, c3, c4]


class Cats():

    @staticmethod
    def get_base(base):
        for i in base:
            print(i.get_cat())

    @staticmethod
    def add_name_base(base, number, name):
        for i in base:
            a = i.get_number()
            if a == number:
                i.add_name(name)
        print("add")


# Cats.get_base(base)
# base.extend(c1+c2)
# Cats.get_base(base)
# Cats.get_base(c3+c4)
# Cats.add_name_base(base,52,"stinger")
# Cats.get_base(base)
# print(c1.sex_validate(c3))


while True:
    Cats.get_base(base)
    print("Выберите действие:")
    print("[O]Организовать случку/[R]Редактировать имя/[L]вывести список/[E]Выход")
    d = input(" ")
    if d == "O" or d == "o":
        n = (input("Введите списочные ").split(","))

        for i in base:
            a = i.get_number()
            if a == int(n[0]):
                c1 = i
        for i in base:
            a = i.get_number()
            if a == int(n[1]):
                c2 = i

        if c1.sex_validate(c2):
            print("Sex True")
            base.extend(c1 + c2)
        else:
            print("Sex False")

            print("Выбрана неправильная пара. Выберите пару разного пола.")

    if d == 'R' or d == 'r':
        n = (input("Введите через запятую списочный номер и новое имя")).split(',')
        Cats.add_name_base(base, int(n[0]), str(n[1]))
    if d == 'L' or d == 'l':
        Cats.get_base(base)

    if d == "E" or d == "e":
        break
