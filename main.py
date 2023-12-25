from tkinter import scrolledtext 
from tkinter import Frame, Tk, Label, WORD
from datetime import datetime

import serial
import time
import logging

from database import database
from database import DatabaseHandler, AttandenceAddition, NewColumn, StudentInfo

from gui_Functions import DropDowns, update_time_date_labels

logging.basicConfig(filename="newfile.log",
                    level = logging.INFO,
                    format='--> %(message)s',
                    filemode='w')


start = time.time()

logging.info(f'ID of database[0] : {id(database[0])}')
logging.info(f'ID of database[1] : {id(database[1])}')
logging.info(f'ID of database[2] : {id(database[2])}')
logging.info(f'ID of database[3] : {id(database[3])}')


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

##############  DATABASE FRAME 
middle = Frame(root)
middle.grid(row=1, column=0, pady=20, padx=20)

##############  STATUS FRAME
bottom = Frame(root)
bottom.grid(row=1, column=1, pady=20, padx=20)

status = scrolledtext.ScrolledText(bottom, wrap = WORD, width =60, height = 25, font = ("Times New Roman",12))
status.grid()

##############  TOP_R FRAME 
top_R = Frame(root, borderwidth=3)
top_R.grid(row=0, column=1, pady=10, padx=20)

subject_selection = DropDowns(
    root=top_R, 
    text='Subject u want to see:', 
    database_frame=middle, 
    Active=database[0])

subject_selection.create_Dropdown(
    elements=[x.subjectName for x in database], 
    fun= subject_selection.subject_selected)

col_selection = DropDowns(
    root=top_R, 
    text='Select lecture', 
    Active=subject_selection.Active.dates_cols)

col_selection.create_Dropdown(
    elements=subject_selection.Active.dates_cols, 
    fun=col_selection.lecture_selected)


##############  SHOWING THE GUI 
update_time_date_labels(time_label, date_label, root)
end = time.time()
print(f"Execution time of the program is -------> {(end-start)*100:.3f}ms\n")
root.mainloop()


print(f'END--->\nID of ActiveSubject : {id(subject_selection.Active)}\n')
print(subject_selection.Active)



# print(f'ID of ActiveSubject : {id(ActiveSubject)}')