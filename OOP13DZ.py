import json
# from ramка import Ramка
# Ramка(40,"OOP 13",'Домашнее задание')

class Trian:
        def __init__(self,a,b,c):
            self.a=int(a)
            self.b=int(b)
            self.c=int(c)

        def save_json(self):

            d={'a':self.a, 'b':self.b, 'c':self.c}

            with open("triangle.json", "w") as fw:
                json.dump(d, fw, indent=4)


        def load_json(self):
            with open("triangle.json", "r") as fw:
                data = json.load(fw)
                self.a=data.get('a')
                self.b=data.get('b')
                self.c=data.get('c')

        def get_trian(self):
            return(self.a,self.b,self.c)





t1=Trian(10,11,8)
t1.save_json()
t2=Trian(0,0,0)
t2.load_json()
print("Считано из файла",t2.get_trian())


