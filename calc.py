import tkinter as tk
from tkinter import messagebox
def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
    elif event.char == '\x08':
        clear()


win = tk.Tk()
win.title('Калькулятор')
win.geometry("240x275+100+200")
win.config(bg='#808080')
win.resizable(False, False)
#photo = tk.PhotoImage(file='calc.png', width=900, height=1000)
#win.iconphoto(False, photo)

win.bind('<Key>', press_key)

def press_key(event):
    print(event)

# операция для кнопок
def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value+digit)

# опреация для 0
def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value+operation)

# операция для =
def calculate():
    value = calc.get()
    if value[-1] in '+-*/':
        value = value+value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError, EnvironmentError):
        messagebox.showinfo('Внимание', 'Нужно только цифры! Вы ввели другие символы')
        calc.insert(0, 0)
    except (NameError, SyntaxError, EnvironmentError):
        messagebox.showinfo('Внимание', 'На ноль делить нельзя!')
        calc.insert(0, 0)


# операция для С

def clear():
    calc.delete(0, tk.END)
    calc.insert(0,0)

# поле ввода
calc = tk.Entry(win, justify=tk.RIGHT, bd=5, font=('Arial', 15), width=15)
# в начале нолик
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick = 'we', padx=5)

# функция для создания кнопки
def make_digit_button(digit):
    return tk.Button(text=digit, bd = 5, font=('Arial', 13), command=lambda : add_digit(digit))

# функция для создания операции
def make_operation_button(operation):
    return tk.Button(text=operation, bd = 5, font=('Arial', 13), command=lambda : add_operation(operation))

# =
def make_calc_button(operation):
    return tk.Button(text=operation, bd = 5, font=('Arial', 13), command=calculate)

# C
def make_clear_button(operation):
    return tk.Button(text=operation, bd = 5, font=('Arial', 13), command=clear)

# кнопки
make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

# операции
make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)

# =
make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)

# очищение
make_clear_button('С').grid(row=4, column=1, stick='wens', padx=5, pady=5)

# для растягивания кнопок
win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()