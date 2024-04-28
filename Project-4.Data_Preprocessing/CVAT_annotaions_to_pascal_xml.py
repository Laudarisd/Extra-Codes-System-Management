# This code converts CVAT xml to pascal xml
# This code extract only one class from xml
# To extract all class add classes in the below where it is commented .check "elif" section



import pandas
import numpy
import os
# from tqdm import tqdm_notebook

from xml.etree.ElementTree import parse, Element, SubElement, ElementTree
import xml.etree.ElementTree as ET


#save_root1 = "./traffic_light"
save_root2 = "./2/xmls"


#if not os.path.exists(save_root1):
#    os.mkdir(save_root1)

if not os.path.exists(save_root2):
    os.mkdir(save_root2)


def indent(elem, level=0): #자료 출처 https://goo.gl/J8VoDK
    i = "\n" + level*"    "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "    "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

            
def write_xml(folder, filename, width, height, bbox_list):
    root = Element('annotation')
    SubElement(root, 'folder').text = folder
    SubElement(root, 'filename').text = filename
    SubElement(root, 'path').text = './images' +  filename
    source = SubElement(root, 'source')
    SubElement(source, 'database').text = 'Unknown'

    size = SubElement(root, 'size')
    SubElement(size, 'width').text = str(width)
    SubElement(size, 'height').text = str(height)
    SubElement(size, 'depth').text = '3'

    SubElement(root, 'segmented').text = '0'

    for i in bbox_list:
        obj = SubElement(root, 'object')
        SubElement(obj, 'name').text = i[0]
        SubElement(obj, 'pose').text = 'Unspecified'
        SubElement(obj, 'truncated').text = '0'
        SubElement(obj, 'difficult').text = '0'

        bbox = SubElement(obj, 'bndbox')
        SubElement(bbox, 'xmin').text = str(i[1])
        SubElement(bbox, 'ymin').text = str(i[2])
        SubElement(bbox, 'xmax').text = str(i[3])
        SubElement(bbox, 'ymax').text = str(i[4])

    indent(root)
    tree = ElementTree(root)
    tree.write('./'+folder + '/' + filename.split('.')[0] +'.xml')
    
file_nm = glob.glob('./2/labels/*.xml')
#print(file_nm)   

for root_nm in file_nm:  # file_nm is xml_file_list
    before_xml = ET.parse(root_nm)
    root = before_xml.getroot()
    for child in root:
        if child.tag == 'image':
            file_nm = child.attrib['name']
            width = child.attrib['width']
            height = child.attrib['height']
            sign = 0
            #light = 0
            bbox_list = []
            for i in child:
                image_box = []
                if (i.attrib['label'] == 'traffic_sign'): #add traffic_sign in xml
                    sign += 1
                    image_box.append(i.attrib['label'])
                    image_box.append(i.attrib['xtl'])
                    image_box.append(i.attrib['ytl'])
                    image_box.append(i.attrib['xbr'])
                    image_box.append(i.attrib['ybr'])

                    bbox_list.append(image_box)
                # elif (i.attrib['label'] == 'traffic_light') : #add another class in annotation file
                    #light += 1
                    #image_box.append(i.attrib['label'])
                    #image_box.append(i.attrib['xtl'])
                    #image_box.append(i.attrib['ytl'])
                    #image_box.append(i.attrib['xbr'])
                    #image_box.append(i.attrib['ybr'])
                    #bbox_list.append(image_box)
            if sign > 0:
                write_xml(save_root2, file_nm, width, height, bbox_list)
            #if light > 0:
                #write_xml('./traffic_light', file_nm, width, height, bbox_list)
