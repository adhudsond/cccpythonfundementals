# Students with detailed info
students = {
'Alice': {
'age': 20,
'major': 'CS',
'gpa': 3.8
},
'Bob': {
'age': 21,
'major': 'Math',
'gpa': 3.6
}
}
# Access nested data
print(students['Alice']) # Whole dict
# {'age': 20, 'major': 'CS', 'gpa': 3.8}
print(students['Alice']['major']) # Specific value
# CS
# Two levels of access!