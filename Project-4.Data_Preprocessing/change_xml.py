import xml.etree.ElementTree as ET
import os

root_path = "labels"

xml_list = sorted(os.listdir(root_path))

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
