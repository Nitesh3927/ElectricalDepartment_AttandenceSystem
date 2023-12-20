import pandas as pd
import os

class DatabaseHandler:
    def __init__(self, csv_file_name):
        self.csvFileName = csv_file_name
        self.subjectName = csv_file_name[:-4]
        self.df = pd.read_csv(csv_file_name)
        
        self.all_cols = list(self.df.columns)
        self.main_cols = [x for x in self.df.columns if x in ('SID', 'NAME', 'RFID')]
        self.dates_cols = [x for x in self.df.columns if x not in ('SID', 'NAME', 'RFID')]
    
    def __str__(self):
        return f'Subject Name : {self.subjectName}\nFile Name : {self.csvFileName}\nAll Cols  : {self.all_cols}\nMain Cols  : {self.main_cols}\nDates Cols : {self.dates_cols}\nDATABASE --->\n[{self.df}\n'    
        
def StudentInfo(df, rfid):

    matching_row = df[df['RFID'] == rfid]
    if not matching_row.empty:
        sid_value = str(matching_row.iloc[0]['SID'])
        name_value = str(matching_row.iloc[0]['NAME'])
        print(f"The RFID :  {rfid}  belongs to  {name_value}, SID: {sid_value}")
        return (sid_value, name_value)
    else:
        return (str(00000000), 'Your RFID card is not matching')

def NewColumn(df, newColName):
    df[newColName] = 0

def AttandenceAddition(df, column_name, sid_value, value_to_add):
   
    if column_name not in df.columns:
        print("Column does not exist.")
        return
    df.loc[df['SID'] == sid_value, column_name] = value_to_add
    print(f'ADDED ATTENDACE FOR SID {sid_value}')
    return


csv_files = list(filter(lambda f: f.endswith('.csv'), os.listdir("./")))

database =[DatabaseHandler(x) for x in csv_files]

print(database)
# for i in database:
#     print(i)
#     print()


# # DATABASE IMPLIMEMTAION 
# database = dict()
# for file_name in csv_files:
#     db = pd.read_csv(file_name)
#     subjectName = file_name[:-4]
#     database[subjectName] = [db, subjectName, file_name]
#     # database[subjectName] = [subjectName, file_name]
