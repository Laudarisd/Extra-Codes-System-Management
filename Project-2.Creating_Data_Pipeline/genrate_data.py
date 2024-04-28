from datetime import datetime
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import os
import warnings
warnings.filterwarnings("ignore")



save_data = './data'

if not os.path.exists(save_data):
    os.makedirs(save_data)

#generate Time from start of 2016 to today
class GenerateData:
    def __init__(self):
        self.today = time.strftime("%Y-%m-%d")
    
    def generateTimeseries(self):
        self.Time = pd.date_range(start='2022-09-01', end=self.today, freq='m')
        self.df = pd.DataFrame(self.Time, columns=['Time'])
        #self.df = self.df.set_index('Time')

        return self.df
    def generateRandomData(self):
        self.df['var_a'] = np.random.randint(0, 100, size=len(self.Time))
        self.df['var_b'] = np.random.randint(-100, 100, size=len(self.Time))
        self.df['var_c'] = np.random.randint(2000, 3000, size=len(self.Time))
        self.df['temperture'] = np.random.randint(95, 99, size=len(self.Time))
        self.df['wind_speed'] = np.random.randint(0, 10, size=len(self.Time))
        self.df['wind_direction'] = np.random.randint(0, 360, size=len(self.Time))
        self.df['pressure'] = np.random.randint(1000, 1050, size=len(self.Time))
        self.df['humidity'] = np.random.randint(0, 100, size=len(self.Time))
        self.df['rain'] = np.random.randint(0, 100, size=len(self.Time))
        self.df['snow'] = np.random.randint(0, 100, size=len(self.Time))
        self.df['cloud'] = np.random.randint(0, 100, size=len(self.Time))
        self.df['visibility'] = np.random.randint(0, 100, size=len(self.Time))
        self.df['class'] = np.random.randint(0, 2, size=len(self.Time))

    def generateCSV(self):
        with open(os.path.join(save_data, 'data.csv'), 'w') as f:
            self.df.to_csv(f, index=False)
        #print(self.df.head(5))
    #now generate random row and append to csv at the end
    def generateSingleRow(self):
        #with time
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
                                    columns=['Time', 'var_a', 'var_b', 'var_c', 'temperture', 
                                            'wind_speed', 'wind_direction', 'pressure', 
                                            'humidity', 'rain', 'snow', 'cloud', 'visibility', 'class'])
        self.df = self.df.append(self.new_row, ignore_index=True)
        with open(os.path.join(save_data, 'data.csv'), 'a') as f:
            self.new_row.to_csv(f, header=False, index=False)
        print(self.new_row)
        
    def run(self):
        self.generateTimeseries()
        self.generateRandomData()
        self.generateCSV()
        self.generateSingleRow()

T = GenerateData()
T.run()

