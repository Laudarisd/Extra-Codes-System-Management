"""
Check: 
Classes check
xml file name check
classes count (pair)
bounding box comapre
label name, wrong label(pair)
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
import glob

root_path = "xml"
label_path = './data'
xml_dir_list = os.listdir(root_path)


f = open(label_path + '/predefined_classes.txt', 'r')
labels = f.readlines()
f.close()

label_list = []
for label in labels:
    label = str(label.replace('\n',''))
    label_list.append(label)

labels_1 = os.listdir(os.path.join(root_path,xml_dir_list[0]))
labels_2 = os.listdir(os.path.join(root_path,xml_dir_list[1]))

#xml_list = sorted(os.listdir(root_path))
xml_list = glob.glob('./xml/*/*')



def get_root(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root


# box_a, box_b intersection

def inter_area_compare(box_a, box_b):
    list_x = [box_a[0],box_a[2],box_b[0],box_b[2]]
    list_y = [box_a[1],box_a[3],box_b[1],box_b[3]]
    list_x.sort()
    list_y.sort()

    list_x = list_x[1:3]
    list_y = list_y[1:3]

    inter_box = [list_x[0],list_y[0],list_x[1],list_y[1]]

    inter_area = (inter_box[2] - inter_box[0]) * (inter_box[3] - inter_box[1])
    boxA_area = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    boxB_area = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])

    iou = inter_area / float(boxA_area + boxB_area - inter_area)
    
    return iou

def check_xml():
    print("1.fault label name checking...")
    for xml_file in xml_list:
        #xml_path = os.path.join(root_path,xml_file)
        # parse xml file
        tree = ET.parse(xml_file)
        # get root node
        root = tree.getroot()
        # get object tag
        for object in root.iter("object"):
            # find value of name
            name = object.findtext("name")
            if not name in label_list:
                print(name, xml_file)
    print("done !!")
    print('-------------------------------------------------------------------')
    
def change_xml():
    for xml_file in xml_list:
        xml_path = os.path.join(root_path,xml_file)
        # parse xml file
        tree = ET.parse(xml_path)
        # get root node
        root = tree.getroot()
        for elem in root.getiterator():
            elem.text = elem.text.replace('person', 'Person')
            elem.text = elem.text.replace('fullbasket', 'FullBasket')
            elem.text = elem.text.replace('emptybasket', 'EmptyBasket')
        tree.write(xml_path)
        print("done : " + xml_path)
        
''' 
if many folders are there

def count_files():
    print('2. file counting....')
    file_cnt = []
    for i in xml_dir_list:
        file_dir = os.path.join(root_path,i)
        files = os.listdir(file_dir)
        file_cnt.append(len(files))
        print(file_dir,' : ', len(files))

    if len(set(file_cnt)) == 1:
        print('2. The number of files is the same !!')
    else:
        print('2. The number of files is different. Please check again !!')
'''        
# label1 , label2 files check 
# 라벨1, 라벨2 파일 개수 확인 (파일 개수 다를 시, 확인해야 하는 파일명 출력) - couple
def count_files():
    
    print('2. file counting....')
#    labels_1 = os.listdir(os.path.join(root_path,xml_dir_list[0]))
#    labels_2 = os.listdir(os.path.join(root_path,xml_dir_list[1]))
    
    if labels_1 == labels_2:
            print('The number of label files is the same !!')
    else:
        print(' >> The number of label files is different. Please check again !! <<')
        
        if len(labels_1) > len(labels_2):
            print('There is no files in label_2 : ', set(labels_1) - set(labels_2))
        else:
            print('There is no files in label_1 : ', set(labels_2) - set(labels_1))

    
    print('-------------------------------------------------------------------')

# each object compare   
# object 개수 비교
def compare_object_count():

    print('3. object counting....')

    if len(labels_1) > len(labels_2):
        files_list = os.listdir(os.path.join(root_path,xml_dir_list[1]))
    else:
        files_list = os.listdir(os.path.join(root_path,xml_dir_list[0]))

    for file in files_list:
        compare_labels_1 = os.path.join(root_path,xml_dir_list[0],file)
        root_1 = get_root(compare_labels_1)
        obj_cnt_1 = len(root_1.findall('object'))


        compare_labels_2 = os.path.join(root_path,xml_dir_list[1],file)
        root_2 = get_root(compare_labels_2)
        obj_cnt_2 = len(root_2.findall('object'))

        if obj_cnt_1 == obj_cnt_2:
          #  print('The number of label and image files is the same !!')
            pass
        else:
            print('Objects are different!! - {}'.format(file))

    print("done !!")
    print('-------------------------------------------------------------------')

# bnd box compare    
# bnd box intersection 비교

def compare_bndbox_iou():

    print('4.compare bndbox iou....')
    print(' ')

    if len(labels_1) > len(labels_2):
        files_list = os.listdir(os.path.join(root_path,xml_dir_list[1]))
    else:
        files_list = os.listdir(os.path.join(root_path,xml_dir_list[0]))

    for file in files_list:

        compare_labels_1 = os.path.join(root_path,xml_dir_list[0],file)
        compare_labels_2 = os.path.join(root_path,xml_dir_list[1],file)

        root_1 = minidom.parse(compare_labels_1)
        bnd_1 = root_1.getElementsByTagName('bndbox')


        root_2 = minidom.parse(compare_labels_2)
        bnd_2 = root_2.getElementsByTagName('bndbox')

        ###########################################################

        result_a = {}
        result_b = {}
        for i in range(len(bnd_1)):
            xmin_a = int(bnd_1[i].childNodes[1].childNodes[0].nodeValue)
            ymin_a = int(bnd_1[i].childNodes[3].childNodes[0].nodeValue)
            xmax_a = int(bnd_1[i].childNodes[5].childNodes[0].nodeValue)
            ymax_a = int(bnd_1[i].childNodes[7].childNodes[0].nodeValue)

            xmean_a = (xmin_a + xmax_a)/2
            ymean_a = (ymin_a + ymax_a)/2

            result_a[i] = [(xmean_a,ymean_a), xmin_a, ymin_a, xmax_a, ymax_a]

            xmin_b = int(bnd_2[i].childNodes[1].childNodes[0].nodeValue)
            ymin_b = int(bnd_2[i].childNodes[3].childNodes[0].nodeValue)
            xmax_b = int(bnd_2[i].childNodes[5].childNodes[0].nodeValue)
            ymax_b = int(bnd_2[i].childNodes[7].childNodes[0].nodeValue)

            xmean_b = (xmin_b + xmax_b)/2
            ymean_b = (ymin_b + ymax_b)/2
            result_b[i] = [(xmean_b,ymean_b), xmin_b, ymin_b, xmax_b, ymax_b]

        ##############################################################

        for i in range(len(result_a)):
            # a[i] compare
            diff_x = []
            diff_y = []
            for j in range(len(result_b)):
                #print('a: ', result_a[i][0][0], result_a[i][0][1])
                #print('b: ', result_b[j][0][0], result_b[j][0][1])
                diff_x.append(abs(result_a[i][0][0] - result_b[j][0][0]))
                diff_y.append(abs(result_a[i][0][1] - result_b[j][0][1]))

            if min(diff_x) <= min(diff_y):
                idx = diff_x.index(min(diff_x))
            else:
                idx = diff_y.index(min(diff_y))
            #print(diff_x)
            #print(diff_y)
            #print(i, idx)

            if idx != i:
                result_b[i], result_b[idx] = result_b[idx], result_b[i]
        
        for i in range(len(result_a)):
            box_a = result_a[i][1:]
            box_b = result_b[i][1:]
            iou = inter_area_compare(box_a, box_b)
            
            if iou <= 0.80:
                print('File name : ',file)
                print('box_a, box_b', box_a, box_b)
                print('inter_section : ', iou)

                print('*' * 50)
        
        
    print("done !!")
    print('-------------------------------------------------------------------')

#compare_bndbox_iou()
check_xml()
count_files()
compare_object_count()
compare_bndbox_iou()
