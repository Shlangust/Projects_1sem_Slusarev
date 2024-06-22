# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу

import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Параметры скидки")
root.geometry("600x700")
root.configure(bg="white")

# Create the main frame
main_frame = tk.Frame(root, bg="white", padx=10, pady=10)
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Activate Checkbox
active_var = tk.BooleanVar(value=True)
active_check = tk.Checkbutton(main_frame, text="Активность:", variable=active_var, bg="white")
active_check.grid(row=0, column=0, columnspan=2, sticky=tk.W)

# Name Label and Entry
name_label = tk.Label(main_frame, text="Название:", bg="white")
name_label.grid(row=1, column=0, sticky=tk.W, pady=5)
name_entry = tk.Entry(main_frame, width=50)
name_entry.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)

# Site Label and Combobox
site_label = tk.Label(main_frame, text="Сайт:", bg="white")
site_label.grid(row=2, column=0, sticky=tk.W, pady=5)
site_combobox = ttk.Combobox(main_frame, values=["(s1) Моя компания"], state="readonly")
site_combobox.current(0)
site_combobox.grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)

# Period of Activity Label and Entries
period_label = tk.Label(main_frame, text="Период активности:", bg="white")
period_label.grid(row=3, column=0, sticky=tk.W, pady=5)
period_start_entry = tk.Entry(main_frame)
period_start_entry.grid(row=3, column=1, pady=5)
period_end_entry = tk.Entry(main_frame)
period_end_entry.grid(row=3, column=2, pady=5)

# Type of Discount Label and Combobox
discount_type_label = tk.Label(main_frame, text="Тип скидки:", bg="white")
discount_type_label.grid(row=4, column=0, sticky=tk.W, pady=5)
discount_type_combobox = ttk.Combobox(main_frame, values=["В процентах"], state="readonly")
discount_type_combobox.current(0)
discount_type_combobox.grid(row=4, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)

# Amount of Discount Label and Entry
discount_amount_label = tk.Label(main_frame, text="Величина скидки:", bg="white")
discount_amount_label.grid(row=5, column=0, sticky=tk.W, pady=5)
discount_amount_entry = tk.Entry(main_frame)
discount_amount_entry.grid(row=5, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)

# Currency Label and Combobox
currency_label = tk.Label(main_frame, text="Валюта скидки:", bg="white")
currency_label.grid(row=6, column=0, sticky=tk.W, pady=5)
currency_combobox = ttk.Combobox(main_frame, values=["RUB"], state="readonly")
currency_combobox.current(0)
currency_combobox.grid(row=6, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)

# Maximum Discount Amount Label and Entry
max_discount_label = tk.Label(main_frame, text="Максимальная сумма скидки (в валюте скидки):", bg="white")
max_discount_label.grid(row=7, column=0, columnspan=2, sticky=tk.W, pady=5)
max_discount_entry = tk.Entry(main_frame)
max_discount_entry.grid(row=7, column=2, sticky=(tk.W, tk.E), pady=5)

# Apply to Subscription Checkbox
apply_subscription_var = tk.BooleanVar()
apply_subscription_check = tk.Checkbutton(main_frame, text="Применяется к продлению подписки", variable=apply_subscription_var, bg="white")
apply_subscription_check.grid(row=8, column=0, columnspan=3, sticky=tk.W, pady=5)

# Priority Label and Entry
priority_label = tk.Label(main_frame, text="Приоритет применимости:", bg="white")
priority_label.grid(row=9, column=0, columnspan=2, sticky=tk.W, pady=5)
priority_entry = tk.Entry(main_frame)
priority_entry.grid(row=9, column=2, sticky=(tk.W, tk.E), pady=5)

# Stop Further Discounts Checkbox
stop_discounts_var = tk.BooleanVar()
stop_discounts_check = tk.Checkbutton(main_frame, text="Прекратить дальнейшее применение скидок:", variable=stop_discounts_var, bg="white")
stop_discounts_check.grid(row=10, column=0, columnspan=3, sticky=tk.W, pady=5)

# Short Description Label and Entry
short_desc_label = tk.Label(main_frame, text="Краткое описание (до 255 символов):", bg="white")
short_desc_label.grid(row=11, column=0, columnspan=3, sticky=tk.W, pady=5)
short_desc_entry = tk.Text(main_frame, height=5, width=50)
short_desc_entry.grid(row=12, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)

# Buttons
button_frame = tk.Frame(main_frame, bg="white")
button_frame.grid(row=13, column=0, columnspan=3, pady=10)
save_button = tk.Button(button_frame, text="Сохранить")
save_button.grid(row=0, column=0, padx=5)
apply_button = tk.Button(button_frame, text="Применить")
apply_button.grid(row=0, column=1, padx=5)
cancel_button = tk.Button(button_frame, text="Отменить")
cancel_button.grid(row=0, column=2, padx=5)

# Run the application
root.mainloop()