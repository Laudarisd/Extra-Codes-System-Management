import os
from PIL import Image


root = './etc/'


folder_list = os.listdir(root)

#print(folder_list)
for files in folder_list:
    subfolder_path = os.path.join(root, files)
    img_list = os.listdir(subfolder_path)
    #print(img_list)
    for img in img_list:
        img_path = os.path.join(subfolder_path, img)
        image = Image.open(img_path)
        name, ext = os.path.splitext(img)
        img_resize = image.resize((224, 224))
        img_resize.save(img_path, 'JPEG', quality=100)
        print("Resize process is completed.")
