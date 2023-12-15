import tkinter
from tkinter import scrolledtext 
from tkinter import *

from pandastable import Table, TableModel
import serial
import time
from database1 import *

def add_to_status(text):
    status.configure(state='normal')
    status.insert(tk.INSERT , text + '\n')
    status.configure(state='disabled')
    status.update()

def runningAtt():
    print('INATATIING ATTENDANCE PROCESS')
    add_to_status('Starting attandence')
    
    newColName = create_new_column(subjectRecords[activeSubject][0])

    try:
        serial_port = 'COM4'
        baud_rate = 115200
        
        ser = serial.Serial(serial_port, baud_rate, timeout=None)
        line = ''
        
        while (line != 'C3 13 F5 FA'):
            line = ser.readline().decode('utf-8').strip()
            
            if (line == 'C3 13 F5 FA'):
                print('exiting')
                line = ''
                add_to_status('Attendance is complete')
                return
        
            (new_SID , new_NAME) = StudentInfo(studentRecord, line)
            
            if ((new_SID , new_NAME) != (str(00000000), 'I am a ghost')):                   

                print(f"SID:  {new_SID},  NAME:  {new_NAME}\n")
                add_to_status(f"SID:  {new_SID},  NAME:  {new_NAME}")
                
                add_value_to_column_sid_wise(df = subjectRecords[activeSubject][0], column_name = newColName , sid_value= new_SID , value_to_add=1)
                print(subjectRecords[activeSubject][0])
                
                middle.table.redraw()
                
                lcdDisplay = str(new_SID + "*" + new_NAME)
                ser.write(lcdDisplay.encode('utf-8'))
                time.sleep(2.2)
        


    except serial.SerialException:
        print('Your ESP32 is not connected')
        add_to_status(f"Failed to connect with ESP32.")
    
    finally:
        print('att over')
        if 'ser' in locals():
            ser.close()
        print(subjectRecords[activeSubject][0])
        
        subjectRecords[activeSubject][0].to_csv(subjectRecords[activeSubject][1], index=False)


def update_time_date_labels():
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d - %m - %Y")
    time_label.config(text="Time: " + current_time)
    date_label.config(text="Date: " + current_date)
    root.after(1000, update_time_date_labels)  # Update every second

def subject_selected(showingSubject):
    # showingSubject = sub.get()
    subject_label.config(text="Subject: " + showingSubject)
    print(f"Showing {showingSubject} Attandence Record")
    show_db(showingSubject)

subjectRecords = {
            'CLass_List': (studentRecord, 'CLass List.csv'),
            'Power Electronics': (electronics, 'PowerElectronics.csv'), 
            'Control System': (control, 'ControlSystem.csv'),
            'Power System': (system, 'PowerSystem.csv')
        }
        
def show_db(subject):
    global activeSubject
    activeSubject = subject
    middle.table = Table(middle, dataframe=subjectRecords[subject][0], showtoolbar=False, showstatusbar=False ,editable=False, height = 550, width = 700)
    middle.table.show()


# global activeSubject
#################################Create the main window #######################
root = tk.Tk()
root.geometry("1200x800")
# root.attributes('-fullscreen', True)
root.title("RFID Attendance System")

################################# TOP_L FRAME #######################
top_L = tk.Frame(root)
top_L.grid(row=0, column=0, pady=20, padx=20)

heading_label = tk.Label(top_L, text="Electrical Department", font=("Helvetica", 24))
date_label = tk.Label(top_L, text="Current Date: ", font=("Helvetica", 12))
time_label = tk.Label(top_L, text="Current Time: ", font=("Helvetica", 12))

heading_label.grid()
date_label.grid()
time_label.grid()


################################# TOP_R FRAME #######################
top_R = tk.Frame(root)
top_R.grid(row=0, column=1, pady=20, padx=20)

sub = tk.StringVar()
curr_sub = tk.OptionMenu(top_R, sub ,'CLass_List', 'Power Electronics', 'Control System', 'Power System', command = subject_selected)
subject_label = tk.Label(top_R, text="Subject :", font=("Helvetica", 12))

start_att = tk.Button(top_R, text='Start\nattandence', command=runningAtt)


curr_sub.grid()
subject_label.grid()

################################# DATABASE FRAME #######################

middle = tk.Frame(root)
middle.grid(row=1, column=0, pady=20, padx=20)

################################# STATUS FRAME #######################
bottom = tk.Frame(root)
bottom.grid(row=1, column=1, pady=20, padx=20)

status = scrolledtext.ScrolledText(bottom, wrap = tk.WORD, width =60, height = 25, font = ("Times New Roman",12))
status.grid()

# ################################# TOP_R FRAME #######################
# top_R = tk.Frame(root)
# top_R.grid(row=0, column=1, pady=20, padx=20)

start_att.grid(row=0, column=3, padx=70)
# stop_att.grid(row=0, column=5, padx=40)

update_time_date_labels()
root.mainloop()
