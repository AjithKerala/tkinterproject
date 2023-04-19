import mysql.connector
database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="allbase"
)
dbCursor=database.cursor()
sql="Create Table tkmainprojectmain (Manbertype char(10) not null primary key,ref char(30) not null,Title char(30) not null,FirstName char(30) not null,LastName char(30) not null,Address char(30) not null,postcode char(30) not null,Booktitle char(30) not null,Dateissued char(30) not null,DueDate char(30) not null,mobileno char(12) not null,price char(100) not null,Returndate char(20) not null)"
dbCursor.execute(sql)
database.commit()
database.close()