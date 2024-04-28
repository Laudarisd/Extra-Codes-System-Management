import glob
import shutil
import os

root_dir = './labels'
move_to = './xmls'


for files in glob.glob(os.path.join(root_dir, "*.xml")):
    #shutil.copy(files, move_dir) # to copy
    shutil.move(files, move_to)
    
onlyfiles = next(os.walk(move_to))[2] #dir is your directory path as string
numbers_files = len(onlyfiles)

print("Tatal number of files:", numbers_files)

