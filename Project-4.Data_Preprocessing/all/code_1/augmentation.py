#use: make aug folder with 2 subfolders named images and xmls.
# edit images path: line 134 
# edit anotations files path: 137 
# edit line 158 : range(5)--- how many images do you need from each image? 

import os
import numpy as np
import cv2
import glob
import xml.etree.ElementTree as ET
from xml.dom import minidom

from albumentations import(
    BboxParams,
    HorizontalFlip,
    VerticalFlip,
    Resize,
    CenterCrop,
    RandomCrop,
    Crop,
    Compose,
    RandomContrast,
    RandomBrightness,
    IAASharpen,
    MotionBlur,
    OneOf)

BOX_COLOR = (255, 0, 0)
TEXT_COLOR = (255, 255, 255)

def read_image(img_path):
    image = cv2.imread(img_path)

    return image

def modify_coordinate(output_path, augmented, xml, idx):
    filename = xml.split('/')[-1]

    tree = ET.parse(xml)
    root = tree.getroot()
    obj_xml = root.findall('object')
    
    bbox_mod = augmented['bboxes']
    # print(bbox_mod)

    for obj in obj_xml:
        bbox_original = obj.find('bndbox')
        bbox_original.find('xmin').text = str(int(bbox_mod[0][0]))
        bbox_original.find('ymin').text = str(int(bbox_mod[0][1]))
        bbox_original.find('xmax').text = str(int(bbox_mod[0][2]))
        bbox_original.find('ymax').text = str(int(bbox_mod[0][3]))

        del bbox_mod[0]

    tree.write(output_path + '/xmls/' + str(idx) + '_' + filename)

def get_boxes(label_path):
    tree = ET.parse(label_path)
    root = tree.getroot()
    obj_xml = root.findall('object')
    
    if obj_xml[0].find('bndbox') != None:

        result = []
        name_list = []
        idx = 0
        category_id = []

        for obj in obj_xml:
            bbox_original = obj.find('bndbox')
            names = obj.find('name')
        
            xmin = int(float(bbox_original.find('xmin').text))
            ymin = int(float(bbox_original.find('ymin').text))
            xmax = int(float(bbox_original.find('xmax').text))
            ymax = int(float(bbox_original.find('ymax').text))

            result.append([xmin, ymin, xmax, ymax])
            name_list.append(names.text)
            category_id.append(idx)
            idx+=1

            # print(result)
            # print(name_list)
            # print(category_id)
        
        return result, name_list, category_id





# def get_boxes(label_path):
#     # print(label_path)
#     xml_path = os.path.join(label_path)

#     root_1 = minidom.parse(xml_path)  # xml.dom.minidom.parse(xml_path)
#     bnd_1 = root_1.getElementsByTagName('bndbox')
#     names = root_1.getElementsByTagName('name')
    
#     result = []
#     name_list = []
#     category_id = []

#     """
#     for i in range(len(bnd_1)):
#         xmin = int(bnd_1[i].childNodes[0].childNodes[0].nodeValue)
#         ymin = int(bnd_1[i].childNodes[1].childNodes[0].nodeValue)
#         xmax = int(bnd_1[i].childNodes[2].childNodes[0].nodeValue)
#         ymax = int(bnd_1[i].childNodes[3].childNodes[0].nodeValue)
#    """
    
#     for i in range(len(bnd_1)):
#         xmin = int(bnd_1[i].childNodes[1].childNodes[0].nodeValue)
#         ymin = int(bnd_1[i].childNodes[3].childNodes[0].nodeValue)
#         xmax = int(bnd_1[i].childNodes[5].childNodes[0].nodeValue)
#         ymax = int(bnd_1[i].childNodes[7].childNodes[0].nodeValue)



#         result.append((xmin,ymin,xmax,ymax))

#         name_list.append(names[i].childNodes[0].nodeValue)

#         category_id.append(i)
    
#     # print(result)
#     return result, name_list, category_id


