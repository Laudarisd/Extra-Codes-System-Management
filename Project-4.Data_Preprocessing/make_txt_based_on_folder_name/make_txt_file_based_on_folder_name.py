# make txt file base on subdirectories name...


import os

class_path = './datasets/train'

CLASS_NAMES = sorted(os.listdir(class_path))
#print(CLASS_NAMES)
#print(len(CLASS_NAMES))

with open('./labels.txt', 'w') as df:
    for n in CLASS_NAMES:
        df.write(n + '\n')


#print(i, file=open('./labels.txt','w'))
