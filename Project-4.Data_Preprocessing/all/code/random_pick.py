import random
import os
import shutil

#Only Images - Random Pick
root_path = '../images'
sub_list = sorted(os.listdir(root_path))


onlyfiles = next(os.walk(root_path))[2] #dir is your directory path as string
total_num = len(onlyfiles)

print("Tatal number of files:", total_num)

cnt = int((total_num * 20)/100)
print(cnt)

root_path = '../images'
sub_list = sorted(os.listdir(root_path))

random_list = random.sample(sub_list, cnt)
random_path = '../val_images'
if not os.path.exists(random_path):
    os.makedirs(random_path)

for i in random_list:
    i_list = str(i).split('.')[0]
    print (i_list)
    image_path = os.path.join(random_path, i)

def random_pick():
    for j in range(0, len(random_list)):
        comb_full_path = os.path.join(root_path, random_list[j])
        move_full_path = os.path.join(random_path, random_list[j])
        shutil.move(comb_full_path, move_full_path)
random_pick()


#Images and xml annotaion files, random pick

"""

import random
import os
import shutil

cnt = 100

root_path = './train_images'
label_path = './train_labels'

img_list = sorted(os.listdir(root_path))
label_list = sorted(os.listdir(label_path))

random_list = random.sample(img_list, cnt)
random_path = './valid_images'

if not os.path.exists(random_path):
    os.makedirs(random_path)
l_random_path = './valid_labels'
if not os.path.exists(l_random_path):
    os.makedirs(l_random_path)
alabel_list = []



for i in random_list:
    i_list = str(i).split('.')[0]
    print (i_list)

    label = i_list+'.xml'
    print (label)
    alabel_list.append(label)
    #second_list = sorted(os.listdir(label))
    #print second_list

    #print os.path.join(random_path, i)

    image_path = os.path.join(random_path, i)
    random_label_path = os.path.join(random_path, label)
    #print random_label_path
    #print image_path
    #print random_label_path

    #shutil.copy(image_path, image_path)

print (alabel_list)

def random_pick():
    for j in range(0, len(random_list)):
        comb_full_path = os.path.join(root_path, random_list[j])
        move_full_path = os.path.join(random_path, random_list[j])

        l_comb_full_path = os.path.join(label_path, alabel_list[j])
        l_move_full_path = os.path.join(l_random_path, alabel_list[j])

        shutil.move(comb_full_path, move_full_path)
        shutil.move(l_comb_full_path, l_move_full_path)

random_pick()

"""
