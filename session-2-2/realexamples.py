# Extract specific column from data
students = [
['Alice', 95, 'A'],
['Bob', 87, 'B'],
['Carol', 92, 'A']
]
names = [student[0] for student in students]
# ['Alice', 'Bob', 'Carol']
# Convert text labels to numbers (ML!)
labels = ['yes', 'no', 'yes', 'yes', 'no']
binary = [1 if label == 'yes' else 0 for label in labels]
# [1, 0, 1, 1, 0]
# This is feature engineering!
# Core ML skill!