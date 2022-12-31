class Student:

    def __init__(self, name,n_name, proc, ram):
        self._name = name
        self.notebook = self.Notebook()
        self.notebook.set_nonebook("XЗ",'xeon','64')
        self.notebook.set_nonebook(n_name,proc,ram)


    def Student_get(self):
        s=self.notebook.rtrn_notebook()
        return str(self._name+s)

    class Notebook:
        def __init__(self):
            self._n_name = "HP"
            self._proc = "i5"
            self._ram = "16"

        def set_nonebook(self, n_name, proc, ram):
            self._n_name = n_name
            self._proc = proc
            self._ram = ram

        def rtrn_notebook(self):
            return "=> " + str(self._n_name) + ", " + str(self._proc) + ", " + str(self._ram)


s1 = Student("Boris","i3","386","4")
print(s1.Student_get())
s2 = Student("ivan","LG", "i7", "32")
print(s2.Student_get())
s3 = Student("Anna","XZ", "i3", "8")
print(s3.Student_get())
