"""
Задание 8 (повышенная сложность): Программа с несколькими окнами.
"""
import tkinter as tk


def open_second_window():
    """Создает и открывает второе окно."""
    second_window = tk.Toplevel(root)
    second_window.title("Второе окно")
    second_window.geometry("250x150")
    tk.Label(second_window, text="Это новое окно!").pack(pady=40)
    
    # Кнопка для закрытия второго окна
    tk.Button(second_window, text="Закрыть", command=second_window.destroy).pack()


def create_multi_window_app():
    global root
    root = tk.Tk()
    root.title("Главное окно")
    root.geometry("300x200")

    tk.Label(root, text="Добро пожаловать!").pack(pady=10)
    tk.Button(root, text="Открыть второе окно", command=open_second_window).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    create_multi_window_app()