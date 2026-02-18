# Keep asking until valid input
age = -1 # Invalid start value
while age < 0 or age > 120:
    age = int(input('Enter your age (0-120): '))
if age < 0 or age > 120:
    print('Invalid! Try again.')
print(f'Valid age: {age}')
# Loop continues until valid age entered
# Don't know how many tries it takes!
# Perfect use case for while!
# This is input validation!