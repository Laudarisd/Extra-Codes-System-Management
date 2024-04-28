from xml.dom import minidom
import xml.etree.ElementTree as ET
from collections import namedtuple
import xml.etree.cElementTree as etree
import numpy as np
import cv2


xmlDoc1 = open('00005.xml', 'r')
xmlDocData1 = xmlDoc1.read()
xmlDocTree1 = etree.XML(xmlDocData1)

bndbox_list1 = []
for bndbox in xmlDocTree1.iter('bndbox'): 
    #for elem in list('bndbox'):
        xmin = bndbox[0].text
        ymin = bndbox[1].text
        xmax = bndbox[2].text
        ymax = bndbox[3].text
        bndbox_list1.append([xmin,ymin,xmax,ymax])
print(bndbox_list1)

boxA = bndbox_list1


xmlDoc2 = open('00006.xml', 'r')
xmlDocData2 = xmlDoc2.read()
xmlDocTree2 = etree.XML(xmlDocData2)

bndbox_list2 = []
for bndbox in xmlDocTree2.iter('bndbox'):
    #for elem in list('bndbox'):
        xmin = bndbox[0].text
        ymin = bndbox[1].text
        xmax = bndbox[2].text
        ymax = bndbox[3].text
        bndbox_list2.append([xmin,ymin,xmax,ymax])
print(bndbox_list2)
        
boxB = bndbox_list2

def bb_intersection_over_union(boxA, boxB):
    xA = int(max(boxA[0][2],boxB[0][2]))
    yA = int(max(boxA[0][3],boxB[0][3]))
    xB = int(min(boxA[0][0],boxB[0][0]))
    yB = int(min(boxA[0][1],boxB[0][1]))
    
    interArea = (max(abs(xB - xA),0)) * (max(abs(yB - yA ),0))
    #interArea = (max(0, xB - xA + 1) * (max(0, yB - yA + 1))
    #if interArea == 0:
      #  return 0
    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = abs(((int(boxA[0][0])) - int(boxA[0][2])) * ((int(boxA[0][1]) - int(boxA[0][3]))))
    boxBArea = abs(((int(boxB[0][0])) - int(boxB[0][2])) * ((int(boxB[0][1]) - int(boxB[0][3]))))
                    
    #boxAArea = ((int(boxA[0][0]) - int(boxA[0][2])) +1) * ((int(boxA[0][1]) - int(boxA[0][3])+1))
    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)

    # return the intersection over union value
    return iou, interArea, boxBArea, boxAArea
    
    
    
    

