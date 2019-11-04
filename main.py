from tkinter import filedialog
from tkinter import *
from tkinter.ttk import * 
import backend as be

input_data = ""
output_data = ""

def submit_button():
    print(input_data)
    print(output_data)
    if input_data != "" and output_data != "":
        be.cor_cal(input_data, output_data)

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global input_data
    input_data = filedialog.askdirectory() + "/*.csv"

def output_button():
    global output_data
    output_data = filedialog.askdirectory()

root = Tk()
root.title("LTE RSSI Correlation Analyzer")
root.geometry('400x120')

style = Style()
style.configure('Send.TButton', font=('calibri', 10, 'bold', 'underline'), background = 'blue')

button1 = Button(text="Select Folder Where Traces Are Located", command=browse_button)
button1.grid(row = 0, column = 3, padx = 100) 

button2 = Button(text="Select Folder Where Results will be saved", command=output_button)
button2.grid(row = 1, column = 3, pady = 10, padx = 100)

button3 = Button(root, text="Submit", style='Send.TButton', command=submit_button)
button3.grid(row = 2, column = 3, pady = 10, padx = 100)

mainloop()