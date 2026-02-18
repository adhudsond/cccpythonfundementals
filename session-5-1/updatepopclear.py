student = {'name': 'Bob', 'age': 20}
# Update with new data
new_data = {'major': 'CS', 'gpa': 3.8}
student.update(new_data)
print(student)
# {'name': 'Bob', 'age': 20, 'major': 'CS', 'gpa': 3.8}
# Pop (remove and return)
age = student.pop('age')
print(f'Removed age: {age}') # 20
print(student) # age is gone
# Clear all
student.clear()
print(student) # {}
# Still a dictionary, just empty!