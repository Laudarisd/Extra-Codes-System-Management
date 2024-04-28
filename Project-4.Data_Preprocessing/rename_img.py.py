import os
path = './images'

"""
save_path = "./rename_img"

if not os.path.exists(save_path):
    os.mkdir(save_path)

"""    
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.png'])))