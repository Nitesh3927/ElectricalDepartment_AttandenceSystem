# import tkinter
from tkinter import scrolledtext 
from tkinter import *

from datetime import datetime
from pandastable import Table

import serial
import time

from database import *
from gui_Functions import DropDowns, update_time_date_labels

ActiveSubject = database[0]

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

subject_selection = DropDowns(root=top_R, text='Subject u want to see:')
subject_selection.create_Dropdown(elements=[x.subjectName for x in database], fun= subject_selection.subject_selected)

col_selection = DropDowns(root=top_R, text='Select lecture')
col_selection.create_Dropdown(elements=ActiveSubject.dates_cols)

##############  DATABASE FRAME 
middle = Frame(root)
middle.grid(row=1, column=0, pady=20, padx=20)

##############  STATUS FRAME
bottom = Frame(root)
bottom.grid(row=1, column=1, pady=20, padx=20)

status = scrolledtext.ScrolledText(bottom, wrap = WORD, width =60, height = 25, font = ("Times New Roman",12))
status.grid()


##############  SHOWING THE GUI 
update_time_date_labels(time_label, date_label, root)
root.mainloop()

