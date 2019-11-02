from tkinter import filedialog
from tkinter import *
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
root.geometry('500x200')

button1 = Button(text="Input Data Folder", command=browse_button)
button1.grid(row=0, column=0)

button2 = Button(text="Output Results Folder", command=output_button)
button2.grid(row=2, column=0)

button3 = Button(text="Submit", command=submit_button)
button3.grid(row=4, column=0)

mainloop()