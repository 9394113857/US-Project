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
query = "SELECT NAME, ROLL FROM STUDENT"
cursorObject.execute(query)

myresult = cursorObject.fetchall() # fetchall() will return as list object
print(type(myresult))

for x in myresult:
	print(x)

# c = csv.writer(open("temp.csv","wb"))
# c.writerow(myresult)

# rows = cursorObject.fetchall()
# fp = open('/tmp/file.csv', 'w')

# csv header
# fieldnames = ['NAME', 'BRANCH', 'ROLL', 'SECTION', 'AGE']

fp = open('file.csv', 'a')
myFile = csv.writer(fp)
myFile.writerows(myresult) # myresult is a resultset
fp.close()

# disconnecting from server
dataBase.close()
