import numpy as np
import cv2
from mss import mss
from PIL import Image
import time

def get_test_data():
    image_path = 'test_data/test.png'
    image = cv2.imread(image_path)
    # Убрать иконки замка и мусорки
    x, y, w, h = 450, 0, 100, 150  
    image[y:y+h, x:x+w] = (0, 0, 0)
    # Убрать иконки статов
    x, y, w, h = 0, 180, 60, 500  
    image[y:y+h, x:x+w] = (0, 0, 0)
    # Преобразуем изображение в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Применим бинаризацию для улучшения качества распознавания
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    # Уберем шум с изображения
    binary = cv2.medianBlur(binary, 3)
    # Преобразуем изображение в формат PIL
    pil_image = Image.fromarray(binary)
    return pil_image

def get_screen_in_character_relics():
    '''
        Returns screenshot as numpy array
    '''
    with mss() as sct:
        bounding_box = {'top': 150, 'left': 1480, 'width': 420, 'height': 350}
        sct_img = sct.grab(bounding_box)
        image = np.asarray(sct_img)
        return image

def get_screen_in_inventory():
    '''
        Returns screenshot as numpy array
    '''
    with mss() as sct:
        bounding_box = {'top': 120, 'left': 1380, 'width': 480, 'height': 480}
        sct_img = sct.grab(bounding_box)
        image = np.asarray(sct_img)
        return image

def get_screen_in_uncraft():
    '''
        Returns screenshot as numpy array
    '''
    with mss() as sct:
        bounding_box = {'top': 120, 'left': 40, 'width': 450, 'height': 480}
        sct_img = sct.grab(bounding_box)
        image = np.asarray(sct_img)
        return image
    
# sct = mss()
# bounding_box = {'top': 120, 'left': 40, 'width': 450, 'height': 480}

# while True:
#     sct_img = sct.grab(bounding_box)
#     cv2.imshow('screen', np.array(sct_img))

#     if (cv2.waitKey(1) & 0xFF) == ord('q'):
#         cv2.destroyAllWindows()
#         break
