students = {
'Alice': {'age': 20, 'gpa': 3.8}
}
# Add new student (outer level)
students['Bob'] = {'age': 21, 'gpa': 3.6}
# Add field to existing student (inner level)
students['Alice']['major'] = 'CS'
# Update nested value
students['Alice']['gpa'] = 3.9
print(students['Alice'])
# {'age': 20, 'gpa': 3.9, 'major': 'CS'}
# Build up complex structures piece by piece!