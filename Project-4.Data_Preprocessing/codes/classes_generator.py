import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

seed_arr = []

# parse xml information 

for xml_file in glob.glob('./annotations/*.xml'):
    root = ET.parse(xml_file).getroot()
    filename = root.find('filename').text

    #for type_tag in root.findall('size'):
        #file_name = type_tag.find('filename').text
        #width = type_tag.find('width').text
        #height = type_tag.find('height').text

    for type_tag in root.findall('object'):
        class_name = type_tag.find('name').text
        #xmin = type_tag.find('bndbox/xmin').text
        #ymin = type_tag.find('bndbox/ymin').text
        #xmax = type_tag.find('bndbox/xmax').text
        #ymax = type_tag.find('bndbox/ymax').text
        #all_list = [filename, width,height,class_name,xmin, ymin, xmax,ymax]
        all_list = [class_name]
        seed_arr.append(all_list)
        
seed_arr.sort()
# convert sublist to tuple

my_list = set(map(tuple,seed_arr))

# generate csv win information my_list(my_list= classes)
column_name = ['classes']
xml_df = pd.DataFrame(my_list, columns=column_name)
xml_df.to_csv(('class.csv'), index=None)
print('Successfully generated csv file.')
    





