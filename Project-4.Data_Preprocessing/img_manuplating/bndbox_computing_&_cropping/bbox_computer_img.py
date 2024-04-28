import random
import math
import cv2 
import numpy as np
import copy
from PIL import Image

#width=1280

#height=720



def get_big_box_position(x0, y0, x1, y1, a): 

    a=a*math.pi/180.0
    
    w=x1-x0

    h=y1-y0

    h0=h*math.cos(a)

    w1=h*math.sin(a)

    w0=w*math.cos(a)

    h1=w*math.sin(a)

    bx0=x0-h0*math.sin(a)

    by0=y0+h0*math.cos(a)

    bx1=x0+h1*math.sin(a)

    by1=y0-h1*math.cos(a)

    bx2=x1+w1*math.cos(a)

    by2=y0+w1*math.sin(a)

    bx3=x0+w0*math.cos(a)

    by3=y1+w0*math.sin(a)

    return [bx0,by0,bx1,by1,bx2,by2,bx3,by3]

def get_random_box():

    w=random.randint(width/8, width/4)

    h=random.randint(height/8, height/4)

    x0=random.randint(0, (width-w))

    y0=random.randint(0, (height-h))

    return [x0,y0,x0,y0+h,x0+w,y0+h,x0+w,y0]

#img = np.zeros((height, width, 3), dtype = "uint8")

#rb=get_random_box()

method = cv2.TM_SQDIFF_NORMED

small_image = cv2.imread('crop.jpg')
large_image = cv2.imread('origin.jpg')

height, width = large_image.shape[:2]

result = cv2.matchTemplate(small_image, large_image, method)

mn,_,mnLoc,_ = cv2.minMaxLoc(result)
xmin,ymin = mnLoc
h,w = small_image.shape[:2]
xmax = xmin+w
ymax = ymin+h 

rb = [xmin, ymin, xmin, ymax, xmax, ymax, xmax, ymin]
sb=np.array([[[rb[0],rb[1]],[rb[2],rb[3]],[rb[4],rb[5]],[rb[6],rb[7]]]], np.int32)
num_image=0
for i in range(3000000):
    angle=random.random()*90.0
    #angle=random.randint(0,90)
    bbp=get_big_box_position(rb[0], rb[1], rb[4], rb[5], angle)
    bb=np.array([[[bbp[0],bbp[1]],[bbp[2],bbp[3]],[bbp[4],bbp[5]],[bbp[6],bbp[7]]]], np.int32)

    horizon = np.array([bb[0][0][0], bb[0][1][0], bb[0][2][0], bb[0][3][0]])
    vertical = np.array([bb[0][0][1], bb[0][1][1], bb[0][2][1], bb[0][3][1]])

    if min(horizon) >= 0 and max(horizon) <= width and min(vertical) >= 0 and max(vertical) <= height:


        pts = np.array([bb[0][0], bb[0][1], bb[0][2], bb[0][3]])
        rect = cv2.boundingRect(pts)
        x,y,w,h = rect
        croped = large_image[y:y+h, x:x+w].copy()
        pts = pts - pts.min(axis=0)
        mask = np.zeros(croped.shape[:2], np.uint8)
        cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

        dst = cv2.bitwise_and(croped, croped, mask=mask)
        
        pil_img = Image.fromarray(dst)
        
        re_angle = random.choice([0, 90, 180, 270])
        rerot_img = pil_img.rotate(angle+re_angle, expand=True)

        
        rerot_img = np.array(rerot_img)
        color_pixel = np.argwhere(np.all(rerot_img != [0,0,0], axis=-1))
        x0, y0 = color_pixel.min(axis=0)
        x1, y1 = color_pixel.max(axis=0) + 1        

        cropped = rerot_img[x0+10:x1-10, y0+10:y1-10]

        cv2.imwrite('./%05d.jpg' % num_image, cropped)
        print 'save', './%05d.jpg' % num_image
        num_image=num_image+1
        if num_image>=300:
            break
        #cv2.imshow('Shapes', img_mod)

        #cv2.waitKey(0)


        #cv2.destroyAllWindows()
