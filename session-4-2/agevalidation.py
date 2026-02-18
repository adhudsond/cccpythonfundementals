# Validate age input
def validate_age(age):
    errors = []
    # Check type
    if not isinstance(age, int):
        errors.append('Age must be integer')
        return False, errors
    # Check range
    if age < 0:
        errors.append('Age cannot be negative')
    if age > 120:
        errors.append('Age too high (max 120)')
    is_valid = len(errors) == 0
    return is_valid, errors
# Test it
valid, errs = validate_age(25)
print(valid) # True
valid, errs = validate_age(-5)
print(valid, errs) # False, ['Age cannot be negative']