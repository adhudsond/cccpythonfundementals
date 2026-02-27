# Handle invalid input
try:
    age = int(input('Enter your age: '))
    print(f'You are {age} years old')
except ValueError:
    print('Error: Please enter a valid number')
    print('Program continues!')
# If user enters 'abc':
# Error: Please enter a valid number
# Program continues!
# If user enters '25':
# You are 25 years old
# Program continues!
# No crash either way!