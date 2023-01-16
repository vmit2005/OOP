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
                print(type(c))
                s1.append(c)

        print (type(tuple(s1)))
        return tuple(s1)


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

c1=Cat(1,"Murka","F")
c2=Cat(2,"Barsik","M")
c3=Cat(3,"Linda","F")
c4=Cat(4,"Bandit","M")



class Cats(Cat):
    n=51 #Номера котов заняты до n


    def __init__(self,*cats:Cat):
        self.base=[]
        for i in cats:
            self.base.append(i)




    def get_base(self):
        for i in self.base:

           print(i.get_cat())

    def __add__(self, other):
        print(self.base, other.base)

        return self.base.extend(other.base)




cc1=Cats(c1,c2,c3,c4)


cc1.get_base()
cc2=Cats(c1+c2)

print("1",type(cc1))
print("2",type(cc2),cc2)
print(type(cc1+cc2))
# (cc1+cc2).get_base()

