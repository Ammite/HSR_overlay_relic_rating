import tkinter as tk

def create_overlay(text = ""):
    '''
    text divided to 3 parts
    One part for one source (inventory, character, uncraft)
    button for choosing source
    text is str or object to divide by parts to display in grid
    tkinter wiki: https://metanit.com/python/tkinter/2.6.php
    '''

    
    character_menu_text = "Rating: S\n"
    character_menu_text += "Good for: DoT\n"
    character_menu_text += "Crit Chance: 10%\n"
    character_menu_text += " \tHP: 10\n \tDEF: 10\n \tATK: 10\n \tCrit Damage: 20%"

    inventory_menu_text = "Rating: A\n"
    inventory_menu_text += "Good for: Crit hero\n"
    inventory_menu_text += "Crit Chance: 20%\n"
    inventory_menu_text += " \tHP: 20\n \tDEF: 20\n \tATK: 20\n \tCrit Damage: 30%"

    uncraft_menu_text = "Rating: B\n"
    uncraft_menu_text += "Good for: Break effect hero\n"
    uncraft_menu_text += "Crit Chance: 15%\n"
    uncraft_menu_text += " \tHP: 15\n \tDEF: 15\n \tATK: 15\n \tCrit Damage: 25%"

    text = "Choose source!"

    overlay = tk.Tk()
    width = 300
    height = 200
    overlay.overrideredirect(True)  # Убираем рамку окна
    overlay.geometry(f'{width}x{height}+650+0')  # Устанавливаем размер окна и его позицию (300x100 пикселей, в верхнем левом углу)
    overlay.attributes('-topmost', True)  # Устанавливаем окно поверх всех остальных
    
    def move(event):
        x, y = overlay.winfo_pointerxy()
        overlay.geometry(f"+{x-int(width/2)}+{y-int(height/2)}")
        # overlay.geometry(f"+{x}+{y}")
    
    overlay.bind('<B1-Motion>',move)

    # Настроем сетку
    overlay.columnconfigure(0, weight=1)
    overlay.columnconfigure(1, weight=1)
    overlay.columnconfigure(2, weight=1)
    overlay.rowconfigure(0, weight=1)
    overlay.rowconfigure(1, weight=30)
    
    # Обработка текста
    def character_menu_click():
        label.config(text=character_menu_text)

    def inventory_menu_click():
        label.config(text=inventory_menu_text)
    
    def uncraft_menu_click():
        label.config(text=uncraft_menu_text)

    # Создадим выбор источника
    tab1 = tk.Button(overlay, text="Character", font=('Helvetica', 10), fg='white', bg='black', command=character_menu_click)
    tab2 = tk.Button(overlay, text="Inventory", font=('Helvetica', 10), fg='white', bg='black', command=inventory_menu_click)
    tab3 = tk.Button(overlay, text="Destroy", font=('Helvetica', 10), fg='white', bg='black', command=uncraft_menu_click)

    # Позиционируем "вкладки"
    tab1.grid(row=0, column=0, padx=4, pady=2, sticky=tk.NSEW)
    tab2.grid(row=0, column=1, padx=4, pady=2, sticky=tk.NSEW)
    tab3.grid(row=0, column=2, padx=4, pady=2, sticky=tk.NSEW)

    # Создаем метку с текстом
    label = tk.Label(overlay, text=text, font=('Helvetica', 10), fg='white', bg='black', wraplength=480)
    label.grid(row=1, column=0, columnspan=3, padx=6, pady=6, sticky=tk.NSEW)


    # Закрытие окна по клику
    overlay.bind("<Escape>", lambda e: overlay.destroy())
    
    overlay.mainloop()

if __name__ == '__main__':
    create_overlay()