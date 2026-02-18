student = {'name': 'Alice', 'age': 25}
# Check before access
if 'name' in student:
    print(student['name']) # Alice
if 'gpa' in student:
    print(student['gpa'])
else:
    print('GPA not recorded') # This runs
# Or use .get() with default
gpa = student.get('gpa', 0.0)
print(f'GPA: {gpa}') # GPA: 0.0
name = student.get('name', 'Unknown')
print(f'Name: {name}') # Name: Alice
# Prevents crashes, handles missing data!