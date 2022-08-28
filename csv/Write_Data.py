# importing required libraries
import csv
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
query = "SELECT * FROM STUDENT"
cursorObject.execute(query)

myresult = cursorObject.fetchall() # fetchall() will return as list object
print(type(myresult))

for x in myresult:
	print(x)

# c = csv.writer(open("temp.csv","wb"))
# c.writerow(myresult)

# writing data to csv file:
fp = open('../students.csv', 'a')
myFile = csv.writer(fp)
myFile.writerows(myresult) # myresult is a resultset
fp.close()

# disconnecting from server
dataBase.close()
