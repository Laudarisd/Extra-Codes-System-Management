import shutil
import os
import glob
dst = "./"
"""
try:
    os.makedirs('labels') 
except OSError:
       pass
"""
for txt_file in glob.iglob('./random/*.xml'):
    shutil.move(txt_file, dst)
