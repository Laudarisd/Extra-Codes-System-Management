#Parse a single json file


import json

# read file
with open('./annotations/_-0aygxELCt_AvFtXT-iOA.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

# show values
#print("usd: " + str(obj['usd']))
#print("eur: " + str(obj['eur']))
#print("gbp: " + str(obj['gbp']))
print(obj)

###############################################################################
#Convert all json to a single csv file. 
# Csv will include file name, width, height, key, label, xmin, ymin, x max, ymax


import glob
import json 
import csv
import os

dir = "./annotations/"
save_dir = "./"

with open(os.path.join(save_dir, 'test.csv'), 'w', newline='') as f_csv:
    csv_output = csv.writer(f_csv)
    csv_output.writerow(["file_name","width","height","key", "label", "xmin", "ymin", "xmax", "ymax"])
    
    for single_file in glob.glob("./annotations/*.json"):
        #print(single_file)
        change_name = os.path.basename(single_file)
        filename = change_name.split( ".", 2) [0] + ".jpg"
        
        with open(single_file) as f_json:
            json_data = json.load(f_json)

        for object in json_data["objects"]:
            done = csv_output.writerow([
                #single_file,
                filename,
                json_data["width"],
                json_data["height"],
                object["key"],
                object["label"],
                object["bbox"]["xmin"],
                object["bbox"]["ymin"],
                object["bbox"]["xmax"],
                object["bbox"]["ymax"]
            ])
            if done:
                print("Csv is saved")
            else:
                print("can't write csv")
