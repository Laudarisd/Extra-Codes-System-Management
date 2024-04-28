import xml.etree.ElementTree as ET
import os

root_path = "./labels"

xml_list = sorted(os.listdir(root_path))

for xml_file in xml_list:
    xml_path = os.path.join(root_path,xml_file)
    # parse xml file
    tree = ET.parse(xml_path)
    # get root node
    root = tree.getroot()
    for elem in root.getiterator():
        elem.text = elem.text.replace('no_yes', 'yes')
        """
        elem.text = elem.text.replace('crosswalk', 'yes')        
        elem.text = elem.text.replace('height', 'yes')
        elem.text = elem.text.replace('left_turn', 'yes')
        elem.text = elem.text.replace('no_left', 'yes')
        elem.text = elem.text.replace('no_parking', 'yes')
        elem.text = elem.text.replace('no_right', 'yes')
        elem.text = elem.text.replace('right_turn', 'yes')
        elem.text = elem.text.replace('uturn', 'yes')
        elem.text = elem.text.replace('stop', 'yes')
        elem.text = elem.text.replace('speed_limit', 'yes')
        elem.text = elem.text.replace('yield', 'yes')
        elem.text = elem.text.replace('straight_notallowed', 'yes')
        elem.text = elem.text.replace('parking', 'yes')
        elem.text = elem.text.replace('no_uturn', 'yes')
        elem.text = elem.text.replace('no_bike', 'yes')
        elem.text = elem.text.replace('straight_allowed', 'yes')
        elem.text = elem.text.replace('slow', 'yes')
        elem.text = elem.text.replace('danger', 'yes')
        """
    tree.write(xml_path)
    print("done : " + xml_path)
   
