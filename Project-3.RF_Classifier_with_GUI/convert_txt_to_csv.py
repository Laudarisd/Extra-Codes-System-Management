import numpy as np
import pandas as pd
import csv
import glob
import time


def main():
    start = time.time()
    data_folder = "./all/" #folder name
    files = glob.glob(data_folder + '*dump*.data')
    print("Total files:", len(files))
    # get header from one of the files
    header = []

    with open('all/dump46000.data', 'r') as f:
        #lines = f.readlines()
        header.extend(f.readline().split()[1:]) 
        timeStep = f.readline().split()
        
        for _ in range(6):
            next(f) # skip first 8 lines
        header.extend(f.readline().split()[2:]) 
        a = True
        print(header)
        headerString = ','.join(header)
        

    for file in files:
        with open(file, 'r') as f, open(f'all.csv', 'a') as g: # note the 'a'
            next(f)
            g.write(headerString+ '\n') # write the header
            timeStep = f.readline().split()
            for _ in range(7):
                next(f)
            for line in f:
                file_line = line.split()
                file_line.insert(0,timeStep[0])
                data = ','.join(file_line)
                g.write(data + '\n')

    print(time.time() - start)


if __name__ == "__main__":
    main()
