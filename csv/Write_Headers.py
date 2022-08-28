# importing required libraries
import csv

# csv fields:-
fieldnames = ['NAME', 'BRANCH', 'ROLL', 'SECTION', 'AGE']

with open('../students.csv', 'w+', encoding='UTF8', newline='') as f:
	writer = csv.DictWriter(f, fieldnames=fieldnames)
	writer.writeheader()
	print("Headers or Columns are Created.")

