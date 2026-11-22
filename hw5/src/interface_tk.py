import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk

import validators
from calculus import calc_integral
from vis import make_plot_image


class SimpleIntegralTk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор интегралов (Tkinter)")
        self.geometry("950x620")
        self.configure(bg="#f4f6f9")

        # Верхняя панель
        top_frame = tk.Frame(self, bg="#ffffff", bd=1, relief="solid")
        top_frame.pack(side="top", fill="x", padx=10, pady=8)

        tk.Label(top_frame, text="Численное интегрирование", font=("Arial", 12, "bold"), bg="#ffffff").pack(side="left", padx=10, pady=8)
        self.result_text = tk.StringVar(value="Ответ: пока не посчитано")
        tk.Label(top_frame, textvariable=self.result_text, font=("Arial", 12), fg="#1d3557", bg="#ffffff").pack(side="left", padx=10)

        # Место под картинку графика
        plot_frame = tk.Frame(self, bg="#ffffff", bd=1, relief="solid")
        plot_frame.pack(side="top", expand=True, fill="both", padx=10, pady=5)

        self.plot_label = tk.Label(plot_frame, bg="#ffffff")
        self.plot_label.pack(expand=True, fill="both", padx=5, pady=5)

        # Панель управления снизу
        bottom_frame = tk.LabelFrame(self, text="Параметры", padx=10, pady=10, bg="#f4f6f9")
        bottom_frame.pack(side="bottom", fill="x", padx=10, pady=8)

        # Выбор метода
        method_box = tk.Frame(bottom_frame, bg="#f4f6f9")
        method_box.pack(side="left", padx=8)
        tk.Label(method_box, text="Метод:", bg="#f4f6f9").pack(anchor="w")
        self.method_list = tk.Listbox(method_box, width=12, height=3, exportselection=False)
        for m in validators.MODES:
            self.method_list.insert(tk.END, m)
        self.method_list.selection_set(validators.DEFAULT_MODE_INDEX)
        self.method_list.pack()

        # Поля ввода L, R, N
        self.left_entry = self.make_field(bottom_frame, "Граница L:")
        self.right_entry = self.make_field(bottom_frame, "Граница R:")
        self.n_entry = self.make_field(bottom_frame, "Число N:")

        # Поле для формулы
        f_box = tk.Frame(bottom_frame, bg="#f4f6f9")
        f_box.pack(side="left", padx=8, fill="x", expand=True)
        tk.Label(f_box, text="Формула f(x):", bg="#f4f6f9").pack(anchor="w")
        self.formula_entry = tk.Entry(f_box, font=("Courier", 11))
        self.formula_entry.pack(fill="x", pady=4)

        # Кнопка старта
        btn = tk.Button(bottom_frame, text="Посчитать", command=self.run_calc, bg="#2b6cb0", fg="white", font=("Arial", 10, "bold"), padx=12, pady=6)
        btn.pack(side="left", padx=10)

        self.mainloop()

    def make_field(self, parent, label_text):
        box = tk.Frame(parent, bg="#f4f6f9")
        box.pack(side="left", padx=8)
        tk.Label(box, text=label_text, bg="#f4f6f9").pack(anchor="w")
        entry = tk.Entry(box, width=12)
        entry.pack(pady=4)
        return entry

    def run_calc(self):
        selected = self.method_list.curselection()
        if not selected:
            messagebox.showerror("Ошибка", "Выберите метод!")
            return

        mode = self.method_list.get(selected[0])
        left_text = self.left_entry.get()
        right_text = self.right_entry.get()
        n_text = self.n_entry.get()
        formula_text = self.formula_entry.get()

        if not validators.check_limits(left_text, right_text):
            messagebox.showerror("Ошибка", "Проверьте границы L и R (R должно быть больше L).")
            return

        if not validators.is_positive_int(n_text):
            messagebox.showerror("Ошибка", "N должно быть целым положительным числом.")
            return

        try:
            func = validators.build_function(formula_text)
            func(1)
        except Exception:
            messagebox.showerror("Ошибка", "Проверьте формулу f(x).")
            return

        left = float(left_text)
        right = float(right_text)
        count = int(n_text)

        total, x_vals, y_vals, bar_x, bar_align, step = calc_integral(func, left, right, count, mode)
        img = make_plot_image(func, left, right, count, mode, total, x_vals, y_vals, bar_x, bar_align, step)

        tk_img = ImageTk.PhotoImage(img)
        self.plot_label.config(image=tk_img)
        self.plot_label.image = tk_img
        self.result_text.set("Ответ: " + str(round(total, 5)))


if __name__ == "__main__":
    SimpleIntegralTk()