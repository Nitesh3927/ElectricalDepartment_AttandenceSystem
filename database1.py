import pandas as pd
import os

def StudentInfo(df, rfid):

    matching_row = df[df['RFID'] == rfid]
    if not matching_row.empty:
        sid_value = str(matching_row.iloc[0]['SID'])
        name_value = str(matching_row.iloc[0]['NAME'])
        print(f"The RFID :  {rfid}  belongs to  {name_value}, SID: {sid_value}")
        return (sid_value, name_value)
    else:
        return (str(00000000), 'Your RFID card is not matching')


def NewColumn(df):

    dtt = datetime.now().strftime("%d %b, %a")
    prevName = df.columns[-1]
    if (prevName == 'NAME'):
        df[f'L-1 {datetime.now().strftime("%d %b, %a")}'] = 0
        return f'L-1 {datetime.now().strftime("%d %b, %a")}'

    newColName = f"L-{int(prevName.replace('-',' ').split()[1])+1} {dtt}" 
    df[newColName] = 0  
    return str(newColName)


def AttandenceAddition(df, column_name, sid_value, value_to_add):
   
    if column_name not in df.columns:
        print("Column does not exist.")
        return
    df.loc[df['SID'] == sid_value, column_name] = value_to_add
    print(f'ADDED ATTENDACE FOR SID {sid_value}')
    return


csv_files = list(filter(lambda f: f.endswith('.csv'), os.listdir("./")))
csv_files.remove('Class Lists.csv')

ClassList = pd.read_csv("Class Lists.csv")

database = dict()
database['Class List']= [ClassList, 'ClassList', 'Class Lists.csv']
for file_name in csv_files:
    db = pd.read_csv(file_name)
    subjectName = file_name[:-4]
    database[subjectName] = [db, subjectName, file_name]
