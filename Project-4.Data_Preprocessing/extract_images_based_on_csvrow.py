# import libraries
import os
import shutil
# this script copies images from a folder ./21/images
# copying crieteria is based on csv column (type_id = row[3]).
# it copies the file which are only mentioned in csv column (type_id = row[3])
# if file doesn't exist , it passes


import csv


# csv path
csv_path = os.path.join('./21', 'labels.csv')

# file root
root_path = os.path.join('./21/images')
#root_path = glob.glob("./images/*/*")
# define the saving path after copying files by making new folder 
save_path = os.path.join('./21')

if not os.path.exists(save_path):
    os.mkdir(save_path)
#os.makedirs(save_path)

df = open(csv_path, 'r')
read = csv.reader(df, delimiter= ',')

flag = 0
for i, row in enumerate(read):
    try:
        if flag == 0:
            flag += 1
            pass
        else:
            type_id = row[3]
            dst = os.path.join(save_path, type_id)
            img = os.path.join(root_path, row[0])
            #print(img)
            if not os.path.exists(dst):
                os.makedirs(dst)
        shutil.copy(os.path.join(root_path, row[0]), dst)
    except:
        pass          
