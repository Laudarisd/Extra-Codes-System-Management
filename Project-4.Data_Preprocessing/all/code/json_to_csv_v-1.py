import glob
import json
import csv
import os


#dir = "./annotations/"
save_csv = "./"

width = 1920
height = 1080

with open(os.path.join(save_csv, "night.csv"), "w", newline="") as file:
    csv_output = csv.writer(file)
    csv_output.writerow(["filename","width", "height", "class_name", "xmin", "ymin", "xmax", "ymax"])
    
    for single_file in glob.glob("./label/*.json"):
        change_name = os.path.basename(single_file)
        filename = change_name.split(".", 2) [0] + ".jpg"
        #print(single_file)
        with open(single_file) as f_json:
            json_data = json.load(f_json)
        for child in json_data["annotation"]:
            #print(child)
            for key, value in child.items():
                if key == "box":
                   print(value)

                if key == "class":
                   print(value)
                #print(key)
            #if child["annotation_type"] == "bbox":


                
        #         done = csv_output.writerow([
        #         #single_file,
        #         filename,
        #         width,
        #         height,
        #         child["class_name"],
        #         child["coord_xy"][0][0],
        #         child["coord_xy"][1][0],
        #         child["coord_xy"][0][1],
        #         child["coord_xy"][1][1],
        #         ])
        #         if done:
        #             print("Csv is saved")
        #         else:
        #             print("can't write csv")