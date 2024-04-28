import numpy as np
import pandas as pd
import cv2
from glob import glob
import os
import pathlib
import matplotlib.pyplot as plt
from tqdm import tqdm

img_dir = '/home/home/sudip/mini_project/augmentation/test/images'
result = []
idx = 0

label_list = [f for f in os.listdir(img_dir) if not f.startswith('.')]

for label in label_list:
    file_list = glob(os.path.join(img_dir,label,'*'))
    
    for file in file_list:
        result.append([idx, label, file])
        idx += 1
        
img_df = pd.DataFrame(result, columns=['idx','label','image_path'])


#print(img_df)


#plt.figure(figuresize=(5,5))
#img_df['label'].value_counts().sort_index().plt.barh()
#img_df['label'].value_counts().sort_index()



from albumentations import (
    HorizontalFlip, IAAPerspective, ShiftScaleRotate, CLAHE, RandomRotate90, RandomGamma, VerticalFlip,
    Transpose, ShiftScaleRotate, Blur, OpticalDistortion, GridDistortion, HueSaturationValue, 
    IAAAdditiveGaussianNoise, GaussNoise, MotionBlur, MedianBlur, RandomBrightnessContrast, IAAPiecewiseAffine,
    IAASharpen, IAAEmboss, Flip, OneOf, Compose, Rotate, RandomContrast, RandomBrightness, RandomCrop, Resize, OpticalDistortion
)


# 음료 classification용

transforms = Compose([
        #Rotate(limit=30, p=0.5),
        #Rotate(limit=180, p=0.5),
        #RandomRotate90(p=1.0)
        #Transpose(p=1.0)
        Resize(248,248, p=0.5),     # resize 후 크롭
        RandomCrop(224,224, p=0.5),  # 위에꺼랑 세트
        
        OneOf([
        RandomContrast(p=1, limit=(-0.1,0.09)),   # -0.5 ~ 2 까지가 현장과 가장 비슷함  -- RandomBrightnessContrast
        RandomBrightness(p=1, limit=(-0.2,0.1)),
        #RandomGamma(p=1, gamma_limit=(80,200)),
        ], p=0.6),
            
        OneOf([
            #Rotate(limit=30, p=0.3),
            #RandomRotate90(p=0.3),
            HorizontalFlip(p=1),
            VerticalFlip(p=1)
        ], p=0.2),
    
        MotionBlur(p=0.1),   # 움직일때 흔들리는 것 같은 이미지
        #ShiftScaleRotate(shift_limit=0.001, scale_limit=0.1, rotate_limit=30, p=0.3, border_mode=1),
        Resize(224,224, p=1),
        ],
        p=1)

TOTAL_IMG_COUNT =4500

for label in tqdm(label_list):
    #print(label)
    counts = len(img_df[img_df['label'] == f'{label}'])

    while True:
        if counts < TOTAL_IMG_COUNT:
            img_path = img_df[img_df['label'] == f'{label}'].sample(n=1)['image_path'].iloc[0]
            img = cv2.imread(img_path)
            img = cv2.resize(img,(224,224))
            img = cv2.cvtColor(img, cv2.cv2.COLOR_BGR2RGB)
            img = transforms(image=img)['image']
            img = cv2.cvtColor(img, cv2.cv2.COLOR_RGB2BGR)
            
            cv2.imwrite(os.path.join(img_dir,label,f'07_aug_{counts + 1}.jpg'), img)
            counts += 1
            #print(counts)
            #print(os.path.join(img_dir,label,f'aug_{counts + 1}.jpg'),' done!!')
            #print('----------------------------------------------------------------')
        else:
            break

"""
label_cnt = []
for label in label_list:
    label_cnt.append([label, len(glob(os.path.join(img_dir,label,'*')))])

final_list = pd.DataFrame(label_cnt, columns=['label', 'counts'])
print(final_list)
"""
