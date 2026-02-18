grades = {'math': 85, 'english': 92, 'science': 88}
# Loop through keys only
for subject in grades:
    print(subject) # math, english, science
# Loop through values only
for grade in grades.values():
    print(grade) # 85, 92, 88
# Loop through both
for subject, grade in grades.items():
    print(f'{subject}: {grade}')
# Output:
# math: 85
# english: 92
# science: 88
# Use .items() most of the time!