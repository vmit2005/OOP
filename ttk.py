import tkinter as tk
click=""
stek_a=0

def add_digit(digit):
    value=calc.get()+str(digit)
    calc.delete(0,tk.END)
    calc.insert(0,value)

def get_entry():
    value=en.get()
    if value:
        print(value)
    else:
        print("Введите значение")

def plus_click():
    click="+"
    stek_a=calc.get()
    calc.insert(0,"0")
    print(click,stek_a)


def say_hello():
    print("Hello")


win=tk.Tk()
win.geometry("240x260+100+200")
win['bg']="#33ffe6"
win.title("Калькулятор")



calc=tk.Entry(win,justify=tk.RIGHT,font=('Arial',15),width=15)
calc.grid(row=0,column=0,columnspan=3,stick='we')

tk.Button(text='1',bd=5, font=('Arial',13),command=lambda :add_digit(1)).grid(row=1,column=0, stick='wens',padx=5,pady=5 )
tk.Button(text='2',bd=5, font=('Arial',13),command=lambda :add_digit(2)).grid(row=1,column=1, stick='wens',padx=5,pady=5 )
tk.Button(text='3',bd=5, font=('Arial',13),command=lambda :add_digit(3)).grid(row=1,column=2, stick='wens',padx=5,pady=5 )
tk.Button(text='4',bd=5, font=('Arial',13),command=lambda :add_digit(4)).grid(row=2,column=0, stick='wens',padx=5,pady=5 )
tk.Button(text='5',bd=5, font=('Arial',13),command=lambda :add_digit(5)).grid(row=2,column=1, stick='wens',padx=5,pady=5 )
tk.Button(text='6',bd=5, font=('Arial',13),command=lambda :add_digit(6)).grid(row=2,column=2, stick='wens',padx=5,pady=5 )
tk.Button(text='7',bd=5, font=('Arial',13),command=lambda :add_digit(7)).grid(row=3,column=0, stick='wens',padx=5,pady=5 )
tk.Button(text='8',bd=5, font=('Arial',13),command=lambda :add_digit(8)).grid(row=3,column=1, stick='wens',padx=5,pady=5 )
tk.Button(text='9',bd=5, font=('Arial',13),command=lambda :add_digit(9)).grid(row=3,column=2, stick='wens',padx=5,pady=5 )
tk.Button(text='0',bd=5, font=('Arial',13),command=lambda :add_digit(0)).grid(row=4,column=1, stick='wens',padx=5,pady=5 )
tk.Button(text='.',bd=5, font=('Arial',13),command=lambda :add_digit(".")).grid(row=4,column=0, stick='wens',padx=5,pady=5 )
tk.Button(text='+',bd=5, font=('Arial',13),command=plus_click()).grid(row=1,column=3,stick='wens',padx=5,pady=5)
tk.Button(text='-',bd=5, font=('Arial',13),command=lambda :add_digit(0)).grid(row=2,column=3, stick='wens',padx=5,pady=5 )
tk.Button(text='*',bd=5, font=('Arial',13),command=lambda :add_digit(0)).grid(row=3,column=3, stick='wens',padx=5,pady=5 )
tk.Button(text='/',bd=5, font=('Arial',13),command=lambda :add_digit(0)).grid(row=4,column=3, stick='wens',padx=5,pady=5 )
tk.Button(text='=',bd=5, font=('Arial',13),command=lambda :add_digit(0)).grid(row=4,column=2, stick='wens',padx=5,pady=5 )

win.grid_columnconfigure(0,minsize=60)
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)
win.grid_columnconfigure(3,minsize=60)

win.grid_rowconfigure(1,minsize=60)
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)

win.mainloop()