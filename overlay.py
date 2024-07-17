import tkinter as tk

def create_overlay(text, root):
    # Создаем главное окно
    if root is None:
        root = tk.Tk()
        root.overrideredirect(True)  # Убираем рамку окна
        root.geometry('700x300+650+0')  # Устанавливаем размер окна и его позицию (300x100 пикселей, в верхнем левом углу)
        root.attributes('-topmost', True)  # Устанавливаем окно поверх всех остальных

        # Создаем метку с текстом
        label = tk.Label(root, text=text, font=('Helvetica', 10), fg='white', bg='black', wraplength=480)
        label.pack(expand=True, fill='both', padx=10, pady=10)

        # Закрытие окна по клику
        label.bind("<Button-1>", lambda e: root.destroy())
        root.label = label
    else:
        root.label.config(text=text)

    return root

