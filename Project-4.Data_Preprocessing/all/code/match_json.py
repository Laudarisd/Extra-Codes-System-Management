import os
import json
import glob



f = open("./result.json", "r", encoding="utf-8")
data = json.load(f)
f.close()


ff = open("./gps.json", "r", encoding="utf-8")
data1 = json.load(ff)
ff.close()
#print(data1)


final_result = []

for j in data1:
    for key, value in j.items():
        if key =="image_id":
            image1 = value
        if key == "prediction":
            rslt1 = value
        if key == "ImageLength":
            image_height = value
        if key =="ImageLength":
            image_width = value
        if key == "DateTime":
            datetime = value
        if key == "Model":
            model = value
        if key == "gps-coordinates":
            geo = value

    for i in data:
        for key, value in i.items():
            if key =="image_id":
                image = value
            if key == "prediction":
                rslt = value

        for m in image1:
            for n in image:
                if n == m :
                    final_result.append({"image_id":m, 
                                    # "Image_hight": image_height,
                                        #"Image_width": image_width,
                                        #"model": model,                           
                                        "gps-coordinates":geo,
                                        "prediction:":rslt})
                                        #"gps":gps-coordinates})
                    
                    print(final_result)


        with open('test.json', 'w') as f:   
                json.dump(final_result, f)