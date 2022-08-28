import csv
rows = []
with open("../students.csv", 'r') as file:
    csvreader = csv.reader(file)
    headers = next(csvreader)
    for row in csvreader:
        rows.append(row)

print(headers)
for rowss in rows:
    print(rowss)