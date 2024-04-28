import glob
import shutil
import os

root_dir = './aug/xmls'
move_to = './xmls'


if not os.path.exists(move_to):
    os.mkdir(move_to)
	


for files in glob.glob(os.path.join(root_dir, "*.xml")):
    #shutil.copy(files, move_dir) # to copy
    shutil.move(files, move_to)
    
onlyfiles = next(os.walk(move_to))[2] #dir is your directory path as string
numbers_files = len(onlyfiles)

print("Tatal number of files:", numbers_files)

