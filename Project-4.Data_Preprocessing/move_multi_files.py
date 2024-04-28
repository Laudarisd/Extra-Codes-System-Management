# move/copy multiple files to multiple folders based on extension


import glob
import os
import shutil

# Location with subdirectories
src_dir = glob.glob("./4/*/*")

# Location to move images to
#move_here = "./30_test/images"
move_xmls = "./4/labels"

move_dir = "./4/images"

if not os.path.exists(move_dir):
    os.mkdir(move_dir)

if not os.path.exists(move_xmls):
    os.mkdir(move_xmls)
    
for file in src_dir:
    #print(file)
    if file.endswith(".jpg"):
        shutil.move(file, move_dir)
    elif file.endswith(".png"):
        shutil.move(file, move_dir)
    else:
        shutil.move(file, move_xmls)
        
        
        
 """
 # move and rename if the files are same
 
 import glob
import os
import shutil

# Location with subdirectories
my_path = "./21/labels"

# Location to move images to
move_here = "./21/images"

if not os.path.exists(move_here):
    os.mkdir(move_here)

# Get List of all images
files = glob.glob(my_path + '/**/*.jpg', recursive=True)

# For each image
for file in files:
    # Get File name and extension
    filename = os.path.basename(file)
    filename=filename[:-4].replace(".", "-") + ".jpg"
    #print(filename)
    # Copy the file with os.rename
    if not os.path.exists(os.path.join(move_here, filename)):
        os.rename(file, os.path.join(move_here, filename))
    #print(filename)
    
    
    """
 
 
