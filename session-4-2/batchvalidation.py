# Validate list of ages
ages = [25, -5, 30, 150, 45, 'invalid', 67, 0, 120]
valid_ages = []
invalid_ages = []
for age in ages:
# Check if numeric
    if not isinstance(age, (int, float)):
        invalid_ages.append((age, 'Not a number'))
    continue
# Check range
if 0 <= age <= 120:
    valid_ages.append(age)
else:
    invalid_ages.append((age, 'Out of range'))
print(f'Valid: {len(valid_ages)} items')
print(f'Invalid: {len(invalid_ages)} items')
print(f'Invalid data: {invalid_ages}')