import csv
# Data as list of dicts
students = [
{'name': 'Alice', 'age': 25, 'score': 95},
{'name': 'Bob', 'age': 30, 'score': 87},
{'name': 'Carol', 'age': 28, 'score': 92}
]
# Write with DictWriter
with open('students.csv', 'w', newline='') as file:
    fieldnames = ['name', 'age', 'score']
writer = csv.DictWriter(file, fieldnames=fieldnames)
writer.writeheader() # Writes column names
writer.writerows(students)
# Read with DictReader
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
for row in reader:
    print(f"{row['name']}: {row['score']}")