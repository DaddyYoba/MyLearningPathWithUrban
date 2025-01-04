import random
import tkinter as tk
from tkinter import ttk
def get_numbers():
    if number1_entry.get().isdecimal() and number2_entry.get().isdecimal():
        num1 = int(number1_entry.get())
        num2 = int(number2_entry.get())
        return num1, num2
    return 'Error', 'Error'

def place_answer(res):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, res)

def addition():
    number1, number2 = get_numbers()
    if number1 == 'Error' or number2 == 'Error':
        place_answer('Требуются целые числа')
    else:
        place_answer(number1 + number2 + variation)

def subtraction():
    number1, number2 = get_numbers()
    if number1 == 'Error' or number2 == 'Error':
        place_answer('Требуются целые числа')
    else:
        place_answer(number1 - number2 - variation)

def multiplication():
    number1, number2 = get_numbers()
    if number1 == 'Error' or number2 == 'Error':
        place_answer('Требуются целые числа')
    else:
        place_answer(number1 * number2 + variation * 2)

def division():
    number1, number2 = get_numbers()
    if number1 == 'Error' or number2 == 'Error':
        place_answer('Требуются целые числа')
    elif number2 == 0:
        place_answer('На ноль делить нельзя')
    else:
        place_answer(round(number1 / number2 + variation / 2, 2))

def troll():
    global variation
    if random.randint(1,10) % 5 == 0:
        variation = random.randint(1,3)
        troll_w = tk.Toplevel()

        label = tk.Label(troll_w, text="Бу! Испугался? Не бойся, я друг, я тебя не обижу.\nИди сюда, иди ко мне, сядь рядом со мной, посмотри мне в глаза.\nТы видишь меня? Я тоже тебя вижу.\nДавай смотреть друг на друга до тех пор, пока наши глаза не устанут.\nТы не хочешь? Почему? Что-то не так?")
        label.pack(fill='x', padx=50, pady=5)

        button_close = tk.Button(troll_w, text="Сесть рядом", command=troll_w.destroy)
        button_close.pack(fill='x')
window = tk.Tk()

variation = 0

style = ttk.Style()
style.theme_use('xpnative')
window.title('Калькулятор')
window.geometry('345x190')
window.resizable(False,False)


button_add = ttk.Button(window, text = '+', width=5, command = addition)
button_add.place(x = 130, y = 107)


button_sub = ttk.Button(window, text = '-', width=5, command = subtraction)
button_sub.place(x = 180, y = 108)


button_mul = ttk.Button(window, text = '*', width=5, command = multiplication)
button_mul.place(x = 230, y = 109)


button_div = ttk.Button(window, text = '/', width=5, command = division)
button_div.place(x = 280, y = 110)

button_troll = ttk.Button(window, command = troll)
button_troll.place(x = 334, y = 183)

number1_entry = ttk.Entry(window, width=20, font='Arial 14')
number1_entry.place(x = 110, y = 20)
number2_entry = ttk.Entry(window, width=20, font='Arial 14')
number2_entry.place(x = 110, y = 60)

answer_entry = ttk.Entry(window, width=20, font='Arial 14', justify='center')
answer_entry.place(x = 110, y = 150)

number1_label = ttk.Label(window, text='Введите первое\nчисло:', justify='right', font='Arial 10')
number1_label.place(x = 5, y = 15)
number2_label = ttk.Label(window, text='Введите второе\nчисло:', justify='right', font='Arial 10')
number2_label.place(x = 5, y = 55)
answer_label = ttk.Label(window, text='Ответ:', justify='right', font='Arial 10')
answer_label.place(x = 62, y = 153)

window.mainloop()