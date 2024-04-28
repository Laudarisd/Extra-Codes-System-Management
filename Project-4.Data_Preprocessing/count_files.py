import os

onlyfiles = next(os.walk("./labels/"))[2] #dir is your directory path as string
numbers_files = len(onlyfiles)

print("Tatal number of files:", numbers_files)

"""
#To count typrs of files + all sub folders

import os

list = os.listdir("./") # dir is your directory path
number_files = len(list)
print ("Number of files(types) + folder:", number_files)

"""
