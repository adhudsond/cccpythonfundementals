student = {'name': 'Alice', 'age': 25, 'major': 'CS'}
# Get all keys
keys = student.keys()
print(keys) # dict_keys(['name', 'age', 'major'])
# Get all values
values = student.values()
print(values) # dict_values(['Alice', 25, 'CS'])
# Get all key-value pairs
items = student.items()
print(items)
# dict_items([('name', 'Alice'), ('age', 25), ('major', 'CS')])
# Convert to list if needed:
key_list = list(student.keys())