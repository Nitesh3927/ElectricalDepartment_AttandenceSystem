from datetime import datetime
from pandastable import Table
from data_manager import database
import tkinter as tk
from tkinter import ttk
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file = logging.FileHandler(filename='GeneralFlow.log')

formatter = logging.Formatter('%(module)s-%(funcName)s--> %(message)s')
file.setFormatter(formatter)

logger.addHandler(file)


def update_options(new_choices, variable, option_menu):
    logger.info(f'yoooooooooooooooooooooo')
    variable.set(new_choices[0])  # Set new initial value
    option_menu['menu'].delete(0, 'end')  # Clear existing options
    for choice in new_choices:
        option_menu['menu'].add_command(label=choice, command=_setit(variable, choice))

class GUImain(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1500x1000")
        self.title("RFID Attendance System")
        
        # ActiveSubject = database[0]
        # ActiveDate = database[0].dates_cols
        
        self.layouts()
        logger.info(f'GUIMAIN intilazed')
        
        self.mainloop()

    def layouts(self):        
        self.top_L = TOP_L_Frame(self)
        self.middle_L = MIDDLE_L_Frame(self)
        self.middle_R = MIDDLE_R_Frame(self)
        self.top_R = TOP_R_Frame(self, viewFrame= self.middle_L, infoFrame=self.middle_R)
    
    def Print():
        print('i am in gui main class')


class TOP_L_Frame(ttk.Frame):
    def __init__(self, master_root):
        super().__init__(master_root)
        self.grid(row=0 , column=0, padx=30, pady=20)
        
        heading_label = ttk.Label(self, text="Electrical Department", font=("Helvetica", 24))
        self.time_label = ttk.Label(self, text="Current Time: ", font=("Helvetica", 12))
        self.date_label = ttk.Label(self, text="Current Date: ", font=("Helvetica", 12))
        heading_label.grid()
        self.time_label.grid()
        self.date_label.grid()
        self.update_time_date_labels()

    def update_time_date_labels(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().strftime("%d - %m - %Y")
        self.time_label['text']= "Time: " + current_time
        self.date_label['text']= "Date: " + current_date
        self.after(1000, self.update_time_date_labels)
    
class TOP_R_Frame(ttk.Frame):
    def __init__(self, master_root, viewFrame, infoFrame):
        super().__init__(master_root)
        self.grid(row=0, column=1, padx=100, pady=20)
        
        self.date_selection = DateSelection(self)
        self.subject_selection = SubjectSelection(
            self, 
            viewFrame=viewFrame,
            date_element=self.date_selection)

class MIDDLE_L_Frame(ttk.Frame):
    def __init__(self, master_root):
        super().__init__(master_root)
        self.grid(row=1, column=0, padx=10, pady=10)
      
class MIDDLE_R_Frame(ttk.Frame):
    def __init__(self, master_root):
        super().__init__(master_root)
        self.grid(row=1, column=1, padx=10, pady=10)    

# --------------------------------------------------------------------------
class SubjectSelection(TOP_R_Frame):
    def __init__(self, root, viewFrame, date_element):
        self.date_element = date_element
        self.var = tk.StringVar()
        self.viewFrame = viewFrame
        self.list = [x.subjectName for x in database]
        
        self.label = ttk.Label(
            root, 
            text='Subject selected ->', 
            font=("Helvetica", 12))
        self.label.grid(row=0, column=0)
        
        self.dropDown = ttk.OptionMenu(
            root, 
            self.var, 
            *self.list, 
            command=self.subject_selected)
        self.dropDown.grid(row=1, column=0)

        print(type(self))
        print(super())
        # print(type(self.middle_R))
        print(super)
        # GUImain.Print()

    def subject_selected(self, event):
        print('entering subject selected function')
        showingSubject = self.var.get()
        self.label['text']= "Subject: " + showingSubject
        
        for x in database:
            if x.subjectName == showingSubject:
                self.ActiveSubject = x
                # break
        
        logger.info(f'{showingSubject} selected')       
        self.show_db()
        self.change_options(
            date_element=self.date_element, 
            subject_selected=self.ActiveSubject)

        print('Exiting subject selected function')

    def show_db(self):
        print('show_db')
        viewFrame = self.viewFrame 
        viewFrame.table = Table(viewFrame, dataframe=self.ActiveSubject.df, showtoolbar=False, showstatusbar=False ,editable=False, height = 550, width = 600)
        self.viewFrame.table.show()
        logger.info(f'{self.ActiveSubject.subjectName} showing')
        print('show_db')

    def change_options(self, date_element, subject_selected):
        date_dropDown = date_element.dropDown
        date_dropDown_var = date_element.var
        
        date_dropDown['menu'].delete(0, 'end')
        date_dropDown_var.set('')
        for x in self.ActiveSubject.dates_cols:
            date_dropDown['menu'].add_command(label=x, command=tk._setit(self.var, x))
# --------------------------------------------------------------------------
class DateSelection():
    def __init__(self, root):
        self.list = ['NONE']
        self.var = tk.StringVar()
        
        self.label = ttk.Label(
            root, 
            text= 'Date selected ->', 
            font=("Helvetica", 12))
        self.label.grid(row=0, column=1, padx=80)
        
        self.dropDown = ttk.OptionMenu(
            root, 
            self.var, 
            *self.list, 
            command=None)
        self.dropDown.grid(row=1, column=1, padx=80)
# --------------------------------------------------------------------------