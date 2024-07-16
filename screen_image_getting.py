import numpy as np
import cv2
from mss import mss
from PIL import Image

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
