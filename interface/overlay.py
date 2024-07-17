import tkinter as tk

def create_overlay(text: dict, overlay):
    # Создаем главное окно
    if overlay is None:
        character_menu_text = text['character_menu_text']
        inventory_menu_text = text['inventory_menu_text']
        uncraft_menu_text = text['uncraft_menu_text']

        overlay = tk.Tk()
        width = 300
        height = 200
        overlay.overrideredirect(True)  # Убираем рамку окна
        overlay.geometry(f'{width}x{height}+650+0')  # Устанавливаем размер окна и его позицию (в верхнем левом углу)
        overlay.attributes('-topmost', True)  # Устанавливаем окно поверх всех остальных
        

        # Настроем сетку
        overlay.columnconfigure(0, weight=1)
        overlay.columnconfigure(1, weight=1)
        overlay.columnconfigure(2, weight=1)
        overlay.rowconfigure(0, weight=1)
        overlay.rowconfigure(1, weight=30)

        # Создаем метку с текстом
        label = tk.Label(overlay, text="choose source", font=('Helvetica', 10), fg='white', bg='black', wraplength=480)
        label.grid(row=1, column=0, columnspan=3, padx=6, pady=6, sticky=tk.NSEW)
        
        # Обработка текста
        def character_menu_click():
            label.config(text=character_menu_text)
            overlay.source = "character_menu_text"

        def inventory_menu_click():
            label.config(text=inventory_menu_text)
            overlay.source = "inventory_menu_text"
        
        def uncraft_menu_click():
            label.config(text=uncraft_menu_text)
            overlay.source = "uncraft_menu_text"

        # Создадим выбор источника
        tab1 = tk.Button(overlay, text="Character", font=('Helvetica', 10), fg='white', bg='black', command=character_menu_click)
        tab2 = tk.Button(overlay, text="Inventory", font=('Helvetica', 10), fg='white', bg='black', command=inventory_menu_click)
        tab3 = tk.Button(overlay, text="Destroy", font=('Helvetica', 10), fg='white', bg='black', command=uncraft_menu_click)

        # Позиционируем "вкладки"
        tab1.grid(row=0, column=0, padx=4, pady=2, sticky=tk.NSEW)
        tab2.grid(row=0, column=1, padx=4, pady=2, sticky=tk.NSEW)
        tab3.grid(row=0, column=2, padx=4, pady=2, sticky=tk.NSEW)

        # Создадим функцию для перетаскивания окна
        def move(event):
            x, y = overlay.winfo_pointerxy()
            overlay.geometry(f"+{x-int(width/2)}+{y-int(height/2)}")
            # overlay.geometry(f"+{x}+{y}")
        # Привязываем функцию к действию
        overlay.bind('<B1-Motion>',move)

        # Закрытие окна по клику
        overlay.bind("<Escape>", lambda e: overlay.destroy())

        overlay.label = label
    else:
        source = overlay.source if hasattr(overlay, 'source') else 'character_menu_text'
        overlay.label.config(text=text[source])

    return overlay