def visualize_bbox(img, bbox, class_id, class_idx_to_name, color=BOX_COLOR, thickness=2):
    x_min, y_min, x_max, y_max = map(lambda v: int(v), bbox)
    # x_min, x_max, y_min, y_max = int(x_min), int(x_min + w), int(y_min), int(y_min + h)
    cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color=color, thickness=thickness)
    class_name = class_idx_to_name[class_id]
    ((text_width, text_height), _) = cv2.getTextSize(class_name, cv2.FONT_HERSHEY_SIMPLEX, 0.35, 1)    
    cv2.rectangle(img, (x_min, y_min - int(1.3 * text_height)), (x_min + text_width, y_min), BOX_COLOR, -1)
    cv2.putText(img, class_name, (x_min, y_min - int(0.3 * text_height)), cv2.FONT_HERSHEY_SIMPLEX, 0.35,TEXT_COLOR, lineType=cv2.LINE_AA)
    return img


def visualize(annotations, category_id_to_name):
    img = annotations['image'].copy()
    for idx, bbox in enumerate(annotations['bboxes']):
        img = visualize_bbox(img, bbox, annotations['category_id'][idx], category_id_to_name)

    resized = cv2.resize(img, (1920, 1080))
    # cv2.imshow('test', resized)
    # cv2.waitKey(0)


def get_aug(min_area=0., min_visibility=0.):
    return Compose(
        OneOf([
        RandomContrast(p=0.0, limit=(-0.5,1)),   # -0.5 ~ 2 -- RandomBrightnessContrast
        RandomBrightness(p=0.05, limit=(-0.2,0.1)),
        HorizontalFlip(p=0.0),
        ], p=0.5),

        bbox_params=BboxParams(format='pascal_voc', min_area=min_area, 
                               min_visibility=min_visibility, label_fields=['category_id'])
                               
    )


def make_categori_id(str_label):
    idx = 0
    result = []
    category_id_to_name = {}

    for label in str_label:
        category_id_to_name.update({int(idx):str(label)})
        idx += 1

    # print(category_id_to_name)
    return category_id_to_name


if __name__ == "__main__":
    image_set_path = './images/*'
    image_list = sorted(glob.glob(image_set_path))

    xml_set_path = './labels/*'
    xml_list = sorted(glob.glob(xml_set_path))

    output_path = './aug/'

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    
    #os.mkdir("./aug/images")
    #os.mkdir("./aug/xmls")
    desire_class = ["red_yield","warning_speed_breaker","warning_left_hand_curved","blue_normal_left",
                    "bojo_traffic_caution","red_pause","warning_danger","red_no_pedestrian","red_no_entry",
                    "warning_missing_right_side","blue_circle_uturn","bojo_signal_light","blue_right_handed",
                    "info","blue_other","warning_bicycle","killopost", "blue_normal_straight", "warning_side_intersection",
                    "red_truck_not_allowed", "blue_bicycle_exclusive_road", "warning_slippery_road", "blue_only_bus",
                    "blue_left_handed", "warning_double_curved_left_right","blue_car_exclusive_road", "red_other",
                    "blue_normal_right", "blue_child_protection_zone", "blue_parking", "red_weight_limit"]


    # desire_class1 = ["warning_bicycle","killopost", "blue_normal_straight", "warning_side_intersection", "red_truck_not_allowed",
    #                 "blue_bicycle_exclusive_road", "warning_slippery_road", "blue_only_bus", "blue_left_handed", "warning_double_curved_left_right",
    #                 "blue_car_exclusive_road", "red_other", "blue_normal_right", "blue_child_protection_zone", 
    #                 "blue_parking", "red_weight_limit"]
 


    
    for image, xml in zip(image_list, xml_list):
        #print(image, xml)
        
        image_name = image.split('/')[-1]
        # print(image_name)
        image = read_image(image)
        bbox, str_label, category_id = get_boxes(xml)
        category_id_to_name = make_categori_id(str_label)
        #print(category_id_to_name)

        for key, value in category_id_to_name.items():
            #print(value)
            if value in desire_class:
                print(value)
                annotations = {'image':image, 'bboxes':bbox, 'category_id':category_id}
                visualize(annotations, category_id_to_name)

                aug = get_aug()
                
                for i in range(2):
                    augmented = aug(**annotations)
                    # print(augmented)
                    visualize(augmented, category_id_to_name)
                    # print(output_path + '/' + str(i) + '_' + image_name)
                    cv2.imwrite(output_path + '/images/' + str(i) + '_' + image_name, augmented['image'])
                    modify_coordinate(output_path, augmented, xml, i)
                
                
            
            

