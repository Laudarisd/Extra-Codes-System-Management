#Import the required modules

import pandas as pd
import os
import numpy as np
import re



with open("./config.txt", "w") as file:
    #a=append,w=write,r=read
    file.write("file_name = annotation.csv\n")
    file.write("width = 1024\n")
    file.write("height = 1024\n")
    file.write("xmin = xmin\n")
    file.write("ymin = ymin\n")
    file.write("xmax = xmax\n")
    file.write("ymax = ymax\n")
    file.write("label = class\n")
    file.write("class_name = nine,ten,jack,queen,king,ace\n")
    file.write("output_csv_name = yolo_output_voc\n")
    file.write("txt_file_path = ./train/\n")
    file.write("txt_images_path = ./\n")
    file.close()
        
