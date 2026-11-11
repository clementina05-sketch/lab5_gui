"""
Задание 7 (средняя сложность): Окно с меню (File→Exit).
"""
import tkinter as tk


def create_menu_app():
    root = tk.Tk()
    root.title("Меню File -> Exit")
    root.geometry("300x200")

    # Создаем главное меню
    menubar = tk.Menu(root)

    # Создаем выпадающее меню "File"
    file_menu = tk.Menu(menubar, tearoff=0)
    # Добавляем пункт Exit, который закрывает программу
    file_menu.add_command(label="Exit", command=root.quit)

    # Добавляем меню File в главное меню
    menubar.add_cascade(label="File", menu=file_menu)

    # Устанавливаем меню в окно
    root.config(menu=menubar)

    tk.Label(root, text="Нажмите File -> Exit, чтобы закрыть.").pack(pady=50)

    root.mainloop()


if __name__ == "__main__":
    create_menu_app()