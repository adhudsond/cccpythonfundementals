import json
# JSON string (from API, file, etc.)
json_data = '{"name": "Bob", "age": 30, "city": "NYC"}'
# Convert to Python dict
person = json.loads(json_data)
print(person)
# {'name': 'Bob', 'age': 30, 'city': 'NYC'}
# Now use like normal Python dict
print(person['name']) # Bob
person['age'] = 31
# Seamless conversion!
# Work with JSON as Python dicts