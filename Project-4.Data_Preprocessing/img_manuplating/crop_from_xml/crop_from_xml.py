from PIL import Image
import ast
import os
import cv2
import os
import glob
import xml.etree.ElementTree as ET

original_file = './images/'
dst = './save/'


def check_folder_exists(path):
        if not os.path.exists(path):
            try:
                os.makedirs(path)
                print ('create ' + path)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise




seed_arr = []
for xml_file in glob.glob('./labels/*.xml'):
    root = ET.parse(xml_file).getroot()
    filename = root.find('filename').text

    for type_tag in root.findall('size'):
        #file_name = type_tag.find('filename').text
        width = type_tag.find('width').text
        height = type_tag.find('height').text

    for type_tag in root.findall('object'):
        class_name = type_tag.find('name').text
        xmin = type_tag.find('bndbox/xmin').text
        ymin = type_tag.find('bndbox/ymin').text
        xmax = type_tag.find('bndbox/xmax').text
        ymax = type_tag.find('bndbox/ymax').text
        all_list = [filename, width,height,class_name,xmin, ymin, xmax,ymax]

        seed_arr.append(all_list)
    
seed_arr.sort()
#print(str(len(seed_arr)))
#print(str(seed_arr))


for index, line in enumerate(seed_arr):
    filename = line[0]
    width = line[1]
    height = line[2]
    class_name = line[3]
    xmin = line[4]
    ymin = line[5]
    xmax = line[6]
    ymax = line[7]
    

#print(len(class_name))
    

    
    load_img_path = os.path.join(original_file, filename)
    #save img path

#save img path----------
    save_class_path = os.path.join(dst, class_name)
    check_folder_exists(save_class_path)
    save_img_path = os.path.join(save_class_path, str(index)+'_'+filename)
    
    img = Image.open(load_img_path)
    crop_img = img.crop((int(xmin) ,int(ymin) ,int(xmax) ,int(ymax)))
    newsize = (224, 224) 
    im1 = crop_img.resize(newsize) 
    im1.save(save_img_path, 'JPEG')
    print('save ' + save_img_path)



