import tkinter as tk
import messagebox as mb

def add():
    a = e1.get().strip()
    try:
        a = int(a)
    except ValueError:
        mb.showerror("Ошибка", "В первое окно должно быть введено целое число")
        return
    b = e2.get()
    try:
        b = int(b)
    except ValueError:
        mb.showerror("Ошибка", "В первое окно должно быть введено целое число")
        return
    c = e3.get()
    try:
        c = int(c)
    except ValueError:
        mb.showerror("Ошибка", "В первое окно должно быть введено целое число")
        return
    m2.config (text=f"{a} + {b} + {c} = {a + b + c}")

def sub():
    a = e1.get().strip()
    try:
        a = int(a)
    except ValueError:
        mb.showerror("Ошибка", "В первое окно должно быть введено целое число")
        return
    b = e2.get()
    try:
        b = int(b)
    except ValueError:
        mb.showerror("Ошибка", "В первое окно должно быть введено целое число")
        return
    c = e3.get()
    try:
        c = int(c)
    except ValueError:
        mb.showerror("Ошибка", "В первое окно должно быть введено целое число")
        return
    m2.config (text=f"{a} * {b} * {c} = {a * b * c}")

window = tk.Tk()
window.title("Калькулятор")

m1 = tk.Label(window, text='Введите три числа  и нажмите на кнопку для вычисления '
                          'суммы или произведения', height=3)
m1.pack()


e1 = tk.Entry(window, justify="center")
e1.pack()
e2 = tk.Entry(window, justify="center")
e2.pack()
e3 = tk.Entry(window, justify="center")
e3.pack()

b1 = tk.Button(window, text=" Сложить три числа", command=add)
b1.pack()
b2 = tk.Button(window, text=" Умножить три числа", command=sub)
b2.pack()

m2 = tk.Label(window, text="", height=3)
m2.pack()

window.mainloop()



