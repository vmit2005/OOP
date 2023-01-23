import tkinter as tk

def get_entry():
    value=en.get()
    if value:
        print(value)
    else:
        print("Введите значение")


def say_hello():
    print("Hello")


win=tk.Tk()
win.title("Графическое окно")
# win.config(bg="#00FF32")
win.geometry("500x600+100+200")
win.minsize(300,400)
win.maxsize(700,800)
win.resizable(True,True)
en=tk.Entry(win)
en.grid(row=0,column=1)
tk.Button(win,text='get',command=get_entry).grid()
tx=tk.Text(win).grid()
tx.
# tx.pack()


win.mainloop()