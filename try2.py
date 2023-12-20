from database import *
from gui_Functions import DropDowns
from tkinter import Tk, Frame

def show_db(middle, ActiveSubject):  
        middle.table = Table(middle, dataframe=ActiveSubject.df, showtoolbar=False, showstatusbar=False ,editable=False, height = 550, width = 700)
        middle.table.show()

ActiveSubject = 'ClassList'

###############  MAIN WINDOW 
root = Tk()
root.geometry("500x500")
root.title("RFID Attendance System")

##############  TOP_L FRAME 
top_L = Frame(root)
top_L.grid(row=0, column=0, pady=20, padx=20)

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

##############  SHOWING THE GUI 
root.mainloop()

