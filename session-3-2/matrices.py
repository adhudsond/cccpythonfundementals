# Student grades: [student][subject]
grades = [
[95, 87, 92], # Alice: Math, English, Science
[88, 90, 85], # Bob
[92, 88, 94] # Carol
]
# Calculate average for each student
for student_num, student_grades in enumerate(grades, 1):
    total = 0
for grade in student_grades:
    total += grade
avg = total / len(student_grades)
print(f'Student {student_num} average: {avg:.1f}')
# Output:
# Student 1 average: 91.3
# Student 2 average: 87.7
# Student 3 average: 91.3