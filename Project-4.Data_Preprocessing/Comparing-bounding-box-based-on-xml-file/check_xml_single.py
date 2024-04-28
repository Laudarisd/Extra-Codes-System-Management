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
                
check_xml()
change_xml()
