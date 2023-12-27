from datetime import datetime
from pandastable import Table
from database import database
from tkinter import Label, StringVar, OptionMenu
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file = logging.FileHandler(filename='GeneralFlow.log', )

formatter = logging.Formatter('\n%(module)s - %(funcName)s --> \n%(message)s')
file.setFormatter(formatter)

logger.addHandler(file)


def show_db(middle, ActiveSubject):  
        middle.table = Table(middle, dataframe=ActiveSubject.df, showtoolbar=False, showstatusbar=False ,editable=False, height = 550, width = 600)
        middle.table.show()
        logger.info(f'{ActiveSubject.subjectName} showing')

def updateOptions(opMenu, newValues):
    opMenu.configure(state='normal')  # Enable drop down
    menu = opMenu['menu']

    # Clear the menu.
    menu.delete(0, 'end')
    for name in newValues:
        # Add menu items.
        menu.add_command(label=name, command=lambda name=name: var.set(name))
        # OR menu.add_command(label=name, command=partial(var.set, name))


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
        
        for x in database:
            if x.subjectName == event:
                self.Active = x
        
        logger.info(f'{showingSubject} selected')
        self.root.update_idletasks()
        show_db(self.database_frame, self.Active)
    
    def lecture_selected(self, event):
        updateOptions(opMenu=self.dropDown, newValues=self.list)
        logger.info(f"\n\nlecture_selected called: {self.Active} selected")
        # logger.info(event)
        # logger.info(ActiveSubject.all_cols)
        # logger.info(self.Active)
        # logger.info(ActiveSubject.dates_cols)
        

def update_time_date_labels(time_label, date_label, root):
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d - %m - %Y")
    time_label.config(text="Time: " + current_time)
    date_label.config(text="Date: " + current_date)
    root.after(1000, lambda: update_time_date_labels(time_label, date_label, root))
