# import tkinter
from tkinter import scrolledtext 
from tkinter import *

from datetime import datetime
from pandastable import Table

import serial
import time

from database import *
import gui_Functions

ActiveSubject = 'ClassList'

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
Sub_OptionMenu__Label = Label(top_R, text="Subject :", font=("Helvetica", 12))
Sub_OptionMenu = OptionMenu(top_R, Sub_OptionMenu__Var, *Sub_OptionMenu__List)
# Sub_OptionMenu = OptionMenu(top_R, Sub_OptionMenu__Var, *Sub_OptionMenu__List, command = subject_selected)

Sub_OptionMenu__Label.grid()
Sub_OptionMenu.grid()

Column_name__Var = StringVar()
Column_name__List = list(database[ActiveSubject][0].columns)
Column_name__Label = Label(top_R, text="Column Name:", font=("Helvetica", 12))
Column_name = OptionMenu(top_R, Column_name__Var, *Column_name__List)

Column_name__Label.grid()
Column_name.grid()

##############  DATABASE FRAME 
middle = Frame(root)
middle.grid(row=1, column=0, pady=20, padx=20)

##############  STATUS FRAME
bottom = Frame(root)
bottom.grid(row=1, column=1, pady=20, padx=20)

status = scrolledtext.ScrolledText(bottom, wrap = WORD, width =60, height = 25, font = ("Times New Roman",12))
status.grid()


##############  SHOWING THE GUI 
gui_Functions.update_time_date_labels(time_label, date_label, root)
root.mainloop()

