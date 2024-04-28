import glob
import shutil
#import os
dst_dir = "./image"
print ('Named explicitly:')
for name in glob.glob('./image/*/*'):    
    if name.endswith(".jpg") or name.endswith(".png")  : 
        shutil.move(name, dst_dir)
        print ('\t', name)
