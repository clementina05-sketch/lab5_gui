"""
Задание 1 (средняя сложность): Окно с кнопкой «Привет».
"""
import tkinter as tk


def say_hello():
    """Обработчик нажатия на кнопку."""
    print("Привет!")


def create_hello_app():
    root = tk.Tk()
    root.title("Кнопка Привет")
    root.geometry("300x150")

    # Создаем кнопку и привязываем к ней функцию say_hello
    btn = tk.Button(root, text="Нажми меня", command=say_hello)
    btn.pack(pady=40)

    root.mainloop()


if __name__ == "__main__":
    create_hello_app()