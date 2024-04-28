#import
import pandas as pd
from PIL import Image
import ast
import os
import cv2
import csv


#file check function
def check_folder_exists(path):
        if not os.path.exists(path):
            try:
                os.makedirs(path)
                print ('create ' + path)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
                    
                    
#set parameters
root = './images/'
dst = './train/'
seed_arr = []

file = open('labels.csv', 'r', encoding='utf-8')
csv_reader = csv.reader(file)

check_folder_exists(dst)


#read csv data
for index, line in enumerate(csv_reader):
    # pass csv header == index[0]
    if index == 0:
        continue
    seed_arr.append(line)
file.close()

#sorting data
seed_arr.sort()
print(str(len(seed_arr)))
print(str(seed_arr))         
                    
                    
# img read, crop save
for index, line in enumerate(seed_arr):
    
    filename = line[0]
    width = line[1]
    height = line[2]
    class_name = line[3]
    xmin = line[4]
    ymin = line[5]
    xmax = line[6]
    ymax = line[7]
    
    
    #load img path
    load_img_path = os.path.join(root, filename)
    
    #save img path
    save_class_path = os.path.join(dst, class_name)
    check_folder_exists(save_class_path)
    save_img_path = os.path.join(save_class_path, str(index) +".jpg")
    
    img = Image.open(load_img_path)
    crop_img = img.crop((int(xmin) ,int(ymin) ,int(xmax) ,int(ymax)))
    newsize = (224, 224) 
    im1 = crop_img.resize(newsize) 
    im1.save(save_img_path, 'JPEG')
    print('save ' + save_img_path)
file.close() 
    
