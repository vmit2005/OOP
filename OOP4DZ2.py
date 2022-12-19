import re
class Account:
    suffix = "RUB"
    suffix_usd = 'USD'
    suffix_eur = "EUR"
    rate_usd = 0.013
    rate_eur = 0.011

    def __init__(self, num, surname, percent, value=0):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value
        print(f"Счет #{self.__num} принадлежащий {self.__surname}  был открыт")
        print("*" * 50)

    def __del__(self):
        print("*"*50)
        print(f"Cчет #{self.__num} принадлежащий {self.__surname} ,был закрыт")

    def print_balance(self):
        print(f"Текущий баланс {self.__value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете")
        print("*" * 50)
        print(f"{self.__num}")
        print(f"Владелец: {self.__surname}")
        self.print_balance()
        print(f"Проценты: {self.__percent:.0%}")
        print("*" * 50)

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f'Состояние счета: {usd_val}{Account.suffix_usd}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f'Состояние счета: {eur_val}{Account.suffix_usd}')

    def edit_owner(self,surname):
        self.surname=surname

    def add_percennts(self):
        self.__value+=self.__value*self.__percent
        print('Проценты были начислены')
        self.print_balance()

    def withdraw_money(self,val):
        if val>self.__value :
            print(f"К сожалению у Вас нет  {val} {Account.suffix}")
        else :
            self.__value-=val
            print(f'{val}{Account.suffix} ,были успешно сняты')
        self.print_balance()

    def add_money(self,val):
        self.__value+=val
        print(f'{val}{Account.suffix} ,были успешно добавлены')
        self.print_balance()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def num2(self):
        return self.__num
    @num2.setter
    def num2(self, num):
        p=r'#[0-9]{5}'
        if (re.findall(p,num))[0]==num:
            self.__num = num
            print("Принят новый номер счета")
        else:
            print("Номер счета не принят")


    @property
    def surname2(self):
        return self.__surname

    @surname2.setter
    def surname2(self,surname):
        p=r'[А-ЯЁа-яё-]{2,32}'
        if (re.findall(p,surname))[0]==surname:
            self.__surname=surname
            print(f"Навая фамилия {self.surname} принята")
        else:
            print("Введенная фамилия не соответствуеет допустимому формату")

    @property
    def percent2(self):
        return  self.__percent

    @percent2.setter
    def percent2(self, percent):
        if isinstance(percent,(float,int)):
            self.__percent=percent
            print(f"Новый процент по счету {self.__percent}")
        else:
            print("Новый процент по счету не принят")

    @property
    def value2(self):
        return self.__value
    @value2.setter
    def value2(self, value):
        if isinstance(value,(int,float)) and 1<value<1000000:
            self.__value=value
        else:
            print('Новое значение не принято')

acc = Account('12345', 'Долгих', 0.03, 1000)
acc.print_balance()
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
Account.set_usd_rate(2)
Account.set_eur_rate(3)
acc.convert_to_usd()
acc.convert_to_eur()
print()
acc.edit_owner("Дюма")
acc.print_info()
acc.add_percennts()
print()
acc.withdraw_money(30000)
acc.withdraw_money(100)
acc.add_money(5000)
acc.withdraw_money(3000)
acc.num2='#23456'
print("Номер счета ",acc.num2)
acc.surname2="Бендер-Задунайский"
print("Фамилия владельца счета:",acc.surname2)
acc.set_percent(6.859)
print("Действующий процент: ",acc.get_percent())
acc.value2=10000
print("Сумма на счете",acc.value2())