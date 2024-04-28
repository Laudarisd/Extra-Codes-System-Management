import exif
from PIL import Image
import glob
import tiffile as js
import json
import numpy as np
from PIL.ExifTags import GPSTAGS
from PIL.ExifTags import TAGS
from pprint import pprint
from PIL import Image
import piexif
import json

from torch._C import Value


codec = 'ISO-8859-1'  # or latin-1

#display exif data
def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()

# Get metadata information

def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")
    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")
            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    return geotagging

# Get key,and value
def get_labeled_exif(exif):
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val
    return labeled

#print(get_labeled_exif(filename))

#convert lat, alt to mapping coordinates
def get_decimal_from_dms(dms, ref):
#     degrees = dms[0]
#     minutes = dms[1] / 60.0
#     seconds = dms[2] / 3600.0
    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1] / 60.0
    seconds = dms[2][0] / dms[2][1] / 3600.0  
    if ref in ['S', 'E']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return round(degrees + minutes + seconds, 5)

def get_coordinates(geotags):
    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

    return (lat,lon)

#import files and check file types
def main():
    coor = []
    all_info = []
    root = glob.glob("./test_1/*.jpg")

    for filename in root:
            if filename.endswith(('jpg','JPG','png','PNG','tiff','TIFF')):
                img = filename[9:]
                exif = get_exif(filename)
                labeled = get_labeled_exif(exif)
                #pprint(labeled)
                for key, Value in labeled.items():
                    if key == "ImageLength":
                        image_height = Value
                    if key =="ImageLength":
                        image_width = Value
                    if key == "DateTime":
                        datetime = Value
                    if key == "Model":
                        model = Value
                    #print(coor)

                pprint(labeled)
                geotags = get_geotagging(exif)
                geo = get_coordinates(geotags)
                coor.append({"image_id":img, 
                            "Image_hight": image_height,
                            "Image_width": image_width,
                            "model": model,                           
                            "gps-coordinates":  geo})
                all_info.append({"all":labeled})
    #pprint(coor)
    #pprint(",".join(coor))
    
    pprint(coor)
    # lst = []
    # for child in coor:
    #     info = ["img_name", "gps"]
    #     lst1 = {k: v for k, v in zip(info, child)}
    #     lst.append(lst1)
    # pprint(lst)
    # for sub_list in lst:
    with open('gps.json', 'w') as f:   
        json.dump(coor, f)
    # with open('all_info.json', 'w') as file:
    #      json.dump(all_info, file)




if __name__ == '__main__':
    main()