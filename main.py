import time
start = time.time()

from tkinter import scrolledtext 
from tkinter import Frame, Tk, Label, WORD
# from datetime import datetime

# import serial
import logging

from data_manager import database
# from database import DatabaseHandler

from gui_manager import DropDowns, update_time_date_labels, SubjectSelection, DateSelection

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file = logging.FileHandler(filename='GeneralFlow.log', mode='w')

formatter = logging.Formatter('%(module)s-%(funcName)s --> %(message)s')
file.setFormatter(formatter)

logger.addHandler(file)



logger.info(f'ID of database[0] : {id(database[0])}')
logger.info(f'ID of database[1] : {id(database[1])}')
logger.info(f'ID of database[2] : {id(database[2])}')
logger.info(f'ID of database[3] : {id(database[3])}')


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

subject_selection = SubjectSelection(root= top_R, database_frame= middle)

date_selection = DateSelection(root=top_R, database_frame= middle)


# # -------------------------------------------------------------------------------------------
# subject_selection = DropDowns(
#     root=top_R, 
#     text='Subject u want to see:', 
#     database_frame=middle, 
#     Active=database[0])

# subject_selection.create_Dropdown(
#     elements=[x.subjectName for x in database], 
#     fun= subject_selection.subject_selected)

# col_selection = DropDowns(
#     root=top_R, 
#     text='Select lecture', 
#     Active=subject_selection.Active)

# col_selection.create_Dropdown(
#     elements=subject_selection.Active.dates_cols, 
#     fun=lambda Active=subject_selection.Active : col_selection.lecture_selected(Active=Active))
# # -------------------------------------------------------------------------------------------


##############  SHOWING THE GUI 
update_time_date_labels(time_label, date_label, root)
end = time.time()
print(f"Execution time of the program is -------> {(end-start)*100:.3f}ms\n")
root.mainloop()
