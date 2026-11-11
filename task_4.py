"""
Задание 6 (повышенная сложность): Программа «Конвертер валют».
"""
import tkinter as tk
from tkinter import messagebox


def convert_currency():
    """Функция конвертации рублей в доллары (курс фиксированный)."""
    try:
        rubles = float(entry_rubles.get())
        rate = 95.0  # Условный курс: 1 доллар = 95 рублей
        dollars = rubles / rate
        label_result.config(text=f"Это {dollars:.2f} USD")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число!")


def create_converter_app():
    root = tk.Tk()
    root.title("Конвертер валют")
    root.geometry("350x200")

    tk.Label(root, text="Сумма в рублях (RUB):").pack(pady=5)
    global entry_rubles
    entry_rubles = tk.Entry(root)
    entry_rubles.pack(pady=5)

    tk.Button(root, text="Конвертировать в USD", command=convert_currency).pack(pady=10)

    global label_result
    label_result = tk.Label(root, text="Введите сумму и нажмите кнопку.")
    label_result.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_converter_app()