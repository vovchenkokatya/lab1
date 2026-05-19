import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        a1 = float(entry_a1.get())
        b1 = float(entry_b1.get())
        c1 = float(entry_c1.get())

        a2 = float(entry_a2.get())
        b2 = float(entry_b2.get())
        c2 = float(entry_c2.get())

        delta = a1 * b2 - a2 * b1
        delta_x = c1 * b2 - c2 * b1
        delta_y = a1 * c2 - a2 * c1

        if delta != 0:
            x = delta_x / delta
            y = delta_y / delta
            label_result.config(text=f"x = {x:g}      y = {y:g}")
        else:
            if delta_x == 0 and delta_y == 0:
                label_result.config(text="Безліч розв'язків")
            else:
                label_result.config(text="Немає розв'язків")

    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть коректні числові значення.")

def close_app():
    root.destroy()

root = tk.Tk()
root.title("tk")
root.config(padx=10, pady=10)

entry_a1 = tk.Entry(root, width=5)
entry_a1.grid(row=0, column=0, padx=2, pady=5)

label_x1 = tk.Label(root, text="x + ")
label_x1.grid(row=0, column=1)

entry_b1 = tk.Entry(root, width=5)
entry_b1.grid(row=0, column=2, padx=2, pady=5)

label_y1 = tk.Label(root, text="y = ")
label_y1.grid(row=0, column=3)

entry_c1 = tk.Entry(root, width=5)
entry_c1.grid(row=0, column=4, padx=2, pady=5)

entry_a2 = tk.Entry(root, width=5)
entry_a2.grid(row=1, column=0, padx=2, pady=5)

label_x2 = tk.Label(root, text="x + ")
label_x2.grid(row=1, column=1)

entry_b2 = tk.Entry(root, width=5)
entry_b2.grid(row=1, column=2, padx=2, pady=5)

label_y2 = tk.Label(root, text="y = ")
label_y2.grid(row=1, column=3)

entry_c2 = tk.Entry(root, width=5)
entry_c2.grid(row=1, column=4, padx=2, pady=5)

label_result = tk.Label(root, text="x =         y =   ", font=("Arial", 12))
label_result.grid(row=2, column=0, columnspan=5, pady=10)

btn_calc = tk.Button(root, text="Обчислити", command=calculate)
btn_calc.grid(row=3, column=0, columnspan=2, sticky="w", pady=5)
btn_close = tk.Button(root, text="Закрити", command=close_app)
btn_close.grid(row=3, column=3, columnspan=2, sticky="e", pady=5)

root.mainloop()