import tkinter
from tkinter import scrolledtext 
from tkinter import *

from pandastable import Table, TableModel
import serial
import time
from database import *
from gui_Functions import *

def update_time_date_labels():
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d - %m - %Y")
    time_label.config(text="Time: " + current_time)
    date_label.config(text="Date: " + current_date)
    root.after(1000, update_time_date_labels)

def subject_selected(showingSubject):
    # showingSubject = sub.get()
    Sub_OptionMenu__Label.config(text="Subject: " + showingSubject)
    print(f"Showing {showingSubject} Attandence Record")
    show_db(showingSubject)

def show_db(subject):  
    middle.table = Table(middle, dataframe=database[subject][0], showtoolbar=False, showstatusbar=False ,editable=False, height = 550, width = 700)
    middle.table.show()

# activeSubject = 'Class List'

###############  MAIN WINDOW 
root = Tk()
root.geometry("1500x1000")
# root.attributes('-fullscreen', True)
root.title("RFID Attendance System")


##############  TOP_L FRAME 
top_L = Frame(root)
top_L.grid(row=0, column=0, pady=20, padx=20)

heading_label = Label(top_L, text="Electrical Department", font=("Helvetica", 24))
date_label = Label(top_L, text="Current Date: ", font=("Helvetica", 12))
time_label = Label(top_L, text="Current Time: ", font=("Helvetica", 12))

heading_label.grid()
date_label.grid()
time_label.grid()

##############  TOP_R FRAME 
top_R = Frame(root, borderwidth=3)
top_R.grid(row=0, column=1, pady=10, padx=20)

Sub_OptionMenu__Var = StringVar()
Sub_OptionMenu__List = list(database.keys())
Sub_OptionMenu__Label = Label(top_R, text="Subject :", font=("Helvetica", 12)).grid()
Sub_OptionMenu = OptionMenu(top_R, Sub_OptionMenu__Var, *Sub_OptionMenu__List, command = subject_selected).grid()

Column_name__Var = StringVar()
Column_name__List = list(database[str(Sub_OptionMenu__Var)][0].columns)
Column_name__Label = Label(top_R, text="Column Name:", font=("Helvetica", 12)).grid()
Column_name = OptionMenu(top_R, Column_name__Var, *Column_name__List).grid()


##############  DATABASE FRAME 
middle = Frame(root)
middle.grid(row=1, column=0, pady=20, padx=20)

##############  STATUS FRAME
bottom = Frame(root)
bottom.grid(row=1, column=1, pady=20, padx=20)

status = scrolledtext.ScrolledText(bottom, wrap = WORD, width =60, height = 25, font = ("Times New Roman",12))
status.grid()


##############  SHOWING THE GUI 
update_time_date_labels()
root.mainloop()

