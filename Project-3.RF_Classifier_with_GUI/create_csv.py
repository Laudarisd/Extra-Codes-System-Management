import os
import glob
import csv


def convert_folder_to_csv(folder_path):
    # get all .data files in the folder
    files = glob.glob(os.path.join(folder_path, '*.data'))
    
    if len(files) == 0:
        return  # no data files in this folder
    
    # create output CSV file in csv folder with the subfolder name
    csv_folder = os.path.join(folder_path, '..', 'csv')
    os.makedirs(csv_folder, exist_ok=True)
    output_file = os.path.join(csv_folder, os.path.basename(folder_path) + '.csv')
    
    # get header from one of the files
    header = []
    with open(files[0], 'r') as f:
        header.extend(f.readline().split()[1:]) 
        timeStep = f.readline().split()
        for _ in range(6):
            next(f) # skip first 6 lines
        header.extend(f.readline().split()[2:])
    
    # write data to CSV file
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for file in files:
            with open(file, 'r') as g:
                next(g)
                timeStep = g.readline().split()
                for _ in range(7):
                    next(g)
                for line in g:
                    row = line.split()
                    row.insert(0, timeStep[0])
                    writer.writerow(row)


def main():
    data_folder = './time'  # main folder containing subfolders
    
    for root, dirs, files in os.walk(data_folder):
        for dir in dirs:
            subfolder_path = os.path.join(root, dir)
            convert_folder_to_csv(subfolder_path)


if __name__ == '__main__':
    main()
