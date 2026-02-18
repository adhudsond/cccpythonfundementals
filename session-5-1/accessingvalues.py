student = {'name': 'Alice', 'age': 25, 'major': 'CS'}
# Direct access (square brackets)
print(student['name']) # Alice
# print(student['gpa']) # KeyError! (doesn't exist)
# Safe access (.get method)
print(student.get('name')) # Alice
print(student.get('gpa')) # None
print(student.get('gpa', 0.0)) # 0.0 (default)
# When to use each:
# [ ]: When you kmow key exists
# .get(): When key might not exist
# .get() prevents crashes!