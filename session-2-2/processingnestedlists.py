grades = [
[95, 87, 92],
[88, 90, 85],
[92, 88, 94],
[78, 85, 80]
]
# Calculate average for each student
for student_grades in grades:
    avg = sum(student_grades) / len(student_grades)
print(f'Average: {avg:.1f}')
# Output:
# Average: 91.3
# Average: 87.7
# Average: 91.3
# Average: 81.0
# Or with comprehension!
avgs = [sum(row)/len(row) for row in grades]