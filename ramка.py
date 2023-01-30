class Ramка:
    """
    Модуль отрисовки рамки
    Ramка(N,'string_1'...'string_n')

    """

    def __init__(self, b : int, *strings):
        print(chr(9556) + chr(9552) * (b - 2) + chr(9559))
        for i in strings:
            if len(i) > b - 2:
                raise TypeError(f"Ширину рамки {b} нужно сделать {len(i)+2} или больше ")
                # b=len(i)+2
            n1 = ((b - len(i)) // 2) - 1
            n2 = b - n1 - len(i) - 2
            print(chr(9553) + " " * n1 + i + " " * n2 + chr(9553))
        print(chr(9562) + chr(9552) * (b - 2) + chr(9565))


if __name__ == '__main__':
    Ramка(45, "Модуль", "отрисовки", "рамки", "===========================================",
          'Ramка(b:int,"string_1"..."string_n")')
    input("Enter")
