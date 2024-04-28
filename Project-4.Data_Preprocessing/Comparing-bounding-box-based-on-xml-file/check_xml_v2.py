import xml.etree.ElementTree as ET
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

#xml_list = sorted(os.listdir(root_path))
xml_list = glob.glob('./xml/*/*')


def get_root(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root


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
if there are many folders

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

def count_files():
    
    print('2. file counting....')
    
    labels_1 = os.listdir(os.path.join(root_path,xml_dir_list[0]))
    labels_2 = os.listdir(os.path.join(root_path,xml_dir_list[1]))
    
    if labels_1 == labels_2:
            print('The number of files is the same !!')
    else:
        print(' >> The number of files is different. Please check again !! <<')
        
        if len(labels_1) > len(labels_2):
            print('There is no files in label_2 : ', set(labels_1) - set(labels_2))
        else:
            print('There is no files in label_1 : ', set(labels_2) - set(labels_1))
        
        
check_xml()
count_files()
