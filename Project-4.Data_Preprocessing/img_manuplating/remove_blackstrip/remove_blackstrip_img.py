import os
import cv2
import numpy as np

barcode_list = sorted(os.listdir('./'))

for barcode in barcode_list:
    barcode_path = os.path.join('./', barcode)
    img_list = sorted(os.listdir(barcode_path))
    for img in img_list:
        img_path = os.path.join(barcode_path, img)
        image = cv2.imread(img_path)
        if np.allclose(image[0][0], [0,0,0]) or sum(image[0][0]) < 10:
            print barcode, img
            os.remove(img_path)
        elif np.allclose(image[-1][-1], [0,0,0]) or sum(image[-1][-1]) < 10:
            print barcode, img
            os.remove(img_path)
        elif np.allclose(image[-1][0], [0,0,0]) or sum(image[-1][0]) < 10:
            print barcode, img
            os.remove(img_path)            
        elif np.allclose(image[0][-1], [0,0,0]) or sum(image[0][-1]) < 10:
            print barcode, img
            os.remove(img_path)

