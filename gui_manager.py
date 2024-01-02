from datetime import datetime
from pandastable import Table
from data_manager import database
from tkinter import Label, StringVar, OptionMenu, _setit
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file = logging.FileHandler(filename='GeneralFlow.log')

formatter = logging.Formatter('\n%(module)s - %(funcName)s --> \n%(message)s')
file.setFormatter(formatter)

logger.addHandler(file)


def show_db(middle, ActiveSubject):  
        middle.table = Table(middle, dataframe=ActiveSubject.df, showtoolbar=False, showstatusbar=False ,editable=False, height = 550, width = 600)
        middle.table.show()
        logger.info(f'{ActiveSubject.subjectName} showing')

def update_options(new_choices, variable, option_menu):
    logger.info(f'yoooooooooooooooooooooo')
    variable.set(new_choices[0])  # Set new initial value
    option_menu['menu'].delete(0, 'end')  # Clear existing options
    for choice in new_choices:
        option_menu['menu'].add_command(label=choice, command=_setit(variable, choice))

class DropDowns:
    def __init__(self, root):
        self.var = StringVar()
        # self.Active = Active
        self.root = root
        # self.text = ''
        # self.list = []
        # self.database_frame = database_frame

    def create_Label(self):
        self.label = Label(self.root, text= self.text, font=("Helvetica", 12))
        self.label.grid()
        
    
    def create_Dropdown(self, fun= None):
        self.dropDown = OptionMenu(self.root, self.var, *self.list, command=fun)
        self.dropDown.grid()

    

    # def lecture_selected(self,Active):
    #     logger.info(f'{Active.dates_cols},  {Active.main_cols}  {Active.all_cols}')
    #     update_options(new_choices=Active.dates_cols, variable=self.var, option_menu=self.dropDown)
    #     # self.ActiveDate = self.var.get()
    #     # logger.info(f"Date list updated\nActive Date: {self.ActiveDate}")
        
class SubjectSelection(DropDowns):
    def __init__(self, root, database_frame=None):
        super().__init__(root)
        self.root = root
        self.database_frame = database_frame
        self.text = 'Subject selected ->'
        self.list = [x.subjectName for x in database]

        self.create_Label()
        self.create_Dropdown(fun=self.subject_selected)
    
    def subject_selected(self, event):
        showingSubject = self.var.get()
        self.label.config(text="Subject: " + showingSubject)
        
        for x in database:
            if x.subjectName == showingSubject:
                self.Active = x
        
        logger.info(f'{showingSubject} selected')
        # self.root.update_idletasks()
        show_db(self.database_frame, self.Active)
        

class DateSelection(DropDowns):
    def __init__(self, root, database_frame=None):
        super().__init__(root)
        self.root = root
        self.database_frame = database_frame
        self.text = 'Date selected ->'
        self.list = ['NONE']

        self.create_Label()
        self.create_Dropdown(fun=self.change_options)

    def change_options(self, event):
        self.dropDown['menu'].delete(0, 'end')
        selected_category = SubjectSelection.var.get()

        self.var.set('')
        for x in database:
                if x.subjectName == selected_category:
                    subject_selected = x

        for x in subject_selected.dates_cols:
            self.dropDown['menu'].add_command(label=x, command=_setit(self.var, x))

def update_time_date_labels(time_label, date_label, root):
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d - %m - %Y")
    time_label.config(text="Time: " + current_time)
    date_label.config(text="Date: " + current_date)
    root.after(1000, lambda: update_time_date_labels(time_label, date_label, root))
