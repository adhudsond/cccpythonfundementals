# Grade book with multiple students
gradebook = {
'Alice': {'math': 95, 'english': 92},
'Bob': {'math': 87, 'english': 90},
'Carol': {'math': 92, 'english': 88}
}
# Calculate average for each student
for name, grades in gradebook.items():
    total = sum(grades.values())
avg = total / len(grades)
print(f'{name}: {avg:.1f}')
# Output:
# Alice: 93.5
# Bob: 88.5
# Carol: 90.0
# Nested loop processes all data!