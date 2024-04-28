import sys
import os
import csv
from lxml import etree
import pandas as pd
import math

filename = 'image'
csvFiles = pd.read_csv('image.csv', header=0)
former_id = 'abc'
once = True


for csvFile in csvFiles.iterrows():
    #print('cnt: ', cnt)
    #xmlFile = csvFile[:-4] + '.xml'
    image_id = csvFile[1][1][:-4]
    print(image_id)
        
    xmlFile = '{}_{}.xml'.format(filename, image_id)
    #xmlFile = '{}.xml'.format(image_id)
    
    
    xmlData = open(xmlFile, 'a')

    #row[i] = row[0].replace(' ', '_')
    if former_id == 'abc':
        former_id = image_id
    print('former: ',former_id)
    
    if image_id == former_id:
        
        if once == True:
            xmlData.write('<annotation>' +"\n")

            xmlData.write('\t<folder>' +'train_images' + '</folder>' + "\n")
            xmlData.write('\t<filename>'+ '{}.png'.format(image_id) +'</filename>' +  "\n")
            xmlData.write('\t<path>'+ '/home/test/Desktop/context_detector_program' +'</path>' +  "\n")
            xmlData.write('\t<source>'+  "\n")
            xmlData.write('\t \t<database>'+ 'Unknown' + '</database>' +  "\n")
            xmlData.write('\t</source>'+  "\n")
            xmlData.write('\t<size>' + "\n")

            xmlData.write('\t    ' + '<' + 'width' + '>' \
                                          + '3000' + '</' + 'width' + '>' + "\n")
            xmlData.write('\t    ' + '<' + 'height' + '>' \
                                          + '3000' + '</' + 'height' + '>' + "\n")
            xmlData.write('\t    ' + '<' + 'depth' + '>' \
                                          + '3' + '</' + 'depth' + '>' + "\n")
            xmlData.write('\t</size>'+  "\n")
            xmlData.write('    ' + '<' + 'segmented' + '>' \
                                  + '0' + '</' + 'segmented' + '>' + "\n")
            once = False

        type_name = csvFile[1][3]

        xmlData.write('\t<object>' + "\n")
        xmlData.write('\t    ' + '<' + 'name' + '>' \
                          + '{}'.format(type_name) + '</' + 'name' + '>' + "\n")
        xmlData.write('\t    ' + '<' + 'pose' + '>' \
                          + 'Unspecified' + '</' + 'pose' + '>' + "\n")
        xmlData.write('\t    ' + '<' + 'truncated' + '>' \
                          + '0' + '</' + 'truncated' + '>' + "\n")
        xmlData.write('\t    ' + '<' + 'difficult' + '>' \
                          + '0' + '</' + 'difficult' + '>' + "\n")
        xmlData.write('\t\t<bndbox>'+  "\n")


        #coor = csvFile[1][0].split(',')
        #x_coor = csvFile[1][0].split(',')[::2]
        #y_coor = csvFile[1][0].split(',')[1::2]
        
        coordinates = csvFile[1][0].split(',')
        coor = [str(math.ceil(float(coor))) for coor in coordinates]
        x_coordinates = csvFile[1][0].split(',')[::2]
        x_coor = [str(math.ceil(float(x_coor))) for x_coor in x_coordinates]
        #coor = 
        y_coordinates = csvFile[1][0].split(',')[1::2]
        y_coor = [str(math.ceil(float(y_coor))) for y_coor in y_coordinates]

        xmlData.write('\t\t    ' + '<' + 'xmin' + '>' \
                          + min(x_coor) + '</' + 'xmin' + '>' + "\n")
        xmlData.write('\t\t    ' + '<' + 'ymin' + '>' \
                          + min(y_coor) + '</' + 'ymin' + '>' + "\n")
        xmlData.write('\t\t    ' + '<' + 'xmax' + '>' \
                          + max(x_coor) + '</' + 'xmax' + '>' + "\n")
        xmlData.write('\t\t    ' + '<' + 'ymax' + '>' \
                          + max(y_coor) + '</' + 'ymax' + '>' + "\n")
        xmlData.write('\t\t</bndbox>'+  "\n")

        xmlData.write('\t</object>' + "\n")
        xmlData.close()

        former_id = image_id
        print(former_id,'<former  /  image>', image_id)
    else:
        
        xmlFile = '{}_{}.xml'.format(filename, former_id)
        xmlData = open(xmlFile, 'a')
        xmlData.write('</annotation>' + "\n")
        xmlData.close()

        
        
        xmlFile = '{}_{}.xml'.format(filename, image_id)
        xmlData = open(xmlFile, 'a')
        
        xmlData.write('<annotation>' +"\n")

        xmlData.write('\t<folder>' +'train_images' + '</folder>' + "\n")
        xmlData.write('\t<filename>'+ '{}.png'.format(image_id) +'</filename>' +  "\n")
        xmlData.write('\t<path>'+ '/home/test/Desktop/context_detector_program' +'</path>' +  "\n")
        xmlData.write('\t<source>'+  "\n")
        xmlData.write('\t \t<database>'+ 'Unknown' + '</database>' +  "\n")
        xmlData.write('\t</source>'+  "\n")
        xmlData.write('\t<size>' + "\n")

        xmlData.write('\t    ' + '<' + 'width' + '>' \
                                      + '3000' + '</' + 'width' + '>' + "\n")
        xmlData.write('\t    ' + '<' + 'height' + '>' \
                                      + '3000' + '</' + 'height' + '>' + "\n")
        xmlData.write('\t    ' + '<' + 'depth' + '>' \
                                      + '3' + '</' + 'depth' + '>' + "\n")
        xmlData.write('\t</size>'+  "\n")
        xmlData.write('    ' + '<' + 'segmented' + '>' \
                              + '0' + '</' + 'segmented' + '>' + "\n")

        type_name = csvFile[1][3]

        xmlData.write('\t<object>' + "\n")
        xmlData.write('\t    ' + '<' + 'name' + '>' \
                          + '{}'.format(type_name) + '</' + 'name' + '>' + "\n")
        xmlData.write('\t    ' + '<' + 'pose' + '>' \
                          + 'Unspecified' + '</' + 'pose' + '>' + "\n")
        xmlData.write('\t    ' + '<' + 'truncated' + '>' \
                          + '0' + '</' + 'truncated' + '>' + "\n")
        xmlData.write('\t    ' + '<' + 'difficult' + '>' \
                          + '0' + '</' + 'difficult' + '>' + "\n")
        xmlData.write('\t\t<bndbox>'+  "\n")


        #coor = csvFile[1][0].split(',')
        #x_coor = [int(math.ceil(csvFile[1][0].split(',')[::2]]
        #y_coor = csvFile[1][0].split(',')[1::2]
        coordinates = csvFile[1][0].split(',')
        coor = [str(math.ceil(float(coor))) for coor in coordinates]
        x_coordinates = csvFile[1][0].split(',')[::2]
        x_coor = [str(math.ceil(float(x_coor))) for x_coor in x_coordinates]
        #coor = 
        y_coordinates = csvFile[1][0].split(',')[1::2]
        y_coor = [str(math.ceil(float(y_coor))) for y_coor in y_coordinates]
        

        xmlData.write('\t\t    ' + '<' + 'xmin' + '>' \
                          + min(x_coor) + '</' + 'xmin' + '>' + "\n")
        xmlData.write('\t\t    ' + '<' + 'ymin' + '>' \
                          + min(y_coor) + '</' + 'ymin' + '>' + "\n")
        xmlData.write('\t\t    ' + '<' + 'xmax' + '>' \
                          + max(x_coor) + '</' + 'xmax' + '>' + "\n")
        xmlData.write('\t\t    ' + '<' + 'ymax' + '>' \
                          + max(y_coor) + '</' + 'ymax' + '>' + "\n")
        xmlData.write('\t\t</bndbox>'+  "\n")

        xmlData.write('\t</object>' + "\n")
        xmlData.close()

        former_id = image_id

            
            
        xmlData.close()    
            
            
        former_id = image_id
        print(former_id,'<former  /  image>', image_id)
xmlFile = '{}_{}.xml'.format(filename, former_id)
xmlData = open(xmlFile, 'a')
xmlData.write('</annotation>' + "\n")
xmlData.close()

#print(row[i].split(','))
#print(min(x_coor), min(y_coor), max(x_coor), max(y_coor))




