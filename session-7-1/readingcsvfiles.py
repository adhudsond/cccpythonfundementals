import csv
# Read CSV file
with open('students.csv', 'r') as file:
    reader = csv.reader(file)
# Skip header
header = next(reader)
print(f'Columns: {header}')
# Process data rows
for row in reader:
    name, age, score = row
print(f'{name}: {score}')
# Output:
# Columns: ['Name', 'Age', 'Score']
# Alice: 95
# Bob: 87
# Carol: 92
# CSV reader handles parsing!