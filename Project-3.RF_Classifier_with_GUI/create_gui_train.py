import csv
import math
import os
import time
from tkinter import messagebox, simpledialog
import warnings
import numpy as np
import pandas as pd
import joblib
from tqdm import tqdm
import seaborn as sns
from time import sleep
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report
from sklearn.metrics import precision_score, recall_score, roc_auc_score, roc_curve
#import precision recal curve
from sklearn.metrics import precision_recall_curve
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')


if not os.path.exists('./collision'):
    os.makedirs('./collision')


class RandomForestGUI:
    def __init__(self,master):
        self.master = master
        self.master.title("Random Forest Classifier")
        self.master.geometry("1500x800")
        self.master.resizable(False, False)
        self.save_model = {}
        # Define the four frames and fixed the value
        self.frame1 = tk.Frame(root, bg="white", width=700, height=300)
        self.frame2 = tk.Frame(root, bg="white", width=700, height=300)
        self.frame3 = tk.Frame(root, bg="white", width=700, height=300)
        self.frame4 = tk.Frame(root, bg="white", width=700, height=300)
        self.frame1.pack_propagate(0)
        self.frame2.pack_propagate(0)
        self.frame3.pack_propagate(0)
        self.frame4.pack_propagate(0)
        # Use the grid geometry manager to arrange the frames
        self.frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.frame3.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.frame4.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        # Add labels to the four frames
        self.label1 = tk.Label(self.frame1, text="Data Information")
        self.label2 = tk.Label(self.frame2, text="Train and Test Results")
        self.label3 = tk.Label(self.frame3, text="Feature Importance Plot")
        self.label4 = tk.Label(self.frame4, text="Precision and Recall Plot")
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()

        # Configure row and column weights to make the frames expand to fill the window
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        # Initialize the data and classifier variables
        self.data = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.rf = None

        #divide frame 2 into two frames and give tiles to each frame as Data Information and Data Visualization
        self.frame2_left = tk.Frame(self.frame2)
        self.frame2_right = tk.Frame(self.frame2)
        self.frame2_left.pack(side=tk.LEFT, padx=10, pady=10)
        self.frame2_right.pack(side=tk.RIGHT, padx=10, pady=10)
        #Display Ranfdom Forest information in subframe left
        
        #To choose RF parameters by user.
        # Add a label and entry widget for n_estimators
        self.n_estimators_label = tk.Label(self.frame2_left, text="Number of estimators(e.g. 100):", anchor='w', padx=5, pady=5)
        self.n_estimators_entry = tk.Entry(self.frame2_right)
        self.n_estimators_label.pack(side=tk.TOP, pady=5, ipady=3)
        self.n_estimators_entry.pack(side=tk.TOP, pady=5, ipady=3)
        #add a label and entry widget for max_depth
        self.max_depth_label = tk.Label(self.frame2_left, text="Maximum depth(e.g. 10):", anchor='w', padx=5, pady=5)
        self.max_depth_entry = tk.Entry(self.frame2_right)
        self.max_depth_label.pack(side=tk.TOP, pady=5, ipady=3)
        self.max_depth_entry.pack(side=tk.TOP, pady=5, ipady=3)

        #add a label and entry widget for random_state. Should be integer
        self.random_state_label = tk.Label(self.frame2_left, text="Random state(e.g. 0):", anchor='w', padx=5, pady=5)
        self.random_state_entry = tk.Entry(self.frame2_right)
        self.random_state_label.pack(side=tk.TOP, pady=5, ipady=3)
        self.random_state_entry.pack(side=tk.TOP, pady=5, ipady=3)
        #add a label and entry widget for n_jobs. Should be integer
        self.n_jobs_label = tk.Label(self.frame2_left, text="Number of jobs(e.g. 1):", anchor='w', padx=5, pady=5)
        self.n_jobs_entry = tk.Entry(self.frame2_right)
        self.n_jobs_label.pack(side=tk.TOP, pady=5, ipady=3)
        self.n_jobs_entry.pack(side=tk.TOP, pady=5, ipady=3)
        #add a label and entry widget for verbose. Should be integer
        self.verbose_label = tk.Label(self.frame2_left, text="Verbose(e.g. 0):", anchor='w', padx=5, pady=5)
        self.verbose_entry = tk.Entry(self.frame2_right)
        self.verbose_label.pack(side=tk.TOP, pady=5, ipady=3)
        self.verbose_entry.pack(side=tk.TOP, pady=5, ipady=3)
        # Add buttons to load data and train the model
        self.load_data_button = tk.Button(self.frame1, text="Load Data", command=self.load_data)
        self.load_data_button.pack(side=tk.BOTTOM, padx=10, pady=10, anchor=tk.CENTER)

        #Train
        self.train_button = tk.Button(self.frame2, text="Train Model", command=self.train_model, state=tk.DISABLED)
        self.train_button.pack(side=tk.BOTTOM, padx=10, pady=10, anchor=tk.CENTER)
        # # Add a button to save the model
        # self.save_model_button = tk.Button(self.frame2, text="Save Model", command=self.save_model, state=tk.DISABLED)
        # self.save_model_button.pack(side=tk.BOTTOM, padx=10, pady=10)
        # Add a button to predict on new data
        # self.predict_button = tk.Button(self.frame2, text="Predict", command=self.predict_model, state=tk.DISABLED)
        # self.predict_button.pack(side=tk.BOTTOM, padx=10, pady=10)
    def load_data(self):
        #Ask the user to select a file 
        filename = filedialog.askopenfilename(initialdir = "./", title = "Select file", filetypes = (("csv files","*.csv"),("all files","*.*")))
        #confirm that the user has selected a file
        if filename == '':
            return None
        #Load the data
        self.data = pd.read_csv(filename)
        #replace column name
        self.data.rename(columns={"omegax": "\u03A9x", "omegay": "\u03A9y", "omegaz": "\u03A9z", "v_acc":"acc", "v_mag_omega":"|\u03A9|",
                    "v_mag_v":"|v|", "v_mag_f":"|f|" }, inplace=True)
        self.data.sort_values(by='z', inplace=True, axis=0)
        initial_zone = self.data[(self.data['z'] > 3.6) & (self.data['z'] < 4.1)]
        cone_zone =    self.data[(self.data['z'] > 1.9) & (self.data['z'] < 3)]
        fall_zone =    self.data[(self.data['z'] > 0.8) & (self.data['z'] < 1.2)]
        ground_zone =  self.data[ self.data['z'] < 0.4]
        # Create a pop-up dialog box to get user input
        user_input = simpledialog.askstring("Input", "Enter zone (eg. collision, dense, all): ", parent=root)
        if user_input == "collision":
            self.data = pd.concat([initial_zone, fall_zone], axis=0)
        elif user_input == "dense":
            self.data = pd.concat([cone_zone, ground_zone], axis=0)
        elif user_input == "all":
            self.data_zone = pd.concat([initial_zone, cone_zone, fall_zone, ground_zone], axis=0)
        else:
            #return error message
            pass

        self.data.rename(columns={"acc": "a"}, inplace=True)
        # change the type of the data
        self.data['type'] = self.data['radius'].apply(lambda x: 0 if x == 0.03 else 1)
        # Split the data into features and target
        self.X = self.data.drop(['TIMESTEP', 'id', 'type', 'mass', 'radius'], axis=1)
        self.X.fillna(self.X.mean(), inplace=True)
        self.y = self.data['type']
        # Split the data into training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.25)

        #divide frame 1 into two frames and give tiles to each frame as Data Information and Data Visualization
        self.frame1_left = tk.Frame(self.frame1)
        self.frame1_right = tk.Frame(self.frame1)
        self.frame1_left.pack(side=tk.LEFT, padx=10, pady=10)
        self.frame1_right.pack(side=tk.RIGHT, padx=10, pady=10)
        #Display the data information in frame 1
        self.text = tk.Text(self.frame1_left, width=40)
        self.text.insert(tk.END, "Number of rows: {}\n".format(self.data.shape[0]))
        self.text.insert(tk.END, "Number of columns: {}\n".format(self.data.shape[1]))
        self.text.insert(tk.END, "Number of training rows: {}\n".format(self.X_train.shape[0]))
        self.text.insert(tk.END, "Number of testing rows: {}\n".format(self.X_test.shape[0]))
        self.text.insert(tk.END, "Number of features: {}\n".format(self.X_train.shape[1]))
        self.text.insert(tk.END, "Number of class: \n{}\n".format(self.y.value_counts()))
        self.text.insert(tk.END, "--------------------\n")
        #display all the columns names in green color
        self.text.tag_configure("green", foreground="green")
        self.text.insert(tk.END, "Training Features:\n", "green")
        for col in self.X.columns:
             self.text.insert(tk.END, "{},".format(col))        
        self.text.pack(side=tk.LEFT, padx=10, pady=10)
        #Display the data visualization in frame 1of n_estimators from the entry widget
        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.scatter(self.data['x'], self.data['z'], c=self.data['type'], cmap='bwr')
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_title('Data Visualization')
        self.canvas = FigureCanvasTkAgg(self.figure, self.frame1_right)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        #Enable the train model button
        self.train_button['state'] = tk.NORMAL
    def train_model(self):
        # Get the value for all the hyperparameterswarm_start = self.warm_start_entry.get()
        n_estimators_entry = self.n_estimators_entry.get()
        if n_estimators_entry == '':
            n_estimators = 100
        else:
            n_estimators = int(n_estimators_entry)
        max_depth = self.max_depth_entry.get()
        if max_depth == '':
            max_depth = 9
        else:
            max_depth = int(max_depth)
        random_state = self.random_state_entry.get()
        if random_state == '':
            random_state = 42
        else:
            random_state = int(random_state)
        n_jobs = self.n_jobs_entry.get()
        if n_jobs == '':
            n_jobs = 1
        else:
            n_jobs = int(n_jobs)
        
        verbose = self.verbose_entry.get()
        if verbose == '':
            verbose = 0
        else:
            verbose = int(verbose)
        #check if the values are not enters then warn the user that the default values are used
        if n_estimators_entry == '' or max_depth == '' or random_state == '' or n_jobs == '' or verbose == '':
            messagebox.showwarning("Warning", "Some of the hyperparameters are not entered. Default values will be used.")
        #Train the model
        self.rf = RandomForestClassifier(n_estimators=n_estimators, 
                                        random_state=random_state, 
                                        max_depth=max_depth, 
                                        n_jobs=n_jobs, 
                                        verbose=verbose)
        self.rf.fit(self.X_train, self.y_train)
        #disable the train model button
        self.train_button['state'] = tk.DISABLED
        # Visualize training in frame 2
        self.text1 = tk.Text(self.frame2_left, width=40)
        self.text1.insert(tk.END, "Random Forest Information:\n")
        self.text1.insert(tk.END, "Number of estimators: {}\n".format(self.rf.n_estimators))
        self.text1.insert(tk.END, "Max depth: {}\n".format(self.rf.max_depth))
        self.text1.insert(tk.END, "Number of features: {}\n".format(self.rf.n_features_))
        self.text1.insert(tk.END, "Number of classes: {}\n".format(self.rf.n_classes_))
        self.text1.insert(tk.END, "--------------------\n")
        self.text1.pack(side=tk.LEFT, padx=10, pady=10)

        # Display training information in subframe right
        self.text2 = tk.Text(self.frame2_left, width=40)
        y_pred = self.rf.predict(self.X_test)
        self.text2.insert(tk.END, "Training Accuracy: {:.2f}\n".format(self.rf.score(self.X_train, self.y_train)))
        self.text2.insert(tk.END, "Testing Accuracy: {:.2f}\n".format(self.rf.score(self.X_test, self.y_test)))
        #self.text2.insert(tk.END, "Precision: {:.2f}\n".format(precision_score(self.y_test, y_pred, average='weighted')))
        #self.text2.insert(tk.END, "Recall: {:.2f}\n".format(recall_score(self.y_test, y_pred, average='weighted')))
        self.text2.insert(tk.END, "F1 Score: {:.2f}\n".format(f1_score(self.y_test, y_pred, average='weighted')))
        self.text2.pack(side=tk.RIGHT, padx=10, pady=10)
        self.feature_importance()
        #Visualize the precision and recall in frame 4
        self.actual_predicted()

    def feature_importance(self):
        # Get the feature importances from self.rf
        importances = self.rf.feature_importances_
        # Get the names of the features from self.X.columns
        features = self.X.columns
        # Get the indices that would sort the importances array
        sorted_indices = np.argsort(importances)
        # Sort the feature importances and feature names in descending order
        sorted_importances = importances[sorted_indices][::-1]
        sorted_features = features[sorted_indices][::-1]
        # Create a bar plot of the feature importances
        fig = plt.Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.barh(y=sorted_features, width=sorted_importances, color='b', alpha=0.7)
        # Set the title of the plot
        ax.set_title('Feature Importance')
        # Create a canvas and show the plot in frame 3
        canvas = FigureCanvasTkAgg(fig, master=self.frame3)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        #after prediction print don and move to frame 4 automatically
        self.actual_predicted()
    def actual_predicted(self):
        y_pred = self.rf.predict(self.X_test)
        #plot the actual vs predicted values in frame 4
        fig = plt.Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.scatter(self.y_test, y_pred)
        # Set the title and axis labels of the plot
        ax.set_title('Actual vs Predicted Values')
        ax.set_xlabel('Actual Values')
        ax.set_ylabel('Predicted Values')
        # Create a canvas and show the plot in frame 4
        canvas = FigureCanvasTkAgg(fig, master=self.frame4)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomForestGUI(root)
    root.mainloop()
