import os
import shutil


def extract_testprint_images(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('-TestPrint.png'):
                full_file_path = os.path.join(root, file) # full path of the file
                
                shutil.copy(full_file_path, destination_dir)
                print(f'Copied {full_file_path} to {destination_dir}')
                
source_dir = './sudip-layers'
destination_dir = './filter_data'

extract_testprint_images(source_dir, destination_dir)

                