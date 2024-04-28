#-*- coding: utf-8 -*-

import pandas as pd
import cv2
import numpy as np
import imutils
from datetime import datetime
import time
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

#####################################################################################
#LABELS = ['galbae_can','coca_can','sprite_can']

RESIZE = 224
BRIGHTNESS = 30
CAMERA_NUM = -1
#####################################################################################



def Rotate(src, degrees) :
    if degrees == 90 :
        dst = cv2.transpose(src)
        dst = cv2.flip(dst, 1)
    elif degrees == 180 :
        dst = cv2.flip(src, 0)
    elif degrees == 270 :
        dst = cv2.transpose(src)
        dst = cv2.flip(dst, 0)
    else :
        dst = null
    return dst

def get_boxes(label_path):
    label_path = label_path
    xml_list = os.listdir(label_path)

    boxes_1 = {}
    cnt = 0
    for xml_file in sorted(xml_list):
        if xml_file =='.DS_Store':
            pass
        else:
                #try:
            xml_path = os.path.join(label_path,xml_file)

            root_1 = minidom.parse(xml_path)
            bnd_1 = root_1.getElementsByTagName('bndbox')

            result = []
            for i in range(len(bnd_1)):
                xmin = int(bnd_1[i].childNodes[1].childNodes[0].nodeValue)
                ymin = int(bnd_1[i].childNodes[3].childNodes[0].nodeValue)
                xmax = int(bnd_1[i].childNodes[5].childNodes[0].nodeValue)
                ymax = int(bnd_1[i].childNodes[7].childNodes[0].nodeValue)
                result.append((xmin,ymin,xmax,ymax))

            boxes_1[str(cnt)] = result
            cnt += 1
    
    return boxes_1


def get_labels(label_path):
    with open('./label.txt', 'r') as file:
        labels = file.readlines()
        labels = list(map(lambda x : x.strip(), labels))

    return labels

def crop_image(image, boxes, save_path, labels, resize=None):
        seed_image = image
        images = list(map(lambda b : image[b[1]+1:b[3]-1, b[0]+2:b[2]-1], boxes))
        images = list(map(lambda i : cv2.resize(i, resize), images))
        #if str(type(resize)) == "<class 'tuple'>":
        #    images = list(map(lambda i : cv2.resize(i, resize), images))
        #num = 0
        
        for img, label in zip(images, labels):
            #num = num + 1
            cv2.imwrite('{}/{}/{}_{}.jpg'.format(save_path,label,today,label), img)
            
        return images

def make_folder(label_dir):
    if not os.path.exists(save_dir +'/' + label_dir):
        os.makedirs(save_dir +'/' + label_dir)

#####################################################################################

#LABELS = get_labels('./label.txt')

# 수동으로 라벨 조절할 때 사용
#LABELS = ['galbae_can','coca_can','sprite_can']
#for label in LABELS:
#    make_folder(label)


#####################################################################################

BOX_NUM = '0'   # 
MODE = 'b'   # b : box 모드

save_dir = './cls_seed_images'
#box = get_boxes('./boxes')['{}'.format(BOX_NUM)]


cap = cv2.VideoCapture(CAMERA_NUM)  
if cap.isOpened() == False:
    print('카메라를 오픈 할 수 없습니다.')

frame_width = int(3840)
frame_height = int(2160)

MJPG_CODEC = 1196444237.0 # MJPG

cv2.namedWindow('Usb Cam', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Usb Cam', frame_width,frame_height)

cap.set(cv2.CAP_PROP_BRIGHTNESS, BRIGHTNESS)
cap.set(cv2.CAP_PROP_FOURCC, MJPG_CODEC)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
cap.set(cv2.CAP_PROP_FOCUS, 50)
#########################################################################################

while True:
    ret, frame = cap.read()

    box = get_boxes('./boxes')['{}'.format(BOX_NUM)]
    LABELS = get_labels('./label.txt')
    #frame = cv2.resize(frame, (frame_width, frame_height))
    #frame = imutils.rotate(frame, 90) 

    if MODE =='b':
        x = 400
        for i, j in zip(box, LABELS):
            cv2.rectangle(frame, (i[0],i[1]), (i[2], i[3]), (0,0,255), 2)
            #cv2.putText(frame, j, (i[0], i[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 4)
            cv2.putText(frame, '{} ||'.format(j), (x, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)
            x = x + 500

        cv2.putText(frame, 'BOX : {}'.format(BOX_NUM), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        

    cv2.imshow('Usb Cam', frame)
    today = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

    ch = cv2.waitKey(1)

    # 종료
    if ch == ord('q'):
	    break

    # 박스 숨기기 / 나타내기
    elif ch == ord('a'):
        if MODE == 'b':
            MODE = 'a'
        else:
            MODE = 'b'


    # box 변경 ( '[' : - 변경,   ']' : + 변경)
    elif ch == ord(']'):
        BOX_NUM = str(int(BOX_NUM) + 1)
    
        if BOX_NUM == str(len(os.listdir('./boxes'))):
            BOX_NUM = '0'

    elif ch == ord('['):
        BOX_NUM = str(int(BOX_NUM) - 1)
    
        if BOX_NUM == '-1':
            BOX_NUM = str(len(os.listdir('./boxes'))-1)


    # 전체 이미지 캡쳐
    elif ch == ord('c'):
	    print('press c')
	    cv2.imwrite('./saved_images/usbcam({}).jpg'.format(today),frame)
	    print('./saved_images/usbcam({}).jpg saved'.format(today))


    # 박스 이미지 캡쳐 및 resize
    elif ch == ord('s'):
        image = frame
        
        for label in LABELS:
            make_folder(label)


        crop_image(image, box, save_dir,  LABELS, (RESIZE,RESIZE))
        print('{} : images cropped'.format(LABELS))
        
        cv2.imwrite('./saved_images/usbcam({}).jpg'.format(today),frame)
	    #print('./saved_images/usbcam({}).jpg saved'.format(today))


    elif ch == ord('0'):
        image = frame
        image = image[box[0][1]+1:box[0][3]-1, box[0][0]+2:box[0][2]-1]
        image = cv2.resize(image, (RESIZE,RESIZE))
        cv2.imwrite('{}/{}/{}_{}.jpg'.format(save_dir + '/',LABELS[0],today,LABELS[0]), image)

    #cv2.imshow('Usb Cam', frame)

    elif ch == ord('f'):
        image_name = './saved_images/box_{}.jpg'.format(today)
        cv2.imwrite(image_name, frame)
        os.system('python3 ./labelimg/labelImg.py {} ./labelimg/data/predefined_classes.txt ./boxes'.format(image_name))
        

cap.release()
cv2.destroyAllWindows()
