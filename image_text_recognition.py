from PIL import Image
import pytesseract
import time
from screen_image_getting import get_screen_in_character_relics
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

while True:
    time.sleep(2)
    print(pytesseract.image_to_string(get_screen_in_character_relics(), lang='rus'))
