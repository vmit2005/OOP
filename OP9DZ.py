from random import choice
from random import randint

class Cat:
    n=51
    def __init__(self, number:int, name:str, gender:str):
        self.number=number
        self.name=name
        self.gender=gender


    @staticmethod
    def n_plus():
        Cat.n+=1
        return int(Cat.n)

    def get_cat(self):
        return("Списочный номер-"+str(self.number)+" Имя-"+str(self.name)+" Пол-"+str(self.gender))

    def __add__(self, other):
        if self.gender == other.gender:
            raise ValueError('Пол партнеров должен быть одинаковый')
        else:
            s1 = []
            for i in range(randint(1, 6)):
                c=Cat(Cat.n_plus(), " ", Cat.M_F(self))
                # print(c.get_cat())
                s1.append(c)
        return s1


    def M_F(self):
        choice(["M"])
        if randint(1, 2) == 1:
            return "M"
        else:
            return "F"

    def sex_validate(self,other):
        """
        Валидатор случки
        """
        if self.gender!=other.gender:
            return True
        else:
            return


    def add_name(self, name):
        self.name=name

    def get_number(self):
        return self.number

c1=Cat(1,"Murka","F")
c2=Cat(2,"Barsik","M")
c3=Cat(3,"Linda","F")
c4=Cat(4,"Bandit","M")

base=[c1,c2,c3,c4]

class Cats():

    @staticmethod
    def get_base(base):
        for i in base:
           print(i.get_cat())

    @staticmethod
    def add_name_base(base,number,name):
        for i in base:
            if i.get_number==number:
                i.add_name(name)


Cats.get_base(base)
base.extend(c1+c2)
Cats.get_base(base)
Cats.get_base(c3+c4)




