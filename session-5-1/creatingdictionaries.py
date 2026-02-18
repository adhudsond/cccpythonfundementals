# Method 1: Literal (most common)
student = {'name': 'Bob', 'grade': 85}
# Method 2: Empty then add
student = {}
student['name'] = 'Bob'
student['grade'] = 85
# Method 3: dict() function
student = dict(name='Bob', grade=85)
# All create the same dictionary!
# Use Method 1 most of the time
# Multi-line for readability:
student = {
'name': 'Bob',
'grade': 85,
'major': 'CS'
}