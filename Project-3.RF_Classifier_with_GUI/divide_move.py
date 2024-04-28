import os
import shutil

# Define the path of the folder containing all files
folder_path = "./all"

# Create the 'time' directory if it doesn't exist
if not os.path.exists("./time"):
    os.mkdir("./time")

total_steps = 250000
discharge_time = 25
total_file = 311

file_per_second = total_file / discharge_time

# Loop through each file in the 'all' folder
for i, file_name in enumerate(os.listdir(folder_path)):
    # Create a new directory for each time step where total subfolders = total time steps. 
    # Folder should be like 1s, 2s, and so on
    time_step = int(i / file_per_second) + 1
    time_step_folder = "./time/" + str(time_step) + "s"
    if not os.path.exists(time_step_folder):
        os.mkdir(time_step_folder)
