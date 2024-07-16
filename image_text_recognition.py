from PIL import Image
import pytesseract
import time
from screen_image_getting import *
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

result = pytesseract.image_to_string(get_test_data(), lang='rus+en', config='--psm 6')
# print(result, type(result))
data = result.split('\n')
rows = []
for row in data:
    if row.strip():
        rows.append(row)
while True:
    cv2.imshow('screen', np.array(get_test_data()))
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
print(rows)
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
