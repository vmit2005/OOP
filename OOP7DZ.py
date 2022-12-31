class Student:

    def __init__(self, name):
        self._name = name


    def Student_get(self):
        return self._name

    class Notebook:
        def __init__(self, n_name, proc, ram, obj):
            self._n_name = n_name
            self._proc = proc
            self._ram = ram
            self.obj = obj

        def print_notebook(self):
            print("Характеристики ноута")
            print("Марка     ", self._n_name)
            print("Процессор ", self._proc)
            print("Память(Гб)", self._ram)

        def rtrn_notebook(self):
            return "=> " + str(self._n_name) + ", " + str(self._proc) + ", " + str(self._ram)

        def rtrn_notebook2(self):
            return str(self.obj.Student_get()) + "=> " + str(self._n_name) + ", " + str(self._proc) + ", " + str(
                self._ram)


s1 = Student("Boris")
n = s1.Notebook("HP", "i5", "16", s1)
print(n.rtrn_notebook2())
s2 = Student("Anton")
n2 = s2.Notebook("LG", "i7", "32", s2)
print(n2.rtrn_notebook2())
s3 = Student("Ivan")
n3 = s3.Notebook("XZ", "i3", "8", s3)
print(n3.rtrn_notebook2())
