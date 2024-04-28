## image format changer

from PIL import Image
import os
import argparse


def search_dir(dirname):
    result_file_list = []

    filenames = os.listdir(dirname)
    for filename in filenames:
        full_path = os.path.join(dirname, filename)

        if os.path.isdir(full_path):
            if filename != 'convert':
                result_file_list.extend(search_dir(full_path))
        else:
            result_file_list.append(full_path)
    
    return result_file_list

P = argparse.ArgumentParser()
P.add_argument('-f', type=str)
P.add_argument('-e', type=str)

args = P.parse_args()

if args.f is None or args.e is None:
    print("use : python changer.py -f <img folder path> -e <save folder path>")
else:

    file_list = search_dir(args.f)

    new_format = args.e
    if new_format[0] != '.':
        new_format = '.' + new_format


    for file in file_list:
        new_folder = os.path.split(file)[0] + '/convert'
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        src_filename = os.path.splitext(file)[0]   # dddd.jpg ---name 
        new_file = new_folder + '/' + src_filename.split("/")[-1] + new_format
        #print(new_file)

        #img = img.open(file)
        #img.save(new_file)
        

        try:
            img = Image.open(file)
            img.verify()   # check img
            img.close()

            img = Image.open(file)
            img.save(new_file)
        
        except:
            pass



