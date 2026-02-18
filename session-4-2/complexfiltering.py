# Filter students: good grades AND good attendance
students = [
{'name': 'Alice', 'grade': 95, 'attendance': 90},
{'name': 'Bob', 'grade': 92, 'attendance': 75},
{'name': 'Carol', 'grade': 78, 'attendance': 95},
{'name': 'David', 'grade': 88, 'attendance': 85}
]
honors = []
for student in students:
    if student['grade'] >= 90 and student['attendance'] >= 80:
        honors.append(student['name'])
print(f'Honors students: {honors}')
# ['Alice', 'David']
# Multi-criteria filtering!