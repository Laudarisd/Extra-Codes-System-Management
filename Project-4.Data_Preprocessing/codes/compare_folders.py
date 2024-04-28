import os

# list img_baverage folder
img = os.listdir('img_bevarage/')
#print(img)

# list labels_baverage folder
xml = os.listdir('labels_baverage/')
#print(xml)

# remove file extension to make same name while comparing

img_name = list(map(lambda x : x.split('.')[0],img))
#print(img_name)
xml_name = list(map(lambda x : x.split('.')[0],xml))
#print(xml_name)

# Since xml_name has more files than img_img. So printing the files which are not in img_name
set(xml_name) - set(img_name)
