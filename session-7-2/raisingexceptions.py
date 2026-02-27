# Validate age
def set_age(age):
    if not isinstance(age, int):
        raise TypeError('Age must be an integer')
    if age < 0:
        raise ValueError('Age cannot be negative')
    if age > 150:
        raise ValueError('Age too high (max 150)')
    return age
# Usage:
try:
    age = set_age(-5)
except ValueError as e:
    print(f'Error: {e}') # Age cannot be negative
# Function enforces its requirements!