# Multiple defaults
def create_user(name, age=18, city='Unknown'):
    print(f'Name: {name}')
    print(f'Age: {age}')
    print(f'City: {city}')
# Different ways to call:
create_user('Alice')
# Name: Alice, Age: 18, City: Unknown
create_user('Bob', 25)
# Name: Bob, Age: 25, City: Unknown
create_user('Carol', 30, 'Boston')
# Name: Carol, Age: 30, City: Boston
# Mix required and optional!
# Required first, defaults after
