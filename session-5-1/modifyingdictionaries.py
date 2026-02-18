student = {'name': 'Bob', 'age': 20}
# Add new field
student['major'] = 'Computer Science'
print(student)
# {'name': 'Bob', 'age': 20, 'major': 'Computer Science'}
# Update existing field
student['age'] = 21
print(student['age']) # 21
# Delete a field
del student['age']
print(student)
# {'name': 'Bob', 'major': 'Computer Science'}
# Dictionaries grow and shrink dynamically!