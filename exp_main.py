# from data_manager import database
from exp_gui_manager import GUImain
# from tkinter import Tk,  Frame
import logging
# import tkinter as tk

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file = logging.FileHandler(filename='GeneralFlow.log', mode='w')

formatter = logging.Formatter('%(module)s-%(funcName)s --> %(message)s')
file.setFormatter(formatter)

logger.addHandler(file)



GUImain()
# app.root.mainloop()

























# # -----------------------------------------------------
# ###############  MAIN WINDOW 
# root = Tk()
# root.geometry("500x500")
# root.title("RFID Attendance System")

# ##############  TOP_L FRAME 
# top_L = Frame(root)
# top_L.grid(row=0, column=0, pady=20, padx=20)

# ##############  TOP_R FRAME 
# top_L = Frame(root)
# top_R.grid(row=0, column=1, pady=10, padx=20)

# subject_selection = DropDowns(root=top_R, text='Subject u want to see:')
# subject_selection.create_Dropdown(elements=[x.subjectName for x in database], fun= subject_selection.subject_selected)

# col_selection = DropDowns(root=top_R, text='Select lecture')
# col_selection.create_Dropdown(elements=ActiveSubject.dates_cols)

# ##############  DATABASE FRAME 
# middle = Frame(root)
# middle.grid(row=1, column=0, pady=20, padx=20)

# ##############  STATUS FRAME

# ##############  SHOWING THE GUI 
# root.mainloop()
# # -----------------------------------------------------

