import tkinter as tk

def create_overlay(text):
    # Создаем главное окно
    root = tk.Tk()
    root.overrideredirect(True)  # Убираем рамку окна
    root.geometry('300x100+0+0')  # Устанавливаем размер окна и его позицию (300x100 пикселей, в верхнем левом углу)
    root.attributes('-topmost', True)  # Устанавливаем окно поверх всех остальных

    # Создаем метку с текстом
    label = tk.Label(root, text=text, font=('Helvetica', 20), fg='white', bg='black', wraplength=280)
    label.pack(expand=True, fill='both', padx=10, pady=10)

    # Закрытие окна по клику
    label.bind("<Button-1>", lambda e: root.destroy())

    # Запускаем главный цикл приложения
    root.mainloop()

# Пример использования
create_overlay("Ваш текст здесь. Это пример длинного текста, который должен переноситься на несколько строк.")
