# import libraries
from xml.dom import minidom
import xml.etree.ElementTree as ET
from collections import namedtuple
import numpy as np
import cv2

# import xml file 1, list out xmin, ymin....from xml file. We just list out the information of one bounding box1

import xml.etree.cElementTree as etree
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

import xml.etree.cElementTree as etree
xmlDoc2 = open('00006.xml', 'r')
xmlDocData2 = xmlDoc2.read()
xmlDocTree2 = etree.XML(xmlDocData2)


# import xml file 2, list out xmin, ymin....from xml file. We just list out the information of one bounding box2
# boxes should belong to same object. 

bndbox_list2 = []
for bndbox in xmlDocTree2.iter('bndbox'):
    #for elem in list('bndbox'):
        xmin = bndbox[0].text
        ymin = bndbox[1].text
        xmax = bndbox[2].text
        ymax = bndbox[3].text
        bndbox_list2.append([xmin,ymin,xmax,ymax])
print(bndbox_list2)

# assigning list as boxA and boxB to use easily.

boxA = bndbox_list1
boxB = bndbox_list2

# pulout coordinates ax xA, XB....., change them to int.

def bb_intersection_over_union(boxA, boxB):
    xA = int(max(boxA[0][2],boxB[0][2]))
    yA = int(max(boxA[0][3],boxB[0][3]))
    xB = int(min(boxA[0][0],boxB[0][0]))
    yB = int(min(boxA[0][1],boxB[0][1]))
    # find the area of intersection of two boxes and multiply them.
    interArea = (max(abs(xB - xA),0)) * (max(abs(yB - yA ),0))
    #interArea = (max(0, xB - xA + 1) * (max(0, yB - yA + 1))
    #if interArea == 0:
      #  return 0
    # compute the area of both boxes and take abs.
    boxAArea = abs(((int(boxA[0][0])) - int(boxA[0][2])) * ((int(boxA[0][1]) - int(boxA[0][3]))))
    boxBArea = abs(((int(boxB[0][0])) - int(boxB[0][2])) * ((int(boxB[0][1]) - int(boxB[0][3]))))
                    
    # to calculate the accuracy of bounding box, use the following formula. 
    iou = interArea / float(boxAArea + boxBArea - interArea)

    # return the intersection over union value
    return iou, interArea, boxBArea, boxAArea


print(bb_intersection_over_union(boxA , boxB))

#In my case, I got the following results. 00005.xml and 00006.xml file have same values. If it is 1 then boxes are same.
"""
iou = 1
interArea = 248460
boxAArea = 248460
boxBArea = 248460
"""








        
