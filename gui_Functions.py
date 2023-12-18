from datetime import datetime
# from main import date_label, time_label, root, ActiveSubject, middle
from database import database

dtt = datetime.now().strftime("%d %b, %a")

def update_time_date_labels(time_label, date_label, root):
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d - %m - %Y")
    time_label.config(text="Time: " + current_time)
    date_label.config(text="Date: " + current_date)
    root.after(1000, lambda: update_time_date_labels(time_label, date_label, root))

def subject_selected(showingSubject, Sub_OptionMenu__Label):
    # showingSubject = sub.get()
    Sub_OptionMenu__Label.config(text="Subject: " + showingSubject)
    print(f"Showing {showingSubject} Attandence Record")
    show_db(showingSubject)
    global ActiveSubject
    ActiveSubject = str(showingSubject)

def show_db(subject):  
    middle.table = Table(middle, dataframe=database[subject][0], showtoolbar=False, showstatusbar=False ,editable=False, height = 550, width = 700)
    middle.table.show()
