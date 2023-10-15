import pyodbc
import pandas as pd

class SQLDBWriter:
    def DBWriter(df, tablename):

    # insert data from csv file into dataframe.
    # working directory for csv file: type "pwd" in Azure Data Studio or Linux
    # working directory in Windows c:\users\username
    df = pd.read_csv("c:\\user\\username\department.csv")
    # Some other example server values are
    # server = 'localhost\sqlexpress' # for a named instance
    # server = 'myserver,port' # to specify an alternate port
    server = 'yourservername' 
    database = 'AdventureWorks' 
    username = 'username' 
    password = 'yourpassword' 
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    # Insert Dataframe into SQL Server:
    for index, row in df.iterrows():
        cursor.execute("INSERT INTO HumanResources.DepartmentTest (DepartmentID,Name,GroupName) values(?,?,?)", row.DepartmentID, row.Name, row.GroupName)
    cnxn.commit()
    cursor.close()
