from datetime import datetime
from pandastable import Table
from database import database
from tkinter import Label, StringVar, OptionMenu

def show_db(middle, ActiveSubject):  
        middle.table = Table(middle, dataframe=ActiveSubject.df, showtoolbar=False, showstatusbar=False ,editable=False, height = 550, width = 700)
        middle.table.show()
        print(f"show_db called: {ActiveSubject.subjectName} showing\n\n")


class DropDowns:
    def __init__(self, root, text, database_frame=None):
        self.var = StringVar()
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
        
        print(f"subject_selected called: {showingSubject} selected")
        
        for x in database:
            if x.subjectName == event:
                ActiveSubject = x
        
        show_db(self.database_frame, ActiveSubject)


def update_time_date_labels(time_label, date_label, root):
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d - %m - %Y")
    time_label.config(text="Time: " + current_time)
    date_label.config(text="Date: " + current_date)
    root.after(1000, lambda: update_time_date_labels(time_label, date_label, root))


