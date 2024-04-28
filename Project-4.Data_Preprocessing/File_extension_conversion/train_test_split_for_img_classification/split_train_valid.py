# Import modules
import os
import random
import shutil
#from shutil import movefile

# Set up empty folder structure if not exists
if not os.path.exists('data'):
    os.makedirs('data')
else:
    if not os.path.exists('data/train'):
        os.makedirs('data/train')
    if not os.path.exists('data/validation'):
        os.makedirs('data/validation')
        
# Get the subdirectories in the main image folder
img_source_dir = './images'
subdirs = [subdir for subdir in os.listdir(img_source_dir) if os.path.isdir(os.path.join(img_source_dir, subdir))]

train_size = 0.90  # Define the percentage of images in the training folder


for subdir in subdirs:
    subdir_fullpath = os.path.join(img_source_dir, subdir)
    train_subdir = os.path.join('data/train', subdir)
    validation_subdir = os.path.join('data/validation', subdir)
    
    # Create subdirectories in train and validation folders
    if not os.path.exists(train_subdir):
        os.makedirs(train_subdir)
        
    if not os.path.exists(validation_subdir):
        os.makedirs(validation_subdir)
        
    train_counter = 0
    validation_counter = 0
    
    # Randomly assign an image to train or validation folder
    for filename in os.listdir(subdir_fullpath):
        if filename.endswith(".jpg") or filename.endswith(".png"): 
            fileparts = filename.split('.')
            
            if random.uniform(0, 1) <= train_size:
                shutil.move(os.path.join(subdir_fullpath, filename), os.path.join(train_subdir, str(train_counter) + '.' + fileparts[1]))
                train_counter += 1
            else:
                shutil.move(os.path.join(subdir_fullpath, filename), os.path.join(validation_subdir, str(validation_counter) + '.' + fileparts[1]))
                validation_counter += 1