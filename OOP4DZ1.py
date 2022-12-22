import re
class Account:
    suffix = "RUB"
    suffix_usd = 'USD'
    suffix_eur = "EUR"
    rate_usd = 0.013
    rate_eur = 0.011

    def __init__(self, num, surname, percent, value=0):
        self.num = num
        self.surname = surname
        self.percent = percent
        self.value = value
        print(f"Счет #{self.num} принадлежащий {self.surname}  был открыт")
        print("*" * 50)

    def __del__(self):
        print("*"*50)
        print(f"Cчет #{self.num} принадлежащий {self.surname} ,был закрыт")

    def print_balance(self):
        print(f"Текущий баланс {self.value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете")
        print("*" * 50)
        print(f"{self.num}")
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f"Проценты: {self.percent:.0%}")
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
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счета: {usd_val}{Account.suffix_usd}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счета: {eur_val}{Account.suffix_usd}')

    def edit_owner(self,surname):
        self.surname=surname

    def add_percennts(self):
        self.value+=self.value*self.percent
        print('Проценты были начислены')
        self.print_balance()

    def withdraw_money(self,val):
        if val>self.value :
            print(f"К сожалению у Вас нет  {val} {Account.suffix}")
        else :
            self.value-=val
            print(f'{val}{Account.suffix} ,были успешно сняты')
        self.print_balance()

    def add_money(self,val):
        self.value+=val
        print(f'{val}{Account.suffix} ,были успешно добавлены')
        self.print_balance()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def get_num(self):
        return self.num

    def set_num(self, num):
        p=r'#[0-9]{5}'
        if (re.findall(p,num))[0]==num:
            self.num = num
            print("Принят новый номер счета")
        else:
            print("Номер счета не принят")


    def get_surname(self):
        return self.surname

    def set_surname(self,surname):
        p=r'[А-ЯЁа-яё-]{2,32}'
        if (re.findall(p,surname))[0]==surname:
            self.surname=surname
            print(f"Навая фамилия {self.surname} принята")
        else:
            print("Введенная фамилия не соответствуеет допустимому формату")

    def get_percent(self):
        return  self.percent

    def set_percent(self, percent):
        if isinstance(percent,(float,int)):
            self.percent=percent
            print(f"Новый процент по счету {self.percent}")
        else:
            print("Новый процент по счету не принят")


    def get_value(self):
        return self.value

    def set_value(self, value):
        if isinstance(value,(int,float)) and 1<value<1000000:
            self.value=value
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
acc.set_num('#23456')
print("Номер счета ",acc.get_num())
acc.set_surname("Бендер-Задунайский")
print("Фамилия владельца счета:",acc.get_surname())
acc.set_percent(6.859)
print("Действующий процент: ",acc.get_percent())
acc.set_value(10000)
print("Сумма на счете",acc.get_value())