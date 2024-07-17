import pytesseract
from imaging.screen_image_getting import *
from multiprocessing import Pool
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def process_image(image_func):
    return pytesseract.image_to_string(image_func(), lang='rus+en', config='--psm 6')

def get_text():
    print("Getting text")
    image_functions = [get_screen_in_character_relics, get_screen_in_inventory, get_screen_in_uncraft]

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
    return text