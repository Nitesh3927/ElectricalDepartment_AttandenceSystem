from datetime import datetime
from pandastable import Table
from database import database
from tkinter import Label, StringVar, OptionMenu
import logging

def show_db(middle, ActiveSubject):  
        middle.table = Table(middle, dataframe=ActiveSubject.df, showtoolbar=False, showstatusbar=False ,editable=False, height = 550, width = 600)
        middle.table.show()
        print(f"show_db called: {ActiveSubject.subjectName} showing")
        print(f'ID of ActiveSubject_after_assignment ======= {id(ActiveSubject)}\n\n')


class DropDowns:
    def __init__(self, root, text, Active=None, database_frame=None):
        self.var = StringVar()
        self.Active = Active
        self.root = root
        self.label = Label(self.root, text= text, font=("Helvetica", 12))
        self.label.grid()
        self.database_frame = database_frame
    
    def create_Dropdown(self, elements, fun=None):
        self.list = elements
        self.dropDown = OptionMenu(self.root, self.var, *self.list, command=fun)
        self.dropDown.grid()

    def subject_selected(self,event):
        showingSubject = self.var.get()
        self.label.config(text="Subject: " + showingSubject)
        
        print(f"\nsubject_selected called: {showingSubject} selected")
        # print(f'ID of showingSubject : {id(showingSubject)}')
        
        for x in database:
            if x.subjectName == event:
                self.Active = x
                # global ActiveSubject
                # ActiveSubject = x
        
        print(f'ID of ActiveSubject_after_assignment ======= {id(self.Active)}')
        
        show_db(self.database_frame, self.Active)
    
    def lecture_selected(self, event):
        print(f"\n\nlecture_selected called: {self.Active} selected")
        # print(event)
        # print(ActiveSubject.all_cols)
        # print(self.Active)
        # print(ActiveSubject.dates_cols)
        

def update_time_date_labels(time_label, date_label, root):
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d - %m - %Y")
    time_label.config(text="Time: " + current_time)
    date_label.config(text="Date: " + current_date)
    root.after(1000, lambda: update_time_date_labels(time_label, date_label, root))
