"""
Задание 5 (средняя сложность): Программа со вкладками (Notebook).
"""
import tkinter as tk
from tkinter import ttk


def create_tabs_app():
    root = tk.Tk()
    root.title("Программа с вкладками")
    root.geometry("400x300")

    # Создаем Notebook (панель с вкладками)
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both', padx=10, pady=10)

    # Вкладка 1
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text='Вкладка 1')
    ttk.Label(tab1, text="Это содержимое первой вкладки.").pack(pady=20)

    # Вкладка 2
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text='Вкладка 2')
    ttk.Label(tab2, text="А это вторая вкладка!").pack(pady=20)

    # Вкладка 3
    tab3 = ttk.Frame(notebook)
    notebook.add(tab3, text='Вкладка 3')
    ttk.Label(tab3, text="Третья вкладка для примера.").pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    create_tabs_app()