from datetime import datetime

from database import database
from tkinter import Label, StringVar, OptionMenu

class DropDowns:
    def __init__(self, root, text):
        self.var = StringVar()
        self.root = root
        self.label = Label(self.root, text= text, font=("Helvetica", 12))
        self.label.grid()
    
    def create_Dropdown(self, elements, fun=None):
        self.list = elements
        self.dropDown = OptionMenu(self.root, self.var, *self.list, command=fun)
        self.dropDown.grid()

    def subject_selected(self,event):
        showingSubject = self.var.get()
        self.label.config(text="Subject: " + showingSubject)
        
        print(f"Showing {showingSubject} Attandence Record")
        
        for x in database:
            if x.subjectName == event:
                ActiveSubject = x
        
        show_db(middle, ActiveSubject)


def update_time_date_labels(time_label, date_label, root):
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d - %m - %Y")
    time_label.config(text="Time: " + current_time)
    date_label.config(text="Date: " + current_date)
    root.after(1000, lambda: update_time_date_labels(time_label, date_label, root))
