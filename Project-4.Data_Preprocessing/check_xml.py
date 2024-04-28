import xml.etree.ElementTree as ET
import os

root_path = "/home/sudip/Desktop/label_program/600_sudip_complete"

xml_list = sorted(os.listdir(root_path))

for xml_file in xml_list:
    xml_path = os.path.join(root_path,xml_file)
    # parse xml file
    tree = ET.parse(xml_path)
    # get root node
    root = tree.getroot()
    # get object tag
    for object in root.iter("object"):
        # find value of name
        name = object.findtext("name")
	if not name in ("product"):
        #if not name in ("Person", "FullBasket", "EmptyBasket"):
            print(name, xml_file)
print("done.")
