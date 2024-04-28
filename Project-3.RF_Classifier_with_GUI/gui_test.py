import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Random Forest Results")
root.geometry("800x600")

# Define the four frames
frame1 = tk.Frame(root, bg="white")
frame2 = tk.Frame(root, bg="white")
frame3 = tk.Frame(root, bg="white")
frame4 = tk.Frame(root, bg="white")

# Use the grid geometry manager to arrange the frames
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
frame3.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
frame4.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Add labels to the four frames
label1 = tk.Label(frame1, text="Data Information")
label2 = tk.Label(frame2, text="Train and Test Results")
label3 = tk.Label(frame3, text="Feature Importance Plot")
label4 = tk.Label(frame4, text="Precision and Recall Plot")
label1.pack()
label2.pack()
label3.pack()
label4.pack()

# Configure row and column weights to make the frames expand to fill the window
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# Start the GUI event loop
root.mainloop()




