from PIL import Image
import pytesseract
import time
from imaging.screen_image_getting import *
import tkinter as tk
from interface.overlay import create_overlay
from multiprocessing import Pool
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def process_image(image_func):
    return pytesseract.image_to_string(image_func(), lang='rus+en', config='--psm 6')


def main_cycle():
    root = None
    image_functions = [get_screen_in_character_relics, get_screen_in_inventory, get_screen_in_uncraft]


    while True:
        time.sleep(5)
        print("new iteration")

        with Pool(processes=3) as pool:
            results = pool.map(process_image, image_functions)

        print("got images")
        character_menu_relic_rows = [row for row in results[0].split('\n') if row.strip()]
        inventory_menu_relic_rows = [row for row in results[1].split('\n') if row.strip()]
        uncraft_menu_relic_rows = [row for row in results[2].split('\n') if row.strip()]
        text = {}
        text['character_menu_text'] = "\n".join(character_menu_relic_rows)
        text['inventory_menu_text']= "\n".join(inventory_menu_relic_rows)
        text['uncraft_menu_text']= "\n".join(uncraft_menu_relic_rows)
        print("got text")
        print(text)
        # cv2.imshow('character_menu_relic', get_screen_in_character_relics())
        # cv2.imshow('inventory_menu_relic', get_screen_in_inventory())
        # cv2.imshow('uncraft_menu_relic', get_screen_in_uncraft())
        # if cv2.waitKey(25) & 0xFF == ord("q"):
        #         cv2.destroyAllWindows()
        #         break
        
        print("creating overlay")
        root = create_overlay(text, root)
        root.update()
        # root.after(2000)
'''
В rows будет лежать для тестового артефакта
['Перчатки стрелка из -', 'грубой кожи', 'Руки .', '+15', 'Сила атаки 352', 'НР 33', 'Защита у 38', 'НР 12,0%', 'Крит. урон 12.3%']
Надо распределить все правильно. Нужен большой словарь возможных значений и условие: 
if "Такой-то стат" in row:
    ...
Но появляется проблема, делать такое для каждого стата? 


'''
# while True:
#     time.sleep(2)
#     answer = pytesseract.image_to_string(get_screen_in_character_relics(), lang='rus')
#     print(answer)
