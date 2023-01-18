class MyDcorator:
    def __init__(self, arg):
        self.p = arg

    def __call__(self, fn):
        def wrap(a, b):
            print("Исходные значения а=" + str(a) + ", b=" + str(b))
            print("возвести в степень - " + str(self.p))
            print("Результат - " + str(fn(a, b) ** self.p))
            print("Спасибо за внимание")

        return wrap


@MyDcorator(3)
def func(a, b):
    return (a * b)

func(2, 2)

print()
print("=================================")
print()

@MyDcorator(3)
def func(a, b):
    return (a * b)

func(2, 4)
