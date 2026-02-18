# Student grades: [student][subject]
# Columns: Math, English, Science
grades = [
[95, 87, 92], # Alice
[88, 90, 85], # Bob
[92, 88, 94], # Carol
[78, 85, 80] # David
]
# Access specific grade
print(grades[0][0]) # 95 (Alice's Math)
print(grades[1][2]) # 85 (Bob's Science)
# Get all of Alice's grades
print(grades[0]) # [95, 87, 92]
# This is like Excel!
# Row 1, Column 1 = grades[0][0]