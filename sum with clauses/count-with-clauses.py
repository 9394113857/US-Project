# importing required libraries

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

# 1.Returns the count of rows:-
query1 = "SELECT COUNT(NAME) FROM student;"
cursorObject.execute(query1)
studentsCount = cursorObject.fetchall() # fetchall() will return as list object
print("Count of Name :")
for i in studentsCount:
	print(i)

# 2.Returns the count of all rows for age:-
query2 = "SELECT COUNT(*) FROM student where age = 18;"
cursorObject.execute(query2)
ageCondition = cursorObject.fetchall() # fetchall() will return as list object
print("Age = 18")
for i in ageCondition:
	print(i)

# 3.Returns the count of rows for GROUP BY Clause:-
query3 = "SELECT NAME, AGE, SECTION, COUNT(*) FROM student GROUP BY BRANCH;"
cursorObject.execute(query3)
GroupBYCSE = cursorObject.fetchall() # fetchall() will return as list object
print("Group By BRANCH:")
for i in GroupBYCSE:
	print(i)

# 4.Returns the count of rows for HAVING and ORDER BY Clauses:-
query4 = "SELECT NAME, AGE, SECTION, COUNT(*) FROM student GROUP BY AGE HAVING COUNT(*) >= 2 ORDER BY COUNT(*);"
cursorObject.execute(query4)
HAVINGandORDERBY = cursorObject.fetchall() # fetchall() will return as list object
print("Having and Order By:")
for i in HAVINGandORDERBY:
	print(i)

# disconnecting from server
dataBase.close()
