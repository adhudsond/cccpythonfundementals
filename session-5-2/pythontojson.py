import json
# Python dictionary
person = {
'name': 'Alice',
'age': 25,
'city': 'Boston',
'skills': ['Python', 'ML', 'Data Science']
}
# Convert to JSON string
json_string = json.dumps(person)
print(json_string)
# {"name": "Alice", "age": 25, "city": "Boston", ...
# Pretty print (indented)
json_pretty = json.dumps(person, indent=2)
print(json_pretty)
# {
# "name": "Alice",
# "age": 25,
# ...