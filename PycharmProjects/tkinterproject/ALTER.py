import mysql.connector
database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="allbase"
)
dbCursor=database.cursor()
aq="ALTER TABLE tkmainproject ADD PRIMARY KEY(ref)"
dbCursor.execute(aq)
database.commit()
database.close()