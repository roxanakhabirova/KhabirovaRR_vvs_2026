import tkinter as tk
from tkinter import ttk, messagebox
from calc import DISCOUNTS, check_numbers, calc_discount


def count_click():
    ok, res = check_numbers(entry_price.get(), entry_count.get())
    if not ok:
        messagebox.showerror("Ошибка", res)
        return

    price, count = res
    total, saved = calc_discount(price, count, card_box.get(), promo_var.get())
    result_label.config(text="К оплате: " + str(total) + " руб. (скидка " + str(saved) + " руб.)")


def clear_click():
    entry_price.delete(0, tk.END)
    entry_count.delete(0, tk.END)
    card_box.current(0)
    promo_var.set(False)
    result_label.config(text="К оплате: —")


# Главное окно
root = tk.Tk()
root.title("Калькулятор скидки (Tkinter)")
root.geometry("400x300")

tk.Label(root, text="Расчёт цены со скидкой", font=("Arial", 13, "bold")).pack(pady=10)

# Рамка для полей ввода
box = tk.Frame(root)
box.pack(pady=5)

tk.Label(box, text="Цена за 1 шт (руб.):").grid(row=0, column=0, sticky="w", pady=4)
entry_price = tk.Entry(box, width=20)
entry_price.grid(row=0, column=1, padx=5, pady=4)

tk.Label(box, text="Количество (шт.):").grid(row=1, column=0, sticky="w", pady=4)
entry_count = tk.Entry(box, width=20)
entry_count.grid(row=1, column=1, padx=5, pady=4)

tk.Label(box, text="Карта клиента:").grid(row=2, column=0, sticky="w", pady=4)
card_box = ttk.Combobox(box, values=list(DISCOUNTS.keys()), state="readonly", width=18)
card_box.current(0)
card_box.grid(row=2, column=1, padx=5, pady=4)

promo_var = tk.BooleanVar()
tk.Checkbutton(box, text="Есть промокод (+5%)", variable=promo_var).grid(row=3, column=0, columnspan=2, pady=5)

# Кнопки
btns = tk.Frame(root)
btns.pack(pady=10)

tk.Button(btns, text="Посчитать", width=12, command=count_click).pack(side="left", padx=5)
tk.Button(btns, text="Очистить", width=12, command=clear_click).pack(side="left", padx=5)

# Результат
result_label = tk.Label(root, text="К оплате: —", font=("Arial", 11, "bold"))
result_label.pack(pady=10)

root.mainloop()