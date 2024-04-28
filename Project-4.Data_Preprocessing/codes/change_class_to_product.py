import xml.etree.ElementTree as ET
import os

root_path = "annotations"

xml_list = sorted(os.listdir(root_path))

for xml_file in xml_list:
    xml_path = os.path.join(root_path,xml_file)
    # parse xml file
    tree = ET.parse(xml_path)
    # get root node
    root = tree.getroot()
    for i in root.iter('name'):
        i.text = 'product'
    tree.write(xml_path)
