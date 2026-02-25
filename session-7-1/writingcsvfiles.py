import csv
# Data to save
students = [
['Name', 'Age', 'Score'], # Header
['Alice', 25, 95],
['Bob', 30, 87],
['Carol', 28, 92]
]
# Write CSV file
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(students)
# Creates:
# Name,Age,Score
# Alice,25,95
# Bob,30,87
# Carol,28,92
# newline='' prevents extra blank lines