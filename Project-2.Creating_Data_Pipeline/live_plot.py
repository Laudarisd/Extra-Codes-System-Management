import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import warnings
warnings.filterwarnings("ignore")

plt.style.use('fivethirtyeight')

#x_values = []
#y_values = []

# index = count()
# plt.figure(figsize=(20, 6))
# def animate(i):
#     data = pd.read_csv('./data/data.csv')
#     x_values = data['Time']
#     y_values = data['wind_speed']
#     #plot only 20 data points at a time
#     x_values = x_values[-20:]
#     y_values = y_values[-20:]

#     plt.cla()
#     plt.plot(x_values, y_values)
#     plt.xlabel('Time')
#     plt.ylabel('Wind Speed')
#     plt.title('Wind Speed over Time')
#     plt.gcf().autofmt_xdate()
#     plt.tight_layout()

# ani = FuncAnimation(plt.gcf(), animate, 5000)
# plt.tight_layout()
# plt.show()


index = count()
fig, ax = plt.subplots(nrows = 6, ncols=2, figsize=(15, 12))
fig.tight_layout(pad=5)


def animate(i):
    data = pd.read_csv('./data/data.csv')
    average_list  = data.mean().tolist()
    #plot all columns
    plt.cla()
    for i in range(0, 6):
        for j in range(0, 2):
            ax[i, j].cla()
            #drop the first column and the last column and plot only 50 data points at a time
            #print(data.iloc[:, i*2+j+1][-20:])
            ax[i, j].plot(data.iloc[:, i*2+j+1][-50:], linewidth=2, linestyle='--', color='blue') 
            #threshold line for each plot from the average of the column
            ax[i, j].axhline(y=average_list[i*2+j+1], color='r', linestyle='-', linewidth=2)
            
            #ax[i, j].plot(data.iloc[:, i*2+j+1])
            #ax[i, j].set_title(data.columns[i*2+j+1], fontsize=10)
            #ax[i, j].set_xlabel('Time', fontsize=10)
            ax[i, j].set_ylabel(data.columns[i*2+j+1], fontsize=10)
            ax[i, j].set_xticklabels(data['Time'], rotation=15, fontsize=10)
            ax[i, j].set_yticklabels(data.iloc[:, i*2+j+1], fontsize=10)
            ax[i, j].grid(True)
            #ax[i, j].legend(loc='upper right', fontsize=10)
    
    plt.gcf().autofmt_xdate()
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, 5000)
plt.tight_layout()
plt.show()
#print(animate(1))