# Разработать программу с применением пакета tk, взяв в качестве условия
# задачу 3_1

import tkinter as tk
from tkinter import messagebox


def check_values():
    x = int(entry_x.get())
    y = int(entry_y.get())

    if x > 0 and y < 0:  # проверка  в какой четверти находится координата
        messagebox.showinfo("Результат", "True")
    else:
        messagebox.showinfo("Результат", "False")


# Создание основного окна
window = tk.Tk()
window.title("Проверка чисел на противоположность")

# Метки и поля для ввода чисел
tk.Label(window, text="Введите x число:").grid(row=0, column=0, padx=10, pady=5)
entry_x = tk.Entry(window)
entry_x.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Введите y число:").grid(row=1, column=0, padx=10, pady=5)
entry_y = tk.Entry(window)
entry_y.grid(row=1, column=1, padx=10, pady=5)


# Кнопка для проверки значений
check_button = tk.Button(window, text="Проверить", command=check_values)
check_button.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()