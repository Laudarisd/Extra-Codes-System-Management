from datetime import datetime
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import os
import warnings
import csv
warnings.filterwarnings("ignore")



save_data = './data'

if not os.path.exists(save_data):
    os.makedirs(save_data)

#generate Time from start of 2016 to today
class GenerateData:
    def __init__(self):
        self.today = time.strftime("%Y-%m-%d")
        self.start = '2022-09-01'
        self.columns=['Time', 'var_a', 'var_b', 'var_c', 'temperture', 
                                            'wind_speed', 'wind_direction', 'pressure', 
                                            'humidity', 'rain', 'snow', 'cloud', 'visibility', 'class']
    def generateSingleRow(self):
        self.current_data_time = datetime.now()
        self.current_data_time = self.current_data_time.strftime("%Y-%m-%d %H:%M:%S")
        #only date
        #self.current_data_date = datetime.now().date()
        self.new_row = pd.DataFrame([[self.current_data_time, 
                                    random.randint(0, 100),
                                    random.randint(-100, 100), 
                                    random.randint(2000, 3000),
                                    random.randint(95, 99),
                                    random.randint(0, 10),
                                    random.randint(0, 360),
                                    random.randint(1000, 1050),
                                    random.randint(0, 100),
                                    random.randint(0, 100),
                                    random.randint(0, 100),
                                    random.randint(0, 100),
                                    random.randint(0, 100),
                                    random.randint(0, 1)]], 
                                    columns=self.columns)
        with open(os.path.join(save_data, 'data.csv'), 'a') as f:
            headers = self.columns
            writer = csv.writer(f, delimiter=',')
            if f.tell() == 0:
                writer.writerow(headers)
            self.new_row.to_csv(f, header=False, index=False)
        print(self.new_row)
     
#     def run(self):
#         self.generateSingleRow()
# T = GenerateData()
# T.run()

