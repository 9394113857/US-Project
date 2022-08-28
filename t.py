import csv

import pymysql

conn = pymysql.connect(server='localhost', port='3306', user='root', password='', database='usa')
cursor = conn.cursor()
query = 'SELECT * FROM student'
cursor.execute(query)
with open("output.csv", "w") as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(col[0] for col in cursor.description)
    for row in cursor:
        writer.writerow(row)
