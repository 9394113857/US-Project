# importing required libraries
import csv
from email import header

import mysql.connector

# DB Connection
dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="",
database = "usa"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# Query passing to the cursor execute()
query = "SELECT * FROM student WHERE BRANCH = 'cse' and AGE <= 18;"
cursorObject.execute(query)

myresult = cursorObject.fetchall() # fetchall() will return as list object
print(type(myresult))

for x in myresult:
	print(x)

# disconnecting from server
dataBase.close()
