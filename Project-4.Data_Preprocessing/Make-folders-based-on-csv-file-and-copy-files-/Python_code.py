# import libraries
import os
import shutil
import csv


# csv path
csv_path = os.path.join('./', 'image.csv')

# file root
root_path = os.path.join('./image')

# define the saving path after copying files by making new folder 
save_path = os.path.join('./move')
os.makedirs(save_path)

df = open(csv_path, 'r')
read = csv.reader(df, delimiter= ',')

flag = 0
for i, row in enumerate(read):
    if flag == 0:
        flag += 1
        pass
    else:
        type_id = row[2]
        dst = os.path.join(save_path, type_id)
        if not os.path.exists(dst):
            os.makedirs(dst)
        shutil.copy(os.path.join(root_path, row[0]), dst)   
        
        
"""
This code will 'copy' all the png images which are in image folder to 'move' folder. 
there ar 4 name sin csv file in second column. png will be copied to each name folders.
"""
