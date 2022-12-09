class Rectangle:
    _l=0
    _b=0

    def __x_valid(self,x):
        if isinstance(x,int) or isinstance(x,float):
            return True
        else:
            # print("Неверные данные")
            return False

    def __init__(self,l,b):
        if self.__x_valid(l):
            self._l=l
        if self.__x_valid(b):
            self._b=b

    def reg_set_l(self,l):
        if self.__x_valid(l):
            self._l = l

    def reg_set_b(self, b):
        if self.__x_valid(b):
            self._b = b

    def reg_get_l(self):
        return self._l

    def reg_get_b(self):
        return self._b



    def __reg_calc(self):
        s=self.reg_get_l()*self.reg_get_b()  # Площадь
        p=(self.reg_get_l()+self.reg_get_b())*2  #Периметр
        d=(self.reg_get_l()**2+self.reg_get_b()**2)**0.5 #Гипотенуза
        return s,p,d

    def __reg_zvezda_pint(self):
        for i in range(self.reg_get_l()):
            print("*"*self.reg_set_b())



    def reg_print(self):
        if self.reg_get_l()==0 or self.reg_get_b()==0:
            print ("Введены неверные данные")
        else:
            print(f"Длина  прямоугольника : {self.reg_get_l()}")
            print(f"Ширина прямоугольника : {self.reg_get_b()}")
            print("="*40)
            s, p, d = self.__reg_calc()
            print(f"Площадь               : {s}")
            print(f"Периметр              : {p}")
            print(f"Диагональ(гипотенуза) : {d:.2f}")
            print()
            print("Изображение прямоугольника")
            self.__reg_zvezda_pint()


        print()
        print()



r1=Rectangle(3,"4")
r3=Rectangle(3,4)

r2=Rectangle(3,9)

r1.reg_print()
r3.reg_print()
r2.reg_print()
r4=Rectangle(8,10)
r4.reg_print()




